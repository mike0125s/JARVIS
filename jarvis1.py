import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib  
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id) 
engine.setProperty('voices', voices[1].id)  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
        speak("I am jervis Sir. Please tell me how may i help you!") 

    elif hour>=12 and hour<18:
        speak("Good afternoon!")
        speak("I am jervis Sir. Please tell me how may i help you!") 

    else:
        speak("Good evening!")

        speak("I am jervis Sir. Please tell me how may i help you!") 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
       # print(e)

        print("Say that again please...")
        return "None" 
    return query    


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() 
    server.startls()
    server.login('manideeptaghosh@gmail.com','mike0125s')
    server.sendemail('manideeptaghosh@gmail.com',to,content)
    server.close()             
if __name__ == "__main__":
    wishMe()
    while True:
       query = takeCommand().lower()
       if 'wikipedia' in query:
           speak('searching wikipedia....')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:
             webbrowser.open("youtube.com") 
       elif 'open google' in query:
                webbrowser.open("google.com") 
       elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")
       elif 'open facebook' in query:
             webbrowser.open("facebook.com") 
       elif 'open instagram' in query:
             webbrowser.open("instagram.com") 
       elif 'open amazon' in query:
             webbrowser.open("amazon.com") 
       elif 'open flipcart' in query:
             webbrowser.open("flipcart.com")
       elif 'open whatsapp' in query:
             whatsapp_dir = 'C:\\Users\\MANIDEEPTA\\AppData\\Local\\WhatsApp'  ## PLease give the own whatsapp directory path ##
             whatsapp = os.listdir(whatsapp_dir)
             print(whatsapp)
             os.startfile(os.path.join(whatsapp_dir,whatsapp[6]))
       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir, The time is {strTime}")
       elif 'email to ujjal' in query:
           try:
               speak("what should i say?")
               content = takeCommand()
               to = "debujjal4@gmail.com"
               sendEmail(to,content)
               speak("email has been sent")
           except Exception as e:
               print(e)
               speak("sorry!unable to send the email")


             
                 
 
