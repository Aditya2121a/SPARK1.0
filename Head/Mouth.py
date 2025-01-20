import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as gui

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Automatically manage ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Set an implicit wait
driver.implicitly_wait(10)

# Load the target website
driver.get("https://tts.5e7en.me/")

# Check if the website loaded properly
print("Page title:", driver.title)
print("Current URL:", driver.current_url)


def speak(text):
    try:
        element_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]'))
        )
        element_to_click.click()
        element_to_click.clear()
        element_to_click.send_keys(text)  # Input the text
        print(f"Text entered: {text}")

        # Wait for and click the speak button
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]'))
        )
        button_to_click.click()

        # Wait for the speech to process
        sleep_duration = min(0.2 + len(text) // 15, 15)
        time.sleep(sleep_duration)

        # Clear the input box
        element_to_click.clear()

    except Exception as e:
        print(f"An error occurred: {e}")


