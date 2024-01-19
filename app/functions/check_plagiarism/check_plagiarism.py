import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from ...firebase.firebase_helper import FirebaseHelper
from ...models.check_plagiarism_model import CheckPlagiarismModel
from .recommendations import generate_video_recommendations


# Function to preprocess text using spaCy
def preprocess_text_with_spacy(text, nlp):
    doc = nlp(text)
    tokens = [
        token.text.lower() for token in doc if not token.is_punct and not token.is_stop
    ]
    return " ".join(tokens)


# Function to calculate cosine similarity
def calculate_cosine_similarity(sop, reference):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([sop, reference])
    return cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]


# references_df = pd.read_csv(r"C:\Users\bil\Desktop\sop_quality_checker\app\functions\check_plagiarism\references.csv")


references_df_in_storage = "plagiarism_reference/SOP_Plagiarism_Dataset.csv"


def check_plagiarism(input: CheckPlagiarismModel, nlp):
    references_df = FirebaseHelper.download_csv_as_df(references_df_in_storage)
    # Set initial values for highest similarity score and best matching reference
    highest_similarity = 0
    best_matching_reference = ""

    sop_text = preprocess_text_with_spacy(input.content, nlp)

    # references_df = references_df_main

    # Assume references_df is a pandas DataFrame with columns ["Owner", "Type", "SOP"]
    for index, row in references_df.iterrows():
        reference_owner = row["Owner"]
        reference_type = row["Type"]
        reference_text = preprocess_text_with_spacy(row["SOP"], nlp)

        # Check if the email matches the user's email or the type is not equal to the provided type
        # if reference_owner == owner or reference_type != type:
        #     references_df.drop(index, inplace=True)

        #     continue

        if reference_owner != input.owner_email and reference_type == input.type:
            # Calculate similarity for non-matching cases
            similarity = calculate_cosine_similarity(sop_text, reference_text)

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_matching_reference = row["SOP"]

    # print("Best matching reference document:")
    # print(best_matching_reference)
    # print("Highest Similarity Score:", highest_similarity)

    if highest_similarity < 0.5:
        # Add new data to the DataFrame (for example)
        new_data = (
            {"SOP": input.content, "Owner": input.owner_email, "Type": input.type},
        )
        new_data_df = pd.DataFrame(new_data)
        updated_references_df = pd.concat(
            [references_df, new_data_df], ignore_index=True
        )

        updated_references_df = updated_references_df.drop_duplicates(subset=["SOP"])

        # Upload the updated DataFrame back to Firebase Storage
        try:
            FirebaseHelper.upload_df_as_csv(
                updated_references_df, references_df_in_storage
            )
        except Exception as e:
            print("Error uploading updated DataFrame to Firebase Storage:", e)

    highest_similarity = min(highest_similarity, 1)
    similarity_percentage = highest_similarity * 100
    # print("Highest Similarity Score:", similarity_percentage, "%")

    uniqueness_level = 1 - highest_similarity
    uniqueness_level = max(uniqueness_level, 0)
    uniqueness_percentage = uniqueness_level * 100
    # print("Uniqueness Level:", uniqueness_percentage, "%")

    if highest_similarity > 0.5:
        message = "High likelihood of plagiarism detected in your SOP/LOM."
    elif highest_similarity > 0.3:
        message = "Moderate likelihood of plagiarism detected in your SOP/LOM."
    elif highest_similarity > 0 and highest_similarity < 0.3:
        message = "Low likelihood of plagiarism detected in your SOP/LOM."
    else:
        message = "No likelihood of plagiarism detected in your SOP/LOM."

    video_recommendations = generate_video_recommendations()

    return {
        "similarity": round(similarity_percentage),
        "uniqueness": round(uniqueness_percentage),
        "out_of": 100,
        "best_matching_reference": best_matching_reference,
        "message": message,
        "video_recommendations": video_recommendations,
    }
