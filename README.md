# Video Transcription with Whisper

This project provides a Python script for automatically transcribing audio from video files using OpenAI's Whisper model. The script converts `.MOV` video files to audio, transcribes them, and saves the transcriptions in Markdown format in a timestamped folder.

## Features

- **Automatic Conversion**: Converts `.MOV` video files to audio files.
- **Transcription**: Utilizes OpenAI's Whisper model for accurate speech-to-text transcription.
- **Markdown Output**: Saves the transcripts in Markdown format, ensuring readability.
- **Batch Processing**: Processes all `.MOV` files within a specified folder.
- **Timestamped Output Folders**: Organizes transcripts in folders named with the current date and time.

## Requirements

To run this script, you need Python 3.7 or higher, and the following packages:

- `moviepy`
- `whisper`
- `tqdm`

Install these packages using pip:

```bash
pip install moviepy whisper tqdm
```

Additionally, [FFmpeg](https://ffmpeg.org/download.html) must be installed on your system as `moviepy` relies on it for video processing.

## Usage

1. Place your `.MOV` video files in a single folder.
2. Update the `folder_path` variable in the script to point to your folder containing the video files.
3. Run the script:

   ```bash
   python transcribe_videos.py
   ```

4. Find the transcribed files in the generated folder within the same directory as the script.

## Script Workflow

1. **Video to Audio Conversion**: Each video file is converted to an audio file.
2. **Transcription**: The audio file is then transcribed using Whisper.
3. **Markdown Formatting**: The transcript is formatted as a Markdown file with each line of the transcript being part of a blockquote.
4. **Output Storage**: The Markdown file is saved in a timestamped folder created in the current working directory.
5. **Clean Up**: Audio files are deleted after transcription to save space.

## Customization

- Modify the `transcribe_audio` function if you need to change the language or model parameters.
- Adjust Markdown formatting in the script according to your preferences.

## Limitations

- The script currently supports `.MOV` files only. You can modify the script to include other video file extensions.
- Whisper does not identify different speakers. It transcribes the speech as continuous text.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](link-to-your-issues-page) if you want to contribute.

## License

Distributed under the MIT License. See `LICENSE` for more information.
