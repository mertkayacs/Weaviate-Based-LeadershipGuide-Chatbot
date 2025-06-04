
import subprocess
import glob

# Transcribe each audio file with Whisper to .vtt
print("\n Turkish audio to .vtt with whisper")
audio_files = glob.glob("audio_files/*.mp3")
for audio_file in audio_files:
    print(f"Transcribing: {audio_file}")
    cmd_whisper = [
        "whisper",
        audio_file,
        "--language", "Turkish",
        "--task", "transcribe",
        "--output_format", "vtt",
        "--output_dir", "subtitles_folder"
    ]
    subprocess.run(cmd_whisper)

print("\n✅ Generated .vtt for all.")
