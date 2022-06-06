import pyttsx3
import os
import datetime
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getproperty("voices")
engine.setProperty("voices", voices[0].id)