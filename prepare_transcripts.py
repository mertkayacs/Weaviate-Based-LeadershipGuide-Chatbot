import os
import json

def clean_vtt(vtt_file):
    text = []
    with open(vtt_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if '-->' in line:
                continue
            if line == '' or line.isdigit():
                continue
            if "Altyazı" in line:
                continue
            text.append(line)
    return ' '.join(text)

#Chunk of 300
def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def process_all_vtt_files(folder_path, output_file):
    all_chunks = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.vtt'):
            print(f"Ongoing {file_name}")
            #vtt to text
            clean_text = clean_vtt(os.path.join(folder_path, file_name))
            #Chunk
            chunks = chunk_text(clean_text)
            #video title without .vtt
            video_title = file_name.replace('.vtt', '')
            #Placeholder
            source_url = "https://www.youtube.com/playlist?list=PLCi3Q_-uGtdlCsFXHLDDHBSLyq4BkQ6gZ"
            
            for chunk in chunks:
                all_chunks.append({
                    "video_title": video_title,
                    "chunk": chunk,
                    "source_url": source_url
                })

    # Save to JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    process_all_vtt_files("subtitles_folder", "turkish_chunks.json")
