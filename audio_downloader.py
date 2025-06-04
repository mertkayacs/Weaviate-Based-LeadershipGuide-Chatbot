import os
import subprocess

playlist_url = "https://www.youtube.com/playlist?list=PLCi3Q_-uGtdlCsFXHLDDHBSLyq4BkQ6gZ"

os.makedirs("audio_files", exist_ok=True)
os.makedirs("subtitles_folder", exist_ok=True)

print("\n🎵 Downloading audio for the playlist")
cmd_download_audio = [
    "yt-dlp",
    "-f", "bestaudio",
    "--extract-audio",
    "--audio-format", "mp3",
    "-o", "audio_files/%(title)s.%(ext)s",
    playlist_url
]
subprocess.run(cmd_download_audio)