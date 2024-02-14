import random

sop_videos = [
    "https://youtu.be/qhBgvVMvPH8",
    "https://youtu.be/P64R-kW-bgw",
    "https://youtu.be/Vc3CQN0IlGs",
    "https://youtu.be/J5lzS4qBuJg",
    "https://youtu.be/lTb90b3oabs",
    "https://youtu.be/lNSEqM6mtW8",
    "https://youtu.be/-UKROk-jNlU",
    "https://youtu.be/YyHTZhc8jnM",
]


def generate_video_recommendations():
    recommended_videos = []

    # Get 3 random video recommendations
    random_recommendations = random.sample(sop_videos, 3)

    for video_link in random_recommendations:
        recommended_videos.append(video_link)
    return recommended_videos
