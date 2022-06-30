import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 125)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    speak('welcome the the voice assistance.')
    t = int(datetime.datetime.now().hour)
    if 0 <= t < 12:
        speak('GOOD MORNING SIR!')
    elif 12 <= t < 18:
        speak('GOOD AFTERNOON SIR!')
    elif 18 <= t < 24:
        speak('GOOD EVENING SIR!')
    speak('I am Funta. Please tell me what to do?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said : {query}')

    except Exception as e:
        print('Say that again')
        return 'None'
    return query


if __name__ == '__main__':
    WishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        if 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        if 'open google' in query:
            webbrowser.open('www.google.com')

        if 'play music' in query:
            addr = r'C:\Users\vshau\Downloads\Music\KK [Krishnakumar Kunnath] ~ Hits 01'
            music = os.listdir(addr)
            os.startfile(os.path.join(addr, music[random.randint(0, (len(music)-1))]))

        if 'change music' in query:
            addr = r'C:\Users\vshau\Downloads\Music\KK [Krishnakumar Kunnath] ~ Hits 01'
            music = os.listdir(addr)
            os.startfile(os.path.join(addr, music[random.randint(0, (len(music) - 1))]))

        if 'the time' in query:
            h = datetime.datetime.now().hour
            m = datetime.datetime.now().minute
            speak(f'The time is {h} Hours and {m} Minutes')

        if 'open vs code' in query:
            os.startfile(r"C:\Users\vshau\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        if 'open downloads' in query:
            os.startfile(r"C:\Users\vshau\Downloads")

        if 'exit the application' in query:
            exit()
