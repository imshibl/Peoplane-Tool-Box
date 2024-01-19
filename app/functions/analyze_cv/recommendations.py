import random

resume_videos = [
    "https://youtu.be/y8YH0Qbu5h4",
    "https://youtu.be/J-4Fv8nq1iA",
    "https://youtu.be/yp693O87GmM",
    "https://youtu.be/UeMmCex9uTU",
    "https://youtu.be/dQ7Q8ZdnuN0",
    "https://youtu.be/HQqqQx5BCFY",
    "https://youtu.be/CLUsplI4xMU",
    "https://youtu.be/pbczsLkv7Cc",
    "https://youtu.be/ihdyy8RT_b0",
    "https://youtu.be/NRTs4HsICI8",
    "https://youtu.be/Tt08KmFfIYQ",
]


def generate_video_recommendations():
    recommended_videos = []

    # Get 3 random video recommendations
    random_recommendations = random.sample(resume_videos, 3)

    for video_link in random_recommendations:
        recommended_videos.append(video_link)
    return recommended_videos
