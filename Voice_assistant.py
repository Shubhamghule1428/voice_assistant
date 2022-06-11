from time import time
import pyttsx3
import os
import datetime
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getproperty("voices")
engine.setProperty("voices", voices[0].id)


def speak(vakya):
    engine.say(vakya)
    engine.runAndWait()


def greats():
    time = int(datetime.datetime.now().hour)
    if time < 12 and time > 0:
        speak("Every morning is new blessing,  a second chance that life gives you because you’re so worth it. Have a great day ahead. Good morning! sir")

    elif time > 12 and time < 16:
        speak("Good, better, best. Never let it rest. still your good is better and your better is best. Good afternoon sir ")

    elif time < 20 and time > 16:
        speak("GOdd evening! I hope you had a good and productive day. cheer up")

    else:
        speak("good night darling")

    speak("My name is baby, How i can help you my lord")
