import subprocess

def merge_ass_subtitles(video_file, subtitle_file, output_file):
    ffmpeg_cmd = f'ffmpeg -i "{video_file}" -vf "ass={subtitle_file}" -c:a copy "{output_file}"'
    subprocess.call(ffmpeg_cmd, shell=True)
