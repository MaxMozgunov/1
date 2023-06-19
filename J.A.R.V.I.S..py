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
