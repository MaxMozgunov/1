import webbrowser

import speech_recognition as sr
import os
import sys
import pyttsx3


def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
    # os.system("say " + words)


talk("Hi, how can I help you?")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            task = r.recognize_google(audio, language="en-EN").lower()
            print("Ви проговорили: " + task)
        except sr.UnknownValueError:
            talk("Я вас не зрозумів")
            task = command()
        return task

def make_something(task):
    if "open site" in task:
        talk("Відкриваю")
        url = "https://ituniver.com"
        webbrowser.open(url)


while True:
    make_something(command())
