import datetime
import pywhatkit
import speech_recognition as kr
import pyttsx3
import wikipedia
import os
import webbrowser
import pyjokes



listener = kr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with kr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alex():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'bye' in command:
        quit()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who created you' in command:
        talk("i was created by krupa kumar")
    elif 'what is your name 'in command:
        talk('i am alexa 2 point o')
    elif 'who are you'in command:
        talk("i am krupa kumar's personal assistant")
    elif 'whatsapp' in command:
        talk('whatsapp')
        pywhatkit.open_web()
    elif 'visual studio' in command:
        talk("opening visual studio")
        codepath= "C:\\Users\\kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif 'google' in command:
        talk("welcome to google")
        webbrowser.open('https://www.google.com/')
    elif 'github' in command:
        talk("opening github")
        webbrowser.open('https://github.com/krupa950')
    elif 'java point' in command:
        talk("opening javapoint")
        webbrowser.open('https://www.javatpoint.com/')
    elif 'linkedin' in command:
        talk("opening linkedin")
        webbrowser.open('https://www.linkedin.com/feed/')
    elif 'facebook' in command:
        talk("opening facebook")
        webbrowser.open('https://www.linkedin.com/feed/')
    elif 'instagram' in command:
        talk("opening instagram")
        webbrowser.open('https://www.linkedin.com/feed/')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "open music" in command:
        codepath='C:\\Users\\kumar\\Music'
        talk("opening music")
        os.startfile(codepath)
    else:
        talk("please say once again..i can't hear properley ")


while True:
    run_alex()
