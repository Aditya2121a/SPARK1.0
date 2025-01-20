import difflib
import webbrowser
import random
import pyautogui as ui
import time
from Head.Mouth import speak
from Data.dlg_data.dlg import *


def appopen(text):
    text = text.replace("open", "")
    text = text.strip()
    random_dlg = random.choice(open_dld)
    speak(random_dlg + text)
    ui.press("win")
    time.sleep(0.8)
    ui.write(text)
    time.sleep(0.8)
    ui.press("enter")
    randomsuccess = random.choice(success_open)
    speak(randomsuccess)


def webopen(text):
    website_name_lower = text.lower()

    if website_name_lower in websites:
        random_dlg = random.choice(open_dld)
        speak(random_dlg + text)
        url = websites[website_name_lower]
        webbrowser.open(url)
        randomsuccess = random.choice(success_open)
        speak(randomsuccess)

    else:
        matches = difflib.get_close_matches(website_name_lower, websites.keys(), n=1, cutoff=0.6)
        if matches:
            randomopen2 = random.choice(open_maybe)
            random_dlg = random.choice(open_dld)
            closest_match = matches[0]
            speak(randomopen2 + random_dlg + text)
            url = websites[closest_match]
            webbrowser.open(url)
            randomsuccess = random.choice(success_open)
            speak(randomsuccess)
        else:
            randomsorry = random.choice(sorry_open)
            speak(randomsorry + " for " + text)


def open(text):
    if "website" in text or "site" in text:
        text = text.replace("open", "")
        text = text.replace("website", "")
        text = text.replace("site", "")
        text = text.strip()
        webopen(text)

    elif "app" in text or "application" in text:
        text = text.replace("app", "")
        text = text.replace("application", "")
        text = text.replace("open", "")
        text = text.strip()
        appopen(text)
    else:
        text = text.replace("open", "")
        text = text.strip()
        appopen(text)


