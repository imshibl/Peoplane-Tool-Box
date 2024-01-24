import string

from .utils import experience_keywords as exp_keys
from .utils import motivation_keywords as moti_keys

# def check_for_experience(text):
#     text = text.lower()
#     text = text.translate(str.maketrans("", "", string.punctuation))

#     total_words = 0
#     # found_keywords = []
#     for word in exp_keys.experience_keywords:
#         if word in text:
#             # found_keywords.append(word)
#             total_words = total_words + 1
#     return {
#         "total_words": total_words,
#         "message1": "Found {} experience keywords.".format(total_words),
#     }


def check_for_experience(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    total_words = sum(1 for word in exp_keys.experience_keywords if word in text)
    return {
        "total_words": total_words,
        "message1": f"Found {total_words} experience keywords.",
    }


# def check_for_motivation(text):
#     text = text.lower()
#     text = text.translate(str.maketrans("", "", string.punctuation))

#     total_words = 0
#     # found_keywords = []
#     for word in moti_keys.motivation_keywords:
#         if word in text:
#             # found_keywords.append(word)
#             total_words = total_words + 1

#     return {
#         "total_words": total_words,
#         "message1": "Found {} motivation keywords.".format(total_words),
#     }


def check_for_motivation(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    motivation_keywords = set(moti_keys.motivation_keywords)
    total_words = sum(1 for word in motivation_keywords if word in text)
    return {
        "total_words": total_words,
        "message1": f"Found {total_words} motivation keywords.",
    }
