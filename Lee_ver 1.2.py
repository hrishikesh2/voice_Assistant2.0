import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
import wikipedia
import pyjokes
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command=None
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'lee' in command:
                command = command.replace('lee', '')
                print(command)
    except:
        pass
    return command


def wishMe():
    hour=datetime.now(tz=None).hour 

    if hour >=0 and hour <12:
        talk('hello,Good Morning')
    elif hour >=12 and hour<18:
        talk('hello,good afternoon')
    else:
        talk('hello,good evening')


def run_lee():

    command = take_command()
    print(command)
    

    if 'hello' in command:
        wishMe()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, sentences=1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        print('I am in a relationship with wifi')
        talk('I am in a relationship with wifi')

    elif 'tell me about you'in command:
        talk("I'm Lee Your assistant, Help you for internet surfing,created by rishi and suyog")

    

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open youtube' in command:
        webbrowser.open('https://www.youtube.com/')

    elif 'open google' in command:
        webbrowser.open('https://www.google.com/')

    elif 'open stack overflow' in command:
        webbrowser.open('https://stackoverflow.com/')

    elif 'open gmail' in command:
        webbrowser.open_new_tab('https://mail.google.com/')

    elif 'news'in command:
        webbrowser.open_new_tab('http://epaper.lokmat.com/1')
        talk("opening news")
        time.sleep(5)

    elif 'cricket'in command:
        webbrowser.open_new_tab('https://www.espncricinfo.com/')
        talk("opening live score")
        time.sleep(5)

    elif 'corona'in command:
        webbrowser.open_new_tab('https://www.worldometers.info/coronavirus/')
        talk("opening corona news")
        time.sleep(5)

    elif 'stop' in command:
        print('good bye')
        talk('good bye')
        exit()
    else:
        talk('Please say the command again.')


while True:
    run_lee()