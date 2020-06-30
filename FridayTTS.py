import os
import time
import playsound
import speech_recognition as sr
import webbrowser
import subprocess
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text,lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def spot():
    subprocess.Popen(["/usr/bin/spotify"])
def code():
    subprocess.Popen(["/usr/bin/code"])

wake = "hey friday"

while True:
    print("Listening")
    text = get_audio()
    
    if text.count(wake) > 0:
        speak("I am ready")
        text = get_audio()


    if "open netflix" in text:
        chrome_path = "/usr/bin/google-chrome"
        url = "https://www.netflix.com/ph/"
        webbrowser.get(chrome_path).open(url)

    if "open gmail" in text:
        chrome_path = "/usr/bin/google-chrome"
        url = "https://mail.google.com/mail/u/0/"
        webbrowser.get(chrome_path).open(url)

    if "open messenger" in text:
        chrome_path = "/usr/bin/google-chrome"
        url = "https://messenger.com/"
        webbrowser.get(chrome_path).open(url)

    if "open youtube" in text:
        chrome_path = "/usr/bin/google-chrome"
        url = "https://www.youtube.com/"
        webbrowser.get(chrome_path).open(url)

    if "open spotify" in text:
        spot()
        
    if "let's code" in text:
        code()
        
    if "exit" in text:
        exit()