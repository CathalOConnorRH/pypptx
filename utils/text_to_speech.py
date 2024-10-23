from gtts import gTTS
from pydub import AudioSegment
import os
from gradio_client import Client, handle_file

# Retrieve the backend URL from the environment variable
backend_url = os.getenv('BACKEND_URL', 'http://127.0.0.1:5000')

def text_to_speech(text, file_name):
    if text.strip():  # Only proceed if there's actual text
        tts = gTTS(text)
        tts.save(file_name)
        print(f"Saved TTS for {file_name}")
    else:
        # Create a 1-second silent MP3 if there's no text
        silent_audio = AudioSegment.silent(duration=1000)  # 1 second of silence
        silent_audio.export(file_name, format="mp3")
        print(f"Created silent MP3 for {file_name}")

def text_to_speech_applio(text, file_name):
    print(f"{file_name}")
    if text.strip():
        client = Client(f"{backend_url}")
        result = client.predict(
            tts_text=text,
            tts_voice="en-US-BrianNeural",
            tts_rate=0,
            pitch=0,
            filter_radius=3,
            index_rate=0.75,
            volume_envelope=1,
            protect=0.5,
            hop_length=128,
            f0_method="rmvpe",
            output_tts_path="~/assets/audios/tts_output.wav",
            output_rvc_path="~/assets/audios/tts_rvc_output.wav",
            pth_path="logs/SamuelLJackson470v2/SamuelLJackson470v2.pth",
            index_path="logs/SamuelLJackson/added_IVF1860_Flat_nprobe_1_SamuelLJackson_v2.index",
            split_audio=False,
            f0_autotune=False,
            clean_audio=True,
            clean_strength=0.5,
            export_format="MP3",
            upscale_audio=False,
            f0_file=handle_file('https://github.com/gradio-app/gradio/raw/main/test/test_files/sample_file.pdf'),
            embedder_model="contentvec",
            embedder_model_custom=None,
            api_name="/run_tts_script"
        )
        print(f"Saved TTS for {file_name}")
        os.replace("~/assets/audios/tts_rvc_output.wav", f"{file_name}")

    else:
        # Create a 1-second silent MP3 if there's no text
        silent_audio = AudioSegment.silent(duration=1000)  # 1 second of silence
        silent_audio.export(file_name, format="mp3")
        print(f"Created silent MP3 for {file_name}")