import pyttsx3
import time


def speak(text):
    engine = pyttsx3.init()
    pitch = 150
    rate = 180
    volume = 2
    voice_id = engine.getProperty("voices")

    if voice_id:
        voices = engine.getProperty('voices')
        try:
            engine.setProperty('voice', voices[2].id)
        except IndexError:
            print("Voice id not found. Using the default voice")

    engine.setProperty('rate', rate)  # Speed of speech
    engine.setProperty('volume', volume)  # Volume level (0.0 to 1.0)
    engine.setProperty('pitch', pitch)  # Pitch level (0 to 100)
    engine.say(text)
    engine.runAndWait()


# Speak the text with customized parameters
speak("Hello Sir! This is an advanced speak function in your PowerPoint presentation.")

