import os
from utils.extract_notes import extract_speaker_notes
from utils.pdf_to_image import pdf_to_images
from utils.pptx_to_images_libreoffice import pptx_to_images_libreoffice
from utils.text_to_speech import text_to_speech_applio
from utils.create_video import create_video, create_video2

PPTX_FILE = 'assets/presentation.pptx'
AUDIO_DIR = 'assets/audio'
SLIDES_DIR = 'assets/slides'
OUTPUT_VIDEO = 'assets/output_video.mp4'

# Make sure directories exist
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(SLIDES_DIR, exist_ok=True)

# Step 1: Extract speaker notes
print("Extracting speaker notes...")
speaker_notes = extract_speaker_notes(PPTX_FILE)

# Step 2: Convert speaker notes to audio
print("Converting speaker notes to audio...")
for i, note in enumerate(speaker_notes):
    print(f"Converting slide {i+1}")

    audio_file = f"{AUDIO_DIR}/slide_{i+1}.mp3"
    print(f"Note {note}")
    if not note is None:
      text_to_speech_applio(note, audio_file)
    print(f"Converted slide {i+1}")

print("Creating slides")
pptx_to_images_libreoffice(PPTX_FILE,SLIDES_DIR)
pdf_to_images("assets/slides/presentation.pdf", "assets/slides")

# Step 3: Generate video from slides and audio
print("Creating video...")
# create_video(PPTX_FILE, OUTPUT_VIDEO, SLIDES_DIR, AUDIO_DIR)
create_video2(OUTPUT_VIDEO,SLIDES_DIR,AUDIO_DIR)
print(f"Video created: {OUTPUT_VIDEO}")
