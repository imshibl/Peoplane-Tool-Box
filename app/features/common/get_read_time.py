import re

def calculate_reading_time(text, words_per_minute=265):
    # Counting words in the text
    words = re.findall(r'\w+', text)
    num_words = len(words)

    # Calculate reading time
    minutes = num_words / words_per_minute
    if minutes < 1:
        seconds = minutes * 60
        return {"time":"{:.2f}".format(seconds) , "type": "seconds"}
    else:
        return {"time": "{:.2f}".format(minutes), "type": "minutes"}