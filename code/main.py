# Import the required libraries
import os
from pydub import AudioSegment
import speech_recognition as sr
from moviepy.editor import VideoFileClip 

def audio_to_text(audio_file, output_file="transcription.txt"):
    # Check file format compatibility
    file_extension = os.path.splitext(audio_file)[-1].lower()
    
    # Handle MP4 files by extracting audio
    if file_extension == ".mp4":
        video = VideoFileClip(audio_file)
        audio_file = audio_file.replace(".mp4", ".wav")
        video.audio.write_audiofile(audio_file) 
        file_extension = ".wav"  
    
    # Ensure the file is in a compatible format (WAV, MP3, M4A, OGG, FLAC)
    if file_extension not in [".wav", ".mp3", ".m4a", ".ogg", ".flac"]:
        raise ValueError("Unsupported file format. Supported formats: WAV, MP3, M4A, OGG, FLAC")

    # Convert non-WAV files to WAV format
    wav_file = audio_file.replace(file_extension, ".wav")
    if file_extension != ".wav":
        audio = AudioSegment.from_file(audio_file)
        audio.export(wav_file, format="wav")

    # Initialize speech recognizer
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)
        try:
            # Transcribe audio to text
            text = recognizer.recognize_google(audio_data)
            print(f"Output saved to {output_file}")
            # Save transcription to file
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(text)
        except sr.UnknownValueError:
            # Handle unclear audio
            print("Audio not clear enough for transcription.")
            text = "Audio not clear enough for transcription."
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(text)
        except sr.RequestError as e:
            # Handle API errors
            print(f"API unavailable: {e}")
            text = f"API unavailable: {e}"
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(text)

    # Delete temporary WAV file if conversion occurred
    if file_extension != ".wav":
        os.remove(wav_file)

# Enter the path of the audio file and the output file
audio_path = "C:/Users/krish/OneDrive/Desktop/audio.mp3"  
output_path = "C:/Users/krish/OneDrive/Desktop/transcription.txt"  
audio_to_text(audio_path, output_path)