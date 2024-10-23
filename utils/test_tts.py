import pyttsx3
from gradio_client import Client, handle_file


def test_tts_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Print available voices
    for voice in voices:
        print(f"Voice ID: {voice.id}, Name: {voice.name}")

    # Set the voice to a known working one (English)
    engine.setProperty('voice', voices[0].id)  # Change this index to try other voices

    engine.say("This is a test of the text-to-speech engine.")
    engine.save_to_file("This is a test of the text-to-speech engine.","test.mp3")
    engine.runAndWait()

def test_applio_tts_engine():
    client = Client("http://127.0.0.1:6969/")
    result = client.predict(
        tts_text="Welcome to an overview of then.",
        tts_voice="en-US-BrianNeural",
        tts_rate=0,
        pitch=0,
        filter_radius=3,
        index_rate=0.75,
        volume_envelope=1,
        protect=0.5,
        hop_length=128,
        f0_method="rmvpe",
        output_tts_path="~/assets/audios/tts_output.mp3",
        output_rvc_path="~/assets/audios/tts_rvc_output.mp3",
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
    print(result)

test_applio_tts_engine()
#ßtest_tts_engine()