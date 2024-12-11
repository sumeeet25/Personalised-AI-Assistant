# API Key
fileopen = open("Data/Api.txt", "r")
API = fileopen.read()
fileopen.close()

# Importing
import openai
import speech_recognition as sr
from dotenv import load_dotenv

# Coding
openai.api_key = API
load_dotenv()
completion = openai.Completion()

def listen_and_reply():
    r = sr.Recognizer()
    chat_log = ""

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Stopped listening.")

    try:
        question = r.recognize_google(audio)
        print(f"You: {question}")
        answer = ReplyBrain(question, chat_log)
        print(f"Jarvis: {answer}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
    except sr.RequestError as e:
        print(f"An error occurred: e")

def ReplyBrain(question,chat_log = None):
    FileLog = open("Database/chat_log.txt", "r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nJarvis : '
    response = completion.create(
        model = "text-davinci-002",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
    FileLog = open("Database/chat_log.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer

if __name__ == "__main__":
    while True:
        listen_and_reply()
