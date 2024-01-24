class CustomResponses:
    university_name_found_response_messages = [
        "That's a fantastic choice! You're applying to",
        "Great, so you're interested in",
        "Wow, you've set your sights on",
        "Excellent! You're considering",
        "Impressive! You've chosen",
        "Awesome! You're applying to",
        "Brilliant! You've set your eyes on",
        "Terrific! You're applying to",
        "Outstanding! You're considering",
    ]

    no_university_name_found_response_messages = [
        "I couldn't find any university name in your SOP. Please check your SOP and make sure you have mentioned the university name in your SOP.",
        "It seems there's no university name mentioned in your SOP. It's important to include the university name when submitting your application.",
        "Your SOP doesn't appear to mention any university name. Ensure that you've clearly stated the university you're applying to in your statement.",
        "I couldn't detect any reference to a university name in your SOP. Be sure to specify the university where you intend to pursue your studies.",
        "No university name was found in your SOP. Please ensure that you've provided this important information in your statement.",
    ]

    destination_country_found_response_messages = [
        "What a great destination!",
        "Great choice!",
        "That's an excellent choice!",
        "That's a fantastic choice!",
        "That's an exciting location!",
        "A fantastic destination indeed!",
        "That's a remarkable choice!",
        "A great country to do your studies!",
        "That's a fantastic country!",
        "A fantastic destination!",
        "That's an amazing choice!",
        "Cool, I hope you will enjoy your studies there!",
        "Nice, A great future is awaiting you there!",
    ]

    destination_country_not_found_response_messages = [
        "I couldn't find any mention of the destination country in your SOP. Please check your SOP and make sure you have mentioned the destination country name.",
        "It seems the destination country is not specified in your SOP. Kindly revisit your document and make sure to include the name of the destination country for clarity.",
        "Your SOP is missing information about the destination country. Double-check your document to ensure that you have explicitly stated the name of the destination country.",
        "The destination country is not identified in your SOP. Please go through your SOP again and confirm that you have provided the necessary details about the country you are discussing.",
        "I couldn't find any reference to the destination country in your SOP. Take a moment to review your SOP and make certain that the name of the destination country is clearly mentioned.",
        "Your SOP lacks information regarding the destination country. Ensure that you have explicitly mentioned the name of the country in your document for a comprehensive overview.",
    ]

    spelling_issues_found_response = "Spelling or Grammer mistakes found. Some common terms may be flagged. Please review and consider using popular tools like Grammarly, ProWritingAid, Ginger or any online spelling/grammer checkers to ensure your SOP is error-free."
    spelling_issues_not_found_response = "No issues found. Please review and consider using popular tools like Grammarly, ProWritingAid, Ginger or any online spelling/grammer checkers to ensure your SOP is error-free."

    motivation_messages = {
        "positive": [
            "Great job! Your statement reflects strong motivation and passion for the field.",
            "Well done! Your enthusiasm and commitment shine through in your statement.",
            "Impressive! Your motivation is evident from your thoughtful statement.",
            "Fantastic! Your dedication and passion align perfectly with the expectations for this opportunity.",
            "Excellent! It's evident from your statement that you possess the enthusiasm and drive.",
        ],
        "neutral": [
            "Your statement contains some relevant keywords, but consider providing more details about your motivation for a more comprehensive overview.",
            "There are elements in your statement that touch on motivation. Consider elaborating further for a stronger emphasis on your drive and enthusiasm.",
            "Your statement has some relevant content, but it could be strengthened by incorporating specific examples of your motivation.",
        ],
        "negative": [
            "I couldn't find specific keywords related to motivation in your statement. Please elaborate on your enthusiasm and passion.",
            "Your statement lacks clear indications of motivation. Consider revisiting and emphasizing your dedication and enthusiasm.",
            "It would be beneficial to include more details about your motivation in your statement.",
            "Your statement is missing keywords related to motivation. Take the opportunity to showcase your enthusiasm and commitment.",
            "Consider revising your statement to include specific examples that highlight your motivation relevant to this opportunity.",
        ],
    }

    experience_messages = {
        "positive": [
            "Great job! Your statement reflects valuable experience and a strong background in the field.",
            "Well done! Your extensive experience and skills is evident from your detailed statement.",
            "Impressive! Your past roles and achievements demonstrate a wealth of experience in the field.",
            "Fantastic! Your professional journey showcases a rich history of success and expertise.",
            "Excellent! It's evident from your statement that you possess the experience and skills required for this program.",
        ],
        "neutral": [
            "Your statement contains some relevant keywords related to experience, but consider providing more specific details for a comprehensive overview.",
            "There are elements in your statement that touch on experience. Consider elaborating further for a stronger emphasis on your professional background.",
            "Your statement has some relevant content related to experience, but it could be strengthened by incorporating specific examples of your past roles and achievements.",
        ],
        "negative": [
            "I couldn't find specific keywords related to experience in your statement. Please elaborate on your professional background and past roles.",
            "Your statement lacks clear indications of experience. Consider revisiting and emphasizing your past roles and achievements in your field.",
            "It would be beneficial to include more details about your experience in your statement.",
            "Your statement is missing keywords related to experience. Take the opportunity to showcase your professional background and expertise.",
            "Consider revising your statement to include specific examples that highlight your experience relevant to this opportunity.",
        ],
    }


# Get a random message from each category
# random_positive_message = random.choice(motivation_messages["positive"])
# random_neutral_message = random.choice(motivation_messages["neutral"])
# random_negative_message = random.choice(motivation_messages["negative"])
