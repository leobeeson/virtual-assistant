import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit


google_search_primers = [
    "search google for",
    "search google",
    "search for",
    "search"    
]

wikipedia_search_primers = [
    "wikipedia",
    "search wikipedia",
    "search wikipedia for"
]


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
    
    
def remove_primers_from_command(command: str, primers: list[str]) -> str:
    search_utterance = command
    if len(primers) > 0:
        for primer in primers:
            if primer in search_utterance:
                search_utterance = search_utterance.replace(primer, "ZULUZULUZULU", 1)
                search_utterance = search_utterance.split("ZULUZULUZULU")[1].strip()
                break
    return search_utterance


def run_jarvis():
    command = take_command()
    if command:
        if "play" in command:
            music_utterance = command.replace("play", " ").strip()
            jarvis_talk("playing" + music_utterance)
            print(f"Playing: {music_utterance}")
            pywhatkit.playonyt(music_utterance)
        elif "what time" in command or "what is the time" in command or "whats the time" in command or "what's the time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            jarvis_talk(f"It's {time}")
            print(f"Time: {time}")
        elif "search" in command:
            search_utterance = remove_primers_from_command(command, google_search_primers)
            print(f"Searcing: {search_utterance}")
            pywhatkit.search(search_utterance)


jarvis_intro(intro)
run_jarvis()
