<h1 align="center">AudioScribe</h1>
This project converts audio or video files into text using Python. It supports various formats, extracts audio from videos, converts non-WAV files, and transcribes speech using Google’s API, delivering accurate results with robust error handling and cleanup.

## Execution Guide:
1. Run the following command line in the terminal:
   ```
   pip install pydub SpeechRecognition moviepy numpy
   ```

2. Download FFmpeg from the official site **https://ffmpeg.org/download.html**

3. Enter the path of the file whose transcription you want to see

4. Enter the path where you want to save the `transcription.txt` file

5. Now run the code and it will output its prediction

## Model Prediction:

  Audio Input:
  
  

  Transcription Output:

  `hey buddy how are you`

## Overview:
This script automates the process of converting audio (or video) files into text. It supports multiple file formats, handles errors gracefully, and ensures accurate transcription by leveraging Python libraries.

### **Features**
- **Multi-Format Compatibility**: Supports `.wav`, `.mp3`, `.m4a`, `.ogg`, `.flac`, and `.mp4` (video).
- **Audio Extraction**: Converts MP4 video files to audio and processes them seamlessly.
- **Automated Format Conversion**: Converts non-WAV files into WAV format for compatibility with the transcription engine.
- **Accurate Transcription**: Uses Google’s Speech Recognition API for text conversion.
- **Error Handling**: Provides meaningful feedback for unclear audio or API issues.
- **Output Management**: Saves the transcription to a specified file and cleans up temporary files.

### **Workflow**
1. **Input Validation**:
   - Checks the file format.
   - Converts MP4 to audio (if needed) and ensures compatibility.

2. **Audio Processing**:
   - Converts non-WAV files (like MP3) into WAV format for processing.
   - Utilizes the `pydub` library for audio conversion.

3. **Speech-to-Text Conversion**:
   - Loads the WAV file using the `speech_recognition` library.
   - Transcribes the audio to text using Google’s API.

4. **Error Handling**:
   - Detects unsupported formats.
   - Handles unclear audio and unavailable API gracefully.

5. **Output Generation**:
   - Saves the transcribed text to a file.
   - Deletes temporary WAV files if created during processing.

### **Libraries Used**
- **`os`**: For file path manipulation and extension handling.
- **`pydub`**: For audio format conversion.
- **`speech_recognition`**: For converting speech to text.
- **`moviepy`**: For extracting audio from video files.

### **How It Works**
1. Drop an audio or video file into the designated path.
2. Run the script with the file path and output location.
3. Let the script handle the rest:
   - Converts formats if needed.
   - Extracts audio (from video files).
   - Processes and saves the transcription.

This script is an efficient and reliable solution for converting audio or video into readable text!
