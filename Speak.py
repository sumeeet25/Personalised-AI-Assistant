from gtts import gTTS
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def Speak(Text):
    tts = gTTS(text=Text, lang='en')
    tts.save('output.mp3')
    os.system('afplay output.mp3')

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = False
Path = "Database/chromedriver"
driver = webdriver.Chrome(Path, options=chrome_options)
driver.maximize_window()

website = "https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)

# Locate the <select> element
select_element = driver.find_element(By.XPATH, value='//*[@id="sprachwahl"]')  # Assuming that 'sprachwahl' is the ID of the <select>

# Create a Select object using the <select> element
ButtonSelection = Select(select_element)

# Select an option by its visible text
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(Text):
    
    lengthoftext = len(str(Text))

    if lengthoftext == 0:
        pass

    else:
        print("")
        print(f"AI : {Text}.")
        print("")
        Data = str(Text)
        xpathofsec = '//*[@id="voicetext"]'
        driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH, value='//*[@id="voicetext"]').clear()

        if lengthoftext >= 30:
            sleep(4)
        elif lengthoftext > 40:
            sleep(6)
        elif lengthoftext > 55:
            sleep(8)
        elif lengthoftext > 70:
            sleep(10)
        elif lengthoftext > 100:
            sleep(13)
        elif lengthoftext > 120:
            sleep(14)
        else:
            sleep(2)
