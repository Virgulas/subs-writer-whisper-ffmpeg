import torch
import subprocess
from moviepy import VideoFileClip
from helper import make_dir

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def whisper(audio_file, path, language, task):
    model = 'medium'
    command = f'whisper {audio_file} --model {model} --language {language} --task {task} --device {DEVICE} --output_dir {path}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def extract_audio(video_file, path):    
    audio_file = video_file.audio
    audio_path = (make_dir(audio_file.filename, path, '_audio')) + 'audio.wav'
    audio_file.write_audiofile(audio_path)
    return audio_path

def get_transcription(video_path, language='en', task='transcribe'):
    video_file = VideoFileClip(video_path)
    directory = make_dir(video_file.filename)
    audio_file = extract_audio(video_file, directory)
    whisper(audio_file, directory, language, task)
    return directory