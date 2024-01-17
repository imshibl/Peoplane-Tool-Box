import string

from ..utils import experience_keywords as exp_keys
from ..utils import motivation_keywords as moti_keys


def check_for_experience(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    total_words = 0
    # found_keywords = []
    for word in exp_keys.experience_keywords:
        if word in text:
            # found_keywords.append(word)
            total_words = total_words + 1
    return {
        "total_words": total_words,
        "message1": "Found {} experience keywords.".format(total_words),
    }


def check_for_motivation(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    total_words = 0
    # found_keywords = []
    for word in moti_keys.motivation_keywords:
        if word in text:
            # found_keywords.append(word)
            total_words = total_words + 1

    return {
        "total_words": total_words,
        "message1": "Found {} motivation keywords.".format(total_words),
    }


"""

Certainly! If you are creating a keyword checking system for evaluating motivation and past experience, here are some messages you can display based on the presence or absence of certain keywords:

### Positive Messages (When Relevant Keywords Are Present):

###
1. "Great job! Your statement reflects strong motivation and passion for the field."

2. "Well done! Your past experiences clearly demonstrate your commitment and enthusiasm for [specific field]."

3. "Impressive! Your statement highlights a genuine interest in [subject] and a solid background in relevant experiences."

4. "Fantastic! Your motivation and past experiences align perfectly with the expectations for this opportunity."

5. "Excellent! It's evident from your statement that you possess the enthusiasm and skills required for [specific role]."

### Neutral Messages (When Keywords Are Partially Present or Ambiguous):

1. "Your statement contains some relevant keywords, but it would be beneficial to provide more specific details about your motivation and past experiences."

2. "There are elements in your statement that touch on motivation and past experiences. Consider elaborating further for a more comprehensive overview."

3. "Your statement has some relevant content, but it could be strengthened by incorporating specific examples of your motivation and past experiences."

### Negative Messages (When Relevant Keywords Are Missing or Insufficient):

1. "I couldn't find specific keywords related to motivation and past experiences in your statement. Please elaborate on your enthusiasm and provide examples from your past."

2. "Your statement lacks clear indications of motivation and past experiences. Consider revisiting and emphasizing your commitment to [specific field]."

3. "It would be beneficial to include more details about your motivation and relevant experiences in your statement."

4. "Your statement is missing keywords related to motivation and past experiences. Take the opportunity to showcase your enthusiasm and qualifications."

5. "Consider revising your statement to include specific examples that highlight your motivation and past experiences relevant to this opportunity."

These messages aim to provide constructive feedback based on the presence or absence of specific keywords related to motivation and past experiences in the applicant's statement.
"""
