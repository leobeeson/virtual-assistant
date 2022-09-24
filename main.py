import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

intro = [
    "I am Jarvis",
    "Just A Rather Very Intelligent System",
    "What can I do for you?"
]


def jarvis_talk(speech: str) -> None:
    engine.say(speech)
    engine.runAndWait()


def jarvis_intro(intro: list[str]) -> None:
    for line in intro:
        jarvis_talk(line)


jarvis_intro(intro)


try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
        if "jarvis" in command.lower():
            print(command)
except:
    pass
