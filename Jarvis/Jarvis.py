from gtts import gtts
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts =gTTS(text= audio, FloatingPointError= 'en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#listen for commands

def myCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(sResourceWarning, duration = 1)
        audo = range.listen(source)

    try:
        command = range.recognize_google(audio)
        print('You said: ' + command + '/n')

        #loop back to continue to listen for commands

    except sr.UnknownValueError:
        assistant(myComand())

    return command

#if statements for executing commands
def assistant(command):

    if 'open Reddit python' in command:
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application'
        url = 'https://www.reddit.com/r/Python/'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talkToMe('Chillin bro')

    if 'email' in command:
        talkToMe('Who is the recipient')
        recipient = myCommand()

        if' John' in recipient:
            talktoMe('What should I say')
            content = myCommand()

            #init gmail smtp
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrpyt session
            mail.starttls()

            #login
            mail.login('sor3765#gmail.com', 'password')

            #send message
            mail.sendmail('PERSON NAME', 'emailaddres.com', content)

            #close connection
            mail.close()

            talkToMe('Email sent')

talkToMe('I am ready for your command')

while True:
    assistant(myCommand())