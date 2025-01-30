from Auth.trainer.recoganize import AuthenticateFace
from Head.Ear import *
from Function.check_online_offline import is_online
from friday.fspeak import fspeak
from Function.random_advice import get_random_advice
from Automation.command import cmd
from Function.battery import *
from Head.Mouth import *
from Function.joke import *


def advice():
    while True:
        x = [500, 520, 580, 400, 300, 800, 700]
        x = random.choice(x)
        time.sleep(x)
        speak("I have some suggestion for you, sir")
        text = listen().lower()
        if "yes tell me" in text or "yes" in text:
            advice = get_random_advice()
            speak(advice)
        else:
            speak("no problem, i think you need some advice so i give")


def joke():
    while True:
        x = [350, 352, 458, 400, 300, 900, 600]
        x = random.choice(x)
        time.sleep(x)
        speak("I have some joke for you, sir")
        text = listen().lower()
        if "yes tell me" in text or "yes" in text:
            advice = get_random_joke()
            speak(advice)
        else:
            speak("No problem, I think you don't need a joke, so I'm not giving one.")


def spark():
    t1 = threading.Thread(target=cmd)
    t2 = threading.Thread(target=advice)
    t3 = threading.Thread(target=battery_alert)
    t4 = threading.Thread(target=check_plugin_status)
    t5 = threading.Thread(target=check_plugin_status)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


def check_spark():
    if is_online():
        spark()
    else:
        x = random.choice(ofline_dlg)
        fspeak(x)


def main(): 
    if AuthenticateFace():
        check_spark()


main()

