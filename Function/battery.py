import psutil
import time
import threading
from Head.Mouth import speak
from Data.dlg_data.dlg import *
import random


def battery_alert():
    """Check and alert about low battery or full charge."""
    while True:
        time.sleep(600)  # Sleep for 10 minutes before checking battery status
        battery = psutil.sensors_battery()

        if battery is None:
            print("No battery information available.")
            continue

        percent = int(battery.percent)
        speak(f"Battery percentage: {percent}")  # Debugging line

        if percent < 30:
            rlow = random.choice(low_b)
            speak(rlow)
        elif percent < 10:
            rlast = random.choice(last_low)
            speak(rlast)
        elif percent == 100:
            rfull = random.choice(full_battery)
            speak(rfull)


def battery_percentage():
    """Report current battery percentage."""
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    speak(f"The device is running on {percent}% battery power.")


def check_plugin_status():
    """Monitor and notify when the device is plugged in or out."""
    previous_state = psutil.sensors_battery().power_plugged

    while True:
        battery = psutil.sensors_battery()
        current_state = battery.power_plugged

        if current_state != previous_state:
            if current_state:
                r_plugin = random.choice(plug_in)
                speak(r_plugin)
            else:
                r_plugout = random.choice(plug_out)
                speak(r_plugout)
            previous_state = current_state

        time.sleep(10)  # Check plugin status every 10 seconds


# Run battery alert and plugin status check in parallel
def battery_status():
    alert_thread = threading.Thread(target=battery_alert)
    plugin_thread = threading.Thread(target=check_plugin_status)

    # Start the threads
    alert_thread.daemon = True
    plugin_thread.daemon = True

    alert_thread.start()
    plugin_thread.start()

    # Keep the main program running indefinitely
    while True:
        time.sleep(1)

# Start monitoring for battery and plugin status