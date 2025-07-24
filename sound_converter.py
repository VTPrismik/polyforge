import subprocess
import shutil
import os
from moviepy import VideoFileClip, AudioFileClip

ffmpeg = "./ffmpeg/bin/ffmpeg.exe"

def convert_to_wav_ffmpeg(input_file, output_file):
    subprocess.run([
        ffmpeg,
        "-y",
        "-i", input_file,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        output_file
    ])

def song_file_conversions(input_file, output_file):
    if input_file.endswith(".wav"):
        shutil.copyfile(input_file, output_file)
    elif input_file.endswith(".mp4"):
        video = VideoFileClip(input_file)
        video.audio.write_audiofile(output_file)
    elif input_file.endswith(("mp3", "mpga")):
        audio = AudioFileClip(input_file)
        audio.write_audiofile(output_file)
    elif input_file.endswith(("flac", "ogg", "aac", "m4a")):
        convert_to_wav_ffmpeg(input_file, output_file)
    else:
        print("Unsupported format.")

def run_audio_converter():
    input_file = input("Enter the path to the input file: ")
    if not os.path.exists(input_file):
        print("File does not exist.")
        return
    
    output_file = input("Enter the output .wav file path: ")
    song_file_conversions(input_file, output_file)
    print(f"Converted {input_file} to {output_file}")
