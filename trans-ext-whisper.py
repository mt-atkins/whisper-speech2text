import datetime
import os
import tqdm
from moviepy.editor import VideoFileClip
import whisper

def convert_video_to_audio(video_file, audio_format='wav'):
    video = VideoFileClip(video_file)
    audio_filename = video_file.rsplit('.', 1)[0] + f'.{audio_format}'
    video.audio.write_audiofile(audio_filename)
    return audio_filename

def transcribe_audio(audio_file, language="en"):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file, language=language)
    return result['text']

def process_videos_in_folder(folder_path):
    # Create a folder with the current date and time for the transcripts
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    transcript_folder = f"Transcripts_{current_time}"
    os.makedirs(transcript_folder, exist_ok=True)

    # Get all .MOV files in the specified folder
    video_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith('.mov')]

    for video_file in tqdm.tqdm(video_files, desc="Processing Videos"):
        print(f"Processing {video_file}...")
        audio_file = convert_video_to_audio(video_file)
        
        try:
            transcript = transcribe_audio(audio_file)
        except Exception as e:
            print(f"Error transcribing {video_file}: {e}")
            continue

        # Writing transcript to a Markdown file in the transcript folder
        base_name = os.path.basename(video_file).rsplit('.', 1)[0]
        transcript_file = os.path.join(transcript_folder, base_name + '.md')
        with open(transcript_file, 'w') as file:
            file.write(f"## Transcript for {base_name}\n\n")
            for line in transcript.splitlines():
                file.write(f"> {line}\n\n")

        # Remove the audio file to save space
        os.remove(audio_file)

        print(f"Transcription completed for {video_file}. Output saved to {transcript_file}")

# Path to the folder containing the video files
folder_path = '/Users/morgan/workspace/whisper-vid2txt/videos'  # Replace with your folder path
process_videos_in_folder(folder_path)
