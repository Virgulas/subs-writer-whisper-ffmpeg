from audio_transcription import get_transcription
from format_subfile import format_subfile
from ass_converter import convert_json_to_ass
from render_sub import merge_ass_subtitles

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input
        print("This field is required. Please provide a valid input.")

filename = get_valid_input("Enter the filename (without extension): ")
file_format = get_valid_input("Enter the file format (e.g., mp4): ")
file_format = '.' + file_format
task = get_valid_input("Enter the task (e.g., 'transcribe'): ")
language = get_valid_input("Enter the language code (e.g., 'en'): ")
font = get_valid_input("Enter the font path (e.g., 'fonts/Roboto-Regular.ttf'): ")
size = int(get_valid_input("Enter the font size (e.g., 40): "))
color = get_valid_input("Enter the font color code (e.g., '00FF00'): ")

def main():
    file = filename + file_format
    dir = get_transcription(file, language, task)
    sub_formatted_path = format_subfile(file, dir + 'audio.json', dir + 'audio_formatted.json', font, size, color)
    ass_path = convert_json_to_ass(file, sub_formatted_path, dir + 'audio.ass')
    merge_ass_subtitles(file, ass_path, f"{filename}_output.mp4")

if __name__ == "__main__":
    main()
