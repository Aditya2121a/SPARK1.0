import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Head.Mouth import speak  # Assuming you have a speak function to give voice output
import pyautogui as gui

def get_internet_speed():
    try:

        # Set the path to your ChromeDriver executable
        chrome_options = Options()
        #chrome_options.add_argument("--headless")  #Run in headless mode (no visible browser window)
        chrome_driver_path = r'C:\My Project\SPARK 1.0\Data\drive\chromedriver.exe'

        # Initialize Chrome browser
        service = ChromeService(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the website
        driver.get('https://fast.com/')
        gui.hotkey('win', 'down')
        speak("Checking your Internet speed")

        # Wait for the speed test to complete (adjust the timeout as needed)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, 'speed-value'))
        )

        # Find the element with the speed value
        speed_element = driver.find_element(By.ID, 'speed-value')
        speed_value = speed_element.text
        return speed_value

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        if driver:
            driver.quit()

def check_internet_speed():

    speed_result = get_internet_speed()
    if speed_result is not None:
        speak(f"Sir, your internet speed is: {speed_result} Mbps")
    else:
        speak("Error: Unable to retrieve internet speed.")

# Call the function to check the internet speed

