#speech_to_text:
'''
from gtts import gTTS
import speech_recognition as sr

def listent():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking...")
        audio = r.listen(source, phrase_time_limit=10)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said:", data)
        
    except Exception as e:
        print("Error:", e)
listent()
'''

#speech to speech:
'''
from gtts import gTTS
import speech_recognition as sr
import playsound
import uuid

def listent():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking...")
        audio = r.listen(source, phrase_time_limit=10)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said:", data)

        # Convert text to speech
        tts = gTTS(text=data, lang='en')
        filename = str(uuid.uuid4()) + ".mp3"
        tts.save(filename)
        playsound.playsound(filename)
        
    except Exception as e:
        print("Error:", e)

# Run the function
listent()
'''





#translator :
'''
from gtts import gTTS
import speech_recognition as sr
import playsound
import uuid

#pip install googletrans==3.1.0a0
from googletrans import Translator

#speech to text:
def listen():
    r=sr.Recognizer()
    translator=Translator()
    with sr.Microphone() as source:
        print("start talking")
        audio=r.listen(source,phrase_time_limit=20)
    data=""
    try:
        data=r.recognize_google(audio)
        print("you said:",data)
        
#translted text:
        translated = translator.translate(data, src='en', dest='hi').text
        print("Translated text:", translated)

        
#convert text -> speech    
        tts = gTTS(text=translated, lang='hi')
        filename = str(uuid.uuid4()) + ".mp3"
        tts.save(filename)
        playsound.playsound(filename)

        
    except Exception as e:
        print(e)

listen()
'''

#virtual assistance:

from gtts import gTTS
import speech_recognition as sr
import playsound
from time import ctime
import os
import uuid
import smtplib
import webbrowser

#to make sure it listens
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking")
        audio = r.listen(source,phrase_time_limit=5)
    data = ""
    #Exception Handling
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
listen()

#To respond back with audio 
def respond(String):
    print(String)
    tts = gTTS(text = String,lang = 'en-IN')
    tts.save("speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
#respond('Hey codegan how are you')
#Start giving actions
#Virtual Assistant actions
def virtual_assistant(data):
    """give your actions"""

    if "how are you" in data:
        listening = True
        respond("Good and doing well")

    if "time" in data:
        listening =True
        respond(ctime())


    if "open google" in data.casefold():
        listening = True
        url = "https://www.google.com/"
        webbrowser.open(url)
        respond("Success")

    if "locate" in data:
        webbrowser.open('https://www.google.com/maps/search/'+
                        data.replace("locate",""))
        result = "Located"
        respond("Located {}".format(data.replace("locate","")))

    if "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen().lower()
        edict = {'ishwar':'eswar@codegnan.com','Pooja Madam':'pooja@codegnan.com','Pooja':'poojach207@gmail.com'} #give mail ids
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("What should i tell that person?")
        message = listen()
        content = 'Subject :{}\n\n{}'.format(subject,message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)
        #identify the server
        mail.ehlo()
        mail.starttls()
        #login
        mail.login('poojach207@gmail.com','zufihfzafcmjjwdr') #enter mailid and app password make sure you enable less secure app access
        mail.sendmail('poojach207@gmail.com',toaddr,content) #enter your gmail username
        mail.close()
        respond('Email Sent')

    if "stop" in data:
        listening =False
        print("Listening Stopped")
        respond("Okay done take care...")

    try:
        return listening
    except UnboundLocalError:
        print("Timedout")

respond("Hey Codegnan how are you")
listening = True
while listening ==True:
    data = listen()
    listening = virtual_assistant(data)


