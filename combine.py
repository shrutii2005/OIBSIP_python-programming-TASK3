import pyttsx3
import speech_recognition as sr

r= sr.Recognizer()

with sr.Microphone() as source:
    print("calibrating...")
    r.adjust_for_ambient_noise(source,duration=1)
    print("speak now...")
    audio= r.listen(source)

try:
    text=(r.recognize_google(audio))
except sr.RequestError:
    print("check your internet connection")
except sr.UnknownValueError:
    print("could not understand")

engine = pyttsx3.init()

voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print("you said:"+text)
engine.say(text)

engine.runAndWait()
