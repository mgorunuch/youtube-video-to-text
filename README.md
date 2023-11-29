# youtube-video-to-text

Welcome to `youtube-video-to-text`! 🎥📝 This tool helps you convert YouTube videos into text by downloading, splitting, converting, and merging audio into a readable text format. Ideal for transcriptions, note-taking, and content repurposing. Let's get started! 🚀

## Installation

### Prerequisites

Before we dive in, you'll need `ffmpeg` to handle audio processing:

- **Mac**: 
  ```bash
  brew install ffmpeg
  ```
- **Linux**:
  ```bash
  sudo apt-get install ffmpeg
  ```

## Usage

Follow these simple steps to transform a YouTube video into text:

### Step 1: Download Video in Audio Format

```bash
make step_1 # Runs python3 1_download_video_audio.py
```

This command downloads the video and saves it as an audio file. 🎵

### Step 2: Split Audio File

```bash
make step_2 # Runs python3 2_split_audio.py
```

Splits the audio file into smaller, manageable pieces. 🔪🔊

### Step 3: Convert Audio to Text

```bash
make step_3 # Runs python3 3_convert_audio.py
```

Converts the audio files into text format. 📜➡️🔡

### Step 4: Merge Text Files

```bash
make step_4 # Runs python3 4_merge_text_files.py
```

Combines the individual text files into a single document. 📄

### Clean Temporary Files

```bash
make clean # Runs rm -f tmp/*
```

Keeps your workspace neat and tidy! 🧹

## Contributing

Your contributions are always welcome! If you have suggestions or want to improve the code, please feel free to create an issue or submit a pull request.

## License

This project is open source and available under the MIT License.

# Happy Transcribing! 🎉

If you find this tool helpful, don't forget to star the repo! ⭐
