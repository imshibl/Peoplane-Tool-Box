import os

import requests

API_URL = "https://api-inference.huggingface.co/models/arpanghoshal/EmoRoBERTa"


# headers = {"Authorization": "Bearer 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"}

# USE ON PRODUCTION
headers = {"Authorization": "Bearer " + os.getenv("EmoRoBERTa_API_KEY")}


# Split the SOP into three parts
def split_text(text):
    # Split the text into words
    words = text.split()

    # Calculate the total number of words
    total_words = len(words)

    # Calculate the approximate word count for each part
    part_size = total_words // 3

    # Find the starting and ending indices for the parts
    start_index = 0
    mid_index = part_size
    end_index = 2 * part_size

    # Extract the three parts based on the calculated indices
    part1 = " ".join(words[start_index:mid_index])
    part2 = " ".join(words[mid_index:end_index])
    part3 = " ".join(words[end_index:])

    return part1, part2, part3


def get_emotions(sop):
    starting, middle, ending = split_text(sop)

    emotions_list = []

    try:
        # Get starting part emotion
        get_starting_emotion = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": starting,
            },
        )

        start_emotion = get_starting_emotion.json()[0][0]["label"]

        emotions_list.append(start_emotion)

    except Exception as e:
        print(e)

    try:
        # Get middle part emotion
        get_middle_emotion = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": middle,
            },
        )

        middle_emotion = get_middle_emotion.json()[0][0]["label"]

        emotions_list.append(middle_emotion)

    except Exception as e:
        print(e)

    try:
        # Get ending part emotion
        get_ending_emotion = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": ending,
            },
        )

        end_emotion = get_ending_emotion.json()[0][0]["label"]

        emotions_list.append(end_emotion)

    except Exception as e:
        print(e)

    return emotions_list


emotions_for_SOP = [
    "admiration", "approval", "caring", "curiosity", "excitement", 
    "gratitude", "joy", "optimism", "pride", "relief", "realization", "surprise", "neutral"
]
