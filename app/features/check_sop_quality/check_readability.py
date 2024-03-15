
from textstat import textstat


def check_readability(text):
    automated_readability_index = textstat.automated_readability_index(text)
    readability_levels = {
        (
            17,
            "Very Advanced",
        ): "Very advanced graduate-level text. Best understood by individuals with a Master/Ph.D. degree.",
        (
            15,
            "Advanced",
        ): "Advanced level text. Best understood by individuals with a Master/Bachelor degree.",
        (
            12,
            "Intermediate",
        ): "Intermediate level text. Easily understood by an average college/high school student.",
        (
            0,
            "Basic",
        ): "Easily understood by an average school student.",
    }
    for threshold, level in readability_levels:
        if automated_readability_index > threshold:
            return {
                "automated_readability_index": automated_readability_index,
                "readability_level": level,
                "message": readability_levels[(threshold, level)],
            }
