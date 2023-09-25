import pyttsx3
import speech_recognition as sr
from lib.traning import *
from os import system
import random

# Initialize the text-to-speech engine
text_to_speech = pyttsx3.init()

# Initialize the recognizer
recognizer = sr.Recognizer()

# Set the wake word
WAKE_WORD = "nano"

def listen_for_wake_word():
    with sr.Microphone() as source:
        print(waiting[random.randint(0, len(waiting)-1)])
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        wake_word = recognizer.recognize_google(audio).lower()
        print("Detected: " + wake_word)

        if WAKE_WORD in wake_word:
            print("I'm here, how may I help you?")
            text_to_speech.say("I'm here, how may I help you?")
            text_to_speech.runAndWait()
            return True

    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

    return False

def respond_to_command():
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said: " + command)

        if "hello" in command:
            response = "Hello! How can I help you?"
        elif "what's the time" in command:
            import datetime
            time = datetime.datetime.now().strftime("%I:%M %p")
            response = f"The current time is {time}"
        elif "goodbye" in command:
            response = "Goodbye! Have a great day!"
        elif code[0] in command or code[1] in command or code[2] in command:
            response = "Ok, opening Visual Code for you!"
            system('start "" "C:\\Users\\AnhPham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\\"')
        else:
            response = "I didn't understand that."

        print("Response: " + response)
        text_to_speech.say(response)
        text_to_speech.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    while True:
        if listen_for_wake_word():
            respond_to_command()
