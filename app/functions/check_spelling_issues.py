import re

from spellchecker import SpellChecker

from ..utils import words_to_ignore_list as words_to_ignore
from ..utils.custom_responses import CustomResponses


def checkSpellingIssues(
    sop_text,
    univeristy_name_list,
    people_name_list,
    place_name_list,
    organization_name_list,
):
    spell = SpellChecker(distance=1)

    words_to_ignore_set = set(words_to_ignore.words_to_ignore_on_spell_check)

    words_to_ignore_set.update(univeristy_name_list)
    words_to_ignore_set.update(people_name_list)
    words_to_ignore_set.update(place_name_list)
    words_to_ignore_set.update(organization_name_list)

    pattern = r"[^a-zA-Z0-9\s\']"
    sop_text = re.sub(pattern, " ", sop_text)

    sop_text = sop_text.lower()
    words = sop_text.split()

    mistakes_found = set()

    for word in words:
        # if not any(word_to_ignore_set in word for word_to_ignore_set in words_to_ignore_set):
        if word not in words_to_ignore_set:
            if not spell.correction(word) == word:
                mistakes_found.add(word)

    if len(mistakes_found) > 0:
        mistake_response = {
            "mistakes_found": len(mistakes_found),
            # "mistakes":mistakes_found,
            "message": CustomResponses.spelling_issues_found_response,
        }
    else:
        mistake_response = {
            "mistakes_found": len(mistakes_found),
            "message": CustomResponses.spelling_issues_not_found_response,
        }

    return mistake_response
