from datetime import date
import datetime
import random
from Head.Mouth import speak
from Data.dlg_data.dlg import *
from Function.welcome import welcome

today = date.today()
formatted_date = today.strftime("%d %b %y")
nowx = datetime.datetime.now()


def make_wish():
    #welcome()
    current_hour = nowx.hour
    if 5 <= current_hour < 12:
        gm = random.choice(good_morningdlg)
        speak(gm)
    elif 12 <= current_hour < 17:
        ga = random.choice(good_afternoondlg)
        speak(ga)
    elif 17 <= current_hour < 21:
        ge = random.choice(good_eveningdlg)
        speak(ge)
    else:
        gn = random.choice(good_nightdlg)
        speak(gn)


