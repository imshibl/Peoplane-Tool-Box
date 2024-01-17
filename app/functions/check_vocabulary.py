def check_vocabulary_richness(text, nlp):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    types = set(tokens)
    ttr = len(types) / len(tokens)
    ttr = round(ttr, 2)

    # Determine the vocabulary richness level based on TTR
    if ttr < 0.3:
        level = "Low"
    elif ttr < 0.5:
        level = "Moderate"
    else:
        level = "High"

    # Define explanations and tips for each level
    explanations = {
        "Low": "Low vocabulary richness means the text uses a limited set of words. To improve, try incorporating more diverse terminology and synonyms.",
        "Moderate": "Moderate vocabulary richness suggests a decent variety of words. To enhance, consider using more precise and industry-specific terms.",
        "High": "High vocabulary richness indicates a rich and diverse vocabulary. Ensure clarity and simplicity in your language while maintaining this level.",
    }

    return {
        "vocabulary_richness": ttr,
        "level": level,
        "message": explanations[level],
    }
