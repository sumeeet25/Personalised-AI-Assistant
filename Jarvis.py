from Brain.AiBrain import ReplyBrain
from Body.Listen import MicExecution
print("Starting Jarvis : Wait for some seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
from Main import MainTaskExecution
print("Starting Jarvis : Wait for few more seconds.")

def MainExecution():
    Speak("Hello Sir!")
    Speak("I'm Jarvis, Ready to assist you sir!")

    while True:
        Data = MicExecution()
        Data = str(Data)
        ValueReturn = MainTaskExecution(Data)
        if ValueReturn == True:
            pass

        Reply = ReplyBrain(Data)
        Speak(Reply)

def ClapDetect():
    query = Tester()
    if query is not None and 'True-Mic' in query:
        print("")
        print("Clap Detected!! >>")
        print("")
        MainExecution()
    
    else:
        pass

ClapDetect()

