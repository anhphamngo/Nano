import speech_recognition as sr
import pyttsx3
from lib.traning import *

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()

# Function to recognize and respond to voice commands
def listen_and_respond():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said: " + command)

        # Define simple commands and responses
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
        else:
            response = "I didn't understand that command."

        print("Response: " + response)
        text_to_speech.say(response)
        text_to_speech.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

# Continuous loop to listen for commands
while True:
    listen_and_respond()