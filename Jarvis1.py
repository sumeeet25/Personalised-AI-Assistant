import speech_recognition as sr
from gtts import gTTS
import os
import openai
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# Set your OpenAI API key here
openai.api_key = "api_key"

# Memory dictionary to store user information
memory = {
    "name": "Rishi",
    "likes": "Being a Billionaire"
}

# Function for text-to-speech and displaying text output
def speak(text):
    print("AI:", text)
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    os.system("afplay speech.mp3")
    os.remove("speech.mp3")

# Function to greet the user
def greet():
    speak("Hello Rishi! How can I assist you today?")

# Function to open websites or applications using ChromeDriver
def open_website_or_app(command):
    driver = None 
    if "open youtube" in command:
        service = ChromeService(executable_path='/Users/rushikeshdeelippatil/Desktop/AI Jarvis/Database/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.youtube.com")
        speak("Opening YouTube")
        if "search for" in command:
            search_query = command.split("search for")[-1].strip()
            search_input = driver.find_element_by_name("search_query")  # Locate the search input field
            search_input.send_keys(search_query)  # Type the search query
            search_input.submit()  # Submit the search
            speak(f"Searching for {search_query} on YouTube")
    elif "open facebook" in command:
        service = ChromeService(executable_path='/Users/rushikeshdeelippatil/Desktop/AI Jarvis/Database/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.facebook.com")
        speak("Opening Facebook")
    elif "open instagram" in command:
        service = ChromeService(executable_path='/Users/rushikeshdeelippatil/Desktop/AI Jarvis/Database/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.instagram.com")
        speak("Opening Instagram")
    else:
        # Use OpenAI's ChatGPT for handling other user commands
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot."},
                {"role": "user", "content": command}
            ]
        )
        speak(response['choices'][0]['message']['content'])

    if driver:  # Close the browser if driver exists
        time.sleep(20)  # Keep the browser open for a few seconds before closing
        driver.quit()

# Function to listen for user input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("User:", command)
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Sorry, I cannot access Google Speech Recognition service.")
        return ""

# Function to listen for trigger phrase
def listen_for_trigger_phrase():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for trigger phrase...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print("User:", command)
            if "wake up friday" in command:
                greet()
                while True:
                    command = listen()
                    if command:
                        if "exit" in command:
                            speak("Goodbye!")
                            break
                        open_website_or_app(command)
                return  # Exit the function after the conversation ends
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            speak("Sorry, I cannot access Google Speech Recognition service.")
            return

# Start listening for the trigger phrase
listen_for_trigger_phrase()
