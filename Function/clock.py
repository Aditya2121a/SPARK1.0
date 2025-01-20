import datetime
from Head.Mouth import speak
import pyautogui as gui

def what_is_the_time():
    try:
        current_time = datetime.datetime.now().strftime("%I:%M%p")
        speak(f"The time is {current_time}")
    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        speak(error_message)
