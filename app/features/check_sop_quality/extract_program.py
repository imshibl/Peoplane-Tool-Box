def extract_education_level_applying_for(sop_text):
    education_level_applying_for = None
    # Define keywords for each educational level
    bachelor_keywords = [
        "bachelor's",
        "undergraduate",
        "bachelors",
        "bachelor",
        "b.sc",
        "bsc",
    ]
    master_keywords = ["master's", "graduate", "masters", "m.sc", "msc", "master"]
    phd_keywords = ["phd", "doctorate", "doctoral", "ph.d", "dphil"]

    # Check for the presence of keywords
    if any(keyword in sop_text.lower() for keyword in phd_keywords):
        education_level_applying_for = "PhD"
    elif any(keyword in sop_text.lower() for keyword in master_keywords):
        education_level_applying_for = "Masters Degree"
    elif any(keyword in sop_text.lower() for keyword in bachelor_keywords):
        education_level_applying_for = "Bachelors Degree"
    else:
        return None  # Educational level not detected

    return education_level_applying_for
