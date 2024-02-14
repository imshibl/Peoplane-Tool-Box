import re

from spellchecker import SpellChecker

from .utils import words_to_ignore_list as words_to_ignore
from .utils.custom_responses import CustomResponses


def check_spelling_issues(sop_text, *ignore_lists):
    spell = SpellChecker(distance=1)
    words_to_ignore_set = set(words_to_ignore.words_to_ignore_on_spell_check)

    for ignore_list in ignore_lists:
        words_to_ignore_set.update(ignore_list)

    sop_text = re.sub(r"[^a-zA-Z0-9\s\']", " ", sop_text).lower()
    words = sop_text.split()

    mistakes_found = {
        word
        for word in words
        if word not in words_to_ignore_set and spell.correction(word) != word
    }

    message = (
        CustomResponses.spelling_issues_found_response
        if mistakes_found
        else CustomResponses.spelling_issues_not_found_response
    )

    return {"mistakes_found": len(mistakes_found), "message": message}
