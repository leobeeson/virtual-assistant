import speech_recognition as sr
import pyttsx3
import pywhatkit


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


def take_command():
    command = None
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"Transcribed Command: {command}")
            if "jarvis" in command:
                command = command.replace("jarvis", "").strip()
                return command
    except:
        pass
    
    


def run_jarvis():
    command = take_command()
    if command:
        if "play" in command:
            music_utterance = command.replace("play", " ").strip()
            jarvis_talk("playing" + music_utterance)
            print(f"Playing: {music_utterance}")
            pywhatkit.playonyt(music_utterance)

# jarvis_intro(intro)

run_jarvis()
