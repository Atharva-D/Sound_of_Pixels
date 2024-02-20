import os
import json
from pytube import YouTube

# Path to the JSON file
JSON_FILE_PATH = r'E:\ET-A\SEM_VIII\Sound_of_Pixels\Download_Videos\JSON\MUSIC21_solo_videos.json'

# Where to save the downloaded videos
SAVE_PATH = r"E:\ET-A\SEM_VIII\Sound_of_Pixels\Download_Videos\Videos\MUSIC21_solo_videos"

# Function to download a single video
def download_video(video_id, save_path, instrument):
    try:
        yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        stream = yt.streams.first()
        instrument_path = os.path.join(save_path, instrument)
        os.makedirs(instrument_path, exist_ok=True)
        stream.download(instrument_path)
        print(f"Downloaded: {video_id}")
    except Exception as e:
        print(f"Error downloading {video_id}: {e}")

# Load the JSON data
with open(JSON_FILE_PATH) as f:
    data = json.load(f)

# Iterate through each instrument type and download its videos
for instrument, videos in data['videos'].items():
    print(f"Downloading videos for {instrument}")
    for video_id in videos:
        download_video(video_id, SAVE_PATH, instrument)
    print(f"Download completed for {instrument}\n")
