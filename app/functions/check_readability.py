from textstat import textstat


def check_readability(text):
    #  flesch_reading_ease = textstat.flesch_reading_ease(text)

    #  flesch_kincaid_grade = textstat.flesch_kincaid_grade(text)
    #  gunning_fog = textstat.gunning_fog(text)

    automated_readability_index = textstat.automated_readability_index(text)

    if automated_readability_index > 17:
        readability_level = "Very Advanced"

    elif automated_readability_index >= 15:
        readability_level = "Advanced"

    elif automated_readability_index >= 12:
        readability_level = "Intermediate"

    else:
        readability_level = "Basic"

    explanations = {
        "Very Advanced": "Very advanced graduate-level text. Best understood by individuals with a Master/Ph.D. degree.",
        "Advanced": "Advanced level text. Best understood by individuals with a Master/Bachelor degree.",
        "Intermediate": "Intermediate level text. Easily understood by an average college/high school student.",
        "Basic": "Easily understood by an average school student.",
    }

    return {
        "automated_readability_index": automated_readability_index,
        "readability_level": readability_level,
        "message": explanations[readability_level],
    }
