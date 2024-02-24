import os
import cv2
import librosa
import moviepy.editor as mp

# Path to the folder containing instrument folders
input_folder = r"E:/ET-A/SEM_VIII/Sound_of_Pixels/Dataset/MUSIC_duet_videos"
output_folder_audio = r"E:/ET-A/SEM_VIII/Sound_of_Pixels/data/audio"
output_folder_frames = r"E:/ET-A/SEM_VIII/Sound_of_Pixels/data/frames"

# Function to extract frames from videos
def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the video file
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    # Extract frames at 8fps
    while success:
        cv2.imwrite(os.path.join(output_folder, '{:06d}.jpg'.format(count)), image)  # Save frame as JPEG file
        success, image = vidcap.read()
        count += 1

# Function to extract audio waveforms
def extract_audio(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Extract audio from video
    video = mp.VideoFileClip(video_path)
    audio_path = os.path.join(output_folder, os.path.splitext(os.path.basename(video_path))[0] + ".mp3")
    video.audio.write_audiofile(audio_path, fps=11025)

# Iterate through each instrument folder
for instrument_folder in os.listdir(input_folder):
    instrument_path = os.path.join(input_folder, instrument_folder)
    if os.path.isdir(instrument_path):
        # Iterate through each video file in the instrument folder
        for video_file in os.listdir(instrument_path):
            video_path = os.path.join(instrument_path, video_file)
            if video_path.endswith(".mp4"):
                # Extract frames
                frames_output_folder = os.path.join(output_folder_frames, instrument_folder, os.path.splitext(video_file)[0])
                extract_frames(video_path, frames_output_folder)
                
                # Extract audio
                audio_output_folder = os.path.join(output_folder_audio, instrument_folder)
                extract_audio(video_path, audio_output_folder)
