# Video Subtitle Processor

This is a command-line Python program that processes video files to generate subtitles using [OpenAI Whisper](https://github.com/openai/whisper). The program transcribes the audio from a video, formats the subtitles, and merges them into the video.

## Features

1. Extracts audio from video files.
2. Transcribes audio using Whisper AI with CUDA support for faster processing.
3. Generates multiple subtitle formats supported by Whisper.
4. Creates a formatted `.ass` subtitle file.
5. Merges the `.ass` subtitles directly into the video file.
6. Outputs a final video with embedded subtitles.

## Requirements

Before running the program, make sure the required Python libraries are installed. A `requirements.txt` file is provided in the project for easy installation:

```bash
pip install -r requirements.txt
```

The program supports CUDA for enhanced performance when available.

## How to Use

### 1. Place the Video File
Place the video file you want to process in the same directory as the program.

### 2. Run the Program
Execute the program from the command line:

```bash
python main.py
```

### 3. Input Required Details
You’ll be prompted to provide the following inputs:
- **Filename**: The name of the video file (without the file extension).
- **File format**: The video file extension (e.g., `mp4`).
- **Task**: Whisper task (e.g., `transcribe`).
- **Language code**: The language code for transcription (e.g., `en` for English).
- **Font path**: Path to the font file used for the subtitles (e.g., `fonts/Roboto-Regular.ttf`).
- **Font size**: Size of the subtitle font (e.g., `40`).
- **Font color code**: Hex color code for the subtitle font (e.g., `00FF00` for green).

### 4. Output
The program creates an `output` folder in the same directory with the following structure:
```
output/
└── <video_filename>/
    └── <video_filename_audio>/
        ├── audio.wav
    ├── audio.json
    ├── audio_formatted.json
    ├── audio.ass
    ├── other_subtitle_files...
```

The final video with embedded subtitles is saved in the root folder as:
```
<video_filename>_output.mp4
```

## Program Workflow

1. **Audio Extraction**: Extracts audio from the video file into a separate folder named `<video_filename_audio>`.
2. **Transcription**: Uses Whisper AI to generate multiple subtitle formats.
3. **Subtitle Formatting**: Formats the Whisper-generated JSON file into a clean `.ass` subtitle file.
4. **Subtitle Merging**: Merges the `.ass` subtitles with the original video to produce a new video file.

## Example

For a video file named `example.mp4`:

1. Place `example.mp4` in the program folder.
2. Run the program and provide the required inputs.
3. The final video with subtitles is generated as `example_output.mp4`.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check out the [issues page](https://github.com/your-repo-link/issues).

