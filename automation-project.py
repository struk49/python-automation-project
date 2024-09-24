import pyttsx3
import speech_recognition as speech_recognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    """
    12:00 - noon
    1:00pm - morning / 13:00 - afternoon
    18:00 - evening
    """
    if hour >=0 and hour<=12:
        speak('Good Morning my dear friend')
    elif hour >=12 and hour <=18:
        speak('Good afternoon my dear friend')
    else:
        speak('Good evening my dear friend')
    speak('Let me know how i can help you, What are you looking for ?')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening to you....')
        r.pause_threshold = 1
        audio = r.listen(source)
    

    try:
        print('Reconising your voice...')
        query = r.recognize_google(audio, language='en-in')
        print(f'My dear friend you said : {query}\n')
    
    except Exception as e:
        print('Did not understand, can you repeat your query')
        return None
    

    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    sever.ehlo()
    server,starttls()
    server.login('autominds20@gmail.com', 'maddison8')
    server.sendmail('autominds20@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishme()


    while True:
        query = takecommand().lower()

        if 'Open wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("Wikipedia", "")
            results = Wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia..")
            print(results)
            speak(results)