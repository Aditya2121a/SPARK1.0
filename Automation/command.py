import time
from Function.temp import temp
from Automation.YouTube import *
from Automation.open import open
from Automation.close import close
from Function.wish import make_wish
from Function.welcome import welcome
from Training_model.model import mind
from Training_model.model2 import get_response
from Head.Ear import listen
import pyautogui as gui
from Function.battery import *
from Function.search_wiki import *
from Function.search_google import search_google
from Function.speed_test import check_internet_speed
from Function.clock import what_is_the_time
from Function.joke import *
from Function.find_my_ip import *


def cmd():
    make_wish()
    while True:
        text = listen()

        if text:
            text = text.lower()

            if "park" in text and "spark" not in text:
                text = text.replace("park", "spark")

            if text in wake_key_word:
                welcome()

            elif text in bye_key_word:
                randm = random.choice(res_bye)
                speak(randm)
                break

            elif text.startswith(("spark", "buddy")):
                text = text.replace("spark", "").strip()
                response = mind(text)
                speak(response)

            elif text.endswith(("spark", "buddy")):
                text = text.replace("spark", "").strip()
                response = mind(text)
                speak(response)

            elif "spark" in text or "park " in text:
                response = get_response(text)
                speak(response)

            elif "search in google" in text or "search on google" in text:
                text = text.replace(" search in google", "")
                text = text.strip()
                search_google(text)

            elif text.endswith(("search in google", "search on google")):
                text = text.replace("search in google", "")
                text = text.replace("search on google", "")
                text = text.strip()
                search_google(text)

            elif "search in youtube" in text or "search on youtube" in text:
                text = text.replace(" search in youtube", "")
                text = text.replace("search on youtube", "")

                text = text.strip()
                youtube_search(text)

            elif text.endswith(("search in youtube", "search on youtube")):
                text = text.replace("search in youtube", "")
                text = text.replace("search on youtube", "")
                text = text.strip()
                youtube_search(text)

            elif "play music on youtube" in text:
                a = random.choice(q)
                speak(a)
                text = listen().lower()
                play_music_on_youtube(text)

            elif text.startswith(("who is", "what is", "who was", "what was")):
                wiki_search(text)

            elif text.startswith(("open", "kholo", "show me")):
                text = text.replace("kholo", "")
                text = text.replace("show me", "")
                text = text.strip()
                open(text)
            elif text in open_input:
                text = text.replace("bin", "")
                text = text.replace("khologe", "")
                text = text.replace("kholo", "")
                open(text)
            elif text in close_input:
                close()

            elif ("check battery life" in text or "battery percentage" in text or
                  "check battery " in text):
                battery_percentage()
            #1
            elif "minimize" in text or "minimise" in text or "minimize this window" in text or "minimise karoge" in text or "minimise the window" in text:
                speak("minimising...")
                gui.hotkey('win', 'down')
            #2
            elif "maximize" in text or "maximize this window" in text or "maximise karoge" in text or "maximise the window" in text:
                speak("maximising...")
                gui.hotkey('win', 'up')
            #3
            elif "write" in text or "likho" in text or "right" in text:
                speak("writing")
                text = text.replace("write", "").replace("likho", "")
                gui.write(text)
            #4
            elif "delete" in text:
                gui.hotkey("delete")
                print("pressed delete")
            #5
            elif "enter" in text or "press enter" in text or "press enter key" in text:
                gui.press("enter")
                print("pressed enter")
            #6
            elif "select all" in text or 'select all paragraph' in text:
                gui.hotkey("ctrl", "a")
                print("selected all")
            #7
            elif "copy" in text or 'copy this' in text:
                gui.hotkey("ctrl", "c")
                print("copy")
            #8
            elif "paste" in text or 'paste here' in text:
                gui.hotkey("ctrl", "v")
                print("paste")
            #9
            elif "undo" in text or 'undo karo' in text:
                gui.hotkey("ctrl", "z")
                print("undo")
            #10
            elif "copy last paragraph" in text:
                gui.hotkey("ctrl", "shift", "c")
                print("copied")
            #11
            elif "increase volume" in text or "volume badhao" in text or "increase sound" in text:
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                print("Volume increased.")
                speak("Volume increased.")
            #12
            elif "decrease volume" in text or "volume kam karo" in text or "decrease sound" in text:
                gui.press("volumedown")
                gui.press("volumedown")
                gui.press("volumedown")
                gui.press("volumedown")
                print("Volume decreased.")
                speak("Volume decreased.")
            #13
            elif "full volume" in text or "full volume kr do" in text:
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                print("now your system in full volume")
                speak("now your system in full volume")
            #14
            elif "mute" in text:
                gui.press("volumemute")
                print("Volume muted.")
            #15
            elif "play" in text or "pause" in text or "stop" in text:
                gui.hotkey("space")
                print("pause")
            #16
            elif text.startswith("search"):
                gui.hotkey("/")
                text = text.replace("search", "")
                gui.write(text)
                speak(f"searching {text}")
                print(f"searching{text}")
                time.sleep(1)
                gui.press("enter")
            #17
            elif "new window" in text or "open new window" in text:
                speak("Opening New Window.")
                gui.hotkey("ctrl", "n")
            #18
            elif "close window" in text:
                speak("Closing Window.")
                gui.hotkey("alt", "f4")
            #19
            elif "restore window" in text:
                speak("Restoring Window.")
                gui.hotkey("win", "shift", "up")
            #20
            elif "switch window" in text or "next window" in text or "next tab" in text or "change tab" in text:
                speak("Switching to Next Window.")
                gui.hotkey("alt", "tab")
            #21
            elif "previous window" in text or "back window" in text:
                speak("Switching to Previous Window.")
                gui.hotkey("alt", "shift", "tab")
            #22
            elif "open incognito" in text or "private window" in text:
                speak("Opening Incognito Window.")
                gui.hotkey("ctrl", "shift", "n")
            #23
            elif "bookmark page" in text or "save page" in text:
                speak("Bookmarking Page")
                gui.hotkey("ctrl", "d")
            #24
            elif "history" in text or "browse history" in text:
                speak("Opening Browsing History.")
                gui.hotkey("ctrl", "h")
            #25
            elif "downloads" in text or "download history" in text:
                speak("Opening Downloads History")
                gui.hotkey("ctrl", "j")
            #26
            elif "inspect element" in text or "open developer tools" in text:
                speak("Opening Developer Tools.")
                gui.hotkey("ctrl", "shift", "i")
            #27
            elif "clear cookies" in text or "delete cookies" in text:
                speak("Clearing Cookies.")
                gui.hotkey("ctrl", "shift", "del")
            #28
            elif "fullscreen" in text or "full screen" in text:
                speak("Entering Fullscreen Mode.")
                gui.hotkey("f11")
            #29
            elif "mute" in text or "mute tab" in text or "mute sound" in text:
                speak("Muting. Tab")
                gui.hotkey("crtl", "m")
            #30
            elif "toggle dark mode" in text or "dark theme" in text:
                speak("Toggling Dark Mode.")
                gui.hotkey("crtl", "shift", "e")
            #40
            elif "unmute" in text or "unmute tab" in text or "unmute sound" in text:
                speak("Unmuting Tab.")
                gui.hotkey("ctrl", "shift", "m")
            #41
            elif "open extensions" in text or "manage extensions" in text:
                speak("Opening Extensions.")
                gui.hotkey("ctrl", "shift", "a")
            #42
            elif "open settings" in text or "browser settings" in text:
                speak("Opening Settings.")
                gui.hotkey("ctrl", ",")
            #43
            elif "save page as" in text or "save as" in text:
                speak("Saving Page As.")
                gui.hotkey("ctrl", "s")
            #44
            elif "print page" in text or "print" in text:
                speak("Printing Page.")
                gui.hotkey("ctrl", "p")
            #45
            elif "open history" in text or "view history" in text:
                speak("Opening History.")
                gui.hotkey("ctrl", "h")
            #46
            elif "clear browsing data" in text or "clear history" in text:
                speak("Clearing Browsing Data.")
                gui.hotkey("ctrl", "shift", "del")
            #47
            elif "open bookmarks" in text or "view bookmarks" in text:
                speak("Opening Bookmarks.")
                gui.hotkey("ctrl", "b")
            #48
            elif "redu" in text:
                gui.hotkey("ctrl", "y")
                print("undo")
            #49
            elif "reload page" in text or "refresh" in text:
                speak("Reloading Page.")
                gui.hotkey("ctrl", "r")
            #50
            elif "go back" in text or "back" in text:
                speak("Going Back.")
                gui.hotkey("alt", "left")
            #51
            elif "go forward" in text or "forward" in text:
                speak("Going Forward.")
                gui.hotkey("alt", "right")
            #52
            elif "stop loading" in text or "stop" in text:
                speak("Stopping Page Load.")
                gui.hotkey("esc")
            #53
            elif "scroll up" in text or "scroll page up" in text:
                speak("Scrolling up.")
                gui.scroll(100)
            #54
            elif "scroll down" in text or "scroll page down" in text:
                speak("Scrolling Down.")
                gui.scroll(-100)
            #55
            elif "scroll to top" in text:
                speak("Scrolling to Top.")
                gui.press("home")
            #56
            elif "scroll to bottom" in text:
                speak("Scrolling to Bottom.")
                gui.press("end")
            #57
            elif "open new tab" in text or "new tab" in text:
                speak("Opening New Tab.")
                gui.hotkey("ctrl", "t")
            #58
            elif "reopen closed tab" in text or "restore closed tab" in text:
                speak("Reopening Closed Tab.")
                gui.hotkey("ctrl", "shift", "t")
            #59
            elif "show desktop" in text or "hide windows" in text:
                speak("Showing Desktop.")
                gui.hotkey("win", "d")
            #60
            elif "open task view" in text or "view tasks" in text:
                speak("Opening Task View.")
                gui.hotkey("win", "tab")

            elif "switch virtual desktop" in text or "change desktop" in text:
                speak("Switching Virtual Desktop.")
                gui.hotkey("ctrl", "win", "right")

            elif "show notification" in text:
                speak("opening notification center")
                gui.hotkey("win", "a")

            elif "lock screen" in text or "lock computer" in text:
                speak("Locking Screen.")
                gui.hotkey("win", "l")

            elif "show action center" in text or "show action menu" in text:
                speak("Showing Action Center.")
                gui.hotkey("win", "a")

            elif "switch user" in text or "change user" in text:
                speak("Switching User.")
                gui.hotkey("win", "l")

            elif "Log off" in text or "sign out" in text:
                speak("Logging off.")
                gui.hotkey("win", "x")
                time.sleep(2)
                gui.hotkey("u", "i")

            elif "shutdown" in text or "turn off computer" in text:
                speak("Shutting Down.")
                gui.hotkey("win", "x")
                time.sleep(2)
                gui.hotkey("u", "u")

            elif "restart" in text or "reboot" in text:
                speak("Restarting.")
                gui.hotkey("win", "x")
                gui.hotkey("u", "r")

            elif "sleep" in text or "put computer to sleep" in text:
                speak("Putting Computer to Sleep")
                gui.hotkey("win", "x")
                time.sleep(2)
                gui.hotkey("u", "s")

            elif "hibernate" in text or "enable hibernation" in text:
                speak("Hibernating.")
                gui.hotkey("alt", "f4")

            elif "check internet speed" in text or "check internet" in text:
                check_internet_speed()

            elif "waqt kya hai" in text or "samay kya hai" in text or "kitne baje hai" in text or "kitna samay hai" in text or "tell me the time" in text or "time" in text:
                what_is_the_time()

            elif "find my ip" in text or "check my ip address" in text or "ip address" in text:
                x = find_my_ip()
                speak(f"sir, your current ip is {x}")

            elif "full screen the video" in text or "full screen tis video" in text:
                gui.hotkey("f")

            elif "check temperature" in text or "check temperature outside" in text or "temperature" in text:
                speak("Which city or state would you like to know the temperature of?")
                temp()

            elif text in qa_dict:
                ans = qa_dict[text]
                speak_thread = threading.Thread(target=speak, args=(ans,))
                speak_thread.start()
                speak_thread.join()
            else:
                pass
        else:
            speak("Please try again.")
