import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def speechToText():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)

    try:
        print("Recognizing...")
        data=recognizer.recognize_google(audio)
        print(data)
        return data

    except sr.UnknownValueError:
        print("Sorry not listen")

    
speechToText()

def textToSpeech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate",200)
    engine.say(x)
    engine.runAndWait()


def textToSpeechgirl(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[5].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate",200)
    engine.say(x)
    engine.runAndWait()



if __name__ == "__main__": 
    
    if "hello" in speechToText().lower():
        textToSpeech("hello Bosssss... how can I assist you today")
    # elif "hello ginni" in speechToText().lower():
    #     textToSpeechgirl("hello Bosssss... how can I assist you today")
        while True:
            data1=speechToText().lower()

            if "your name" in data1:
                name = "my name is vansh"
                textToSpeech(name)

            elif "your father name" in data1:
                textToSpeech("my father's name is Durlabh sharma.")

            elif "your mother name" in data1:
                textToSpeech("my mother's name is Seema dixit.")

            elif "years old are you" in data1:
                age="I am",20,"years old"
                textToSpeech(age)

            elif "your age" in data1:
                age="my age is",20
                textToSpeech(age)

            elif "you live" in data1:
                textToSpeech("i am living in hathras")

            elif "talk about you" in data1:
                textToSpeech("ok boss")

            elif "listen vansh" in data1:
                textToSpeech("yes boss")

            elif "listen ginni" in data1:
                textToSpeechgirl("yes boss")

            elif "in girl voice" in data1:
                textToSpeech("ok boss")
                textToSpeechgirl("hello boss.... now, are you happy with my voice")

            elif "now time" in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                textToSpeech(time)

            elif "vansh what is the time now" in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                textToSpeech(time)

            elif "ginni what is the time now" in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                textToSpeechgirl(time)

            elif "system voice of girl" in data1:
                textToSpeechgirl("ginni")

            elif "system voice of boy" in data1:
                textToSpeech("VANSH")

            elif "youtube" in data1:
                textToSpeech("just a second boss")
                webbrowser.open("https://www.youtube.com/watch?v=KUpwupYj_tY")

            elif "chatgpt" in data1:
                textToSpeech("just a second boss")
                webbrowser.open("https://chat.openai.com/?model=text-davinci-002-render-sha")

            elif "chat gpt" in data1:
                textToSpeech("just a second boss")
                webbrowser.open("https://chat.openai.com/?model=text-davinci-002-render-sha")

            elif "joke" in data1:
                joke1=pyjokes.get_joke(language="en",
                category="all")
                print(joke1)
                textToSpeech(joke1)

            elif "exit" in data1:
                print("OK BOSS, HAVE A NICE DAY")
                textToSpeech("OK BOSS, HAVE A NICE DAY")
                break

            # time.sleep(2)
    
    else:
        print("sorry not understand")
        textToSpeech("sorry, i am not helping you anymore,boss")
