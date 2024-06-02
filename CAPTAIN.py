from email import message
from logging import exception
from pathlib import Path
from xml.dom import minicompat
import bs4
import pyttsx3
import datetime
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys
import pywhatkit
import playsound
import pyaudio
from word2number import w2n


mailIds = { "shubham" : "iamhacker9253@gmail.com"

            } 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",172)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour==0 or hour<12:
        speak("Good morning ")

    elif hour>=12 or hour<=18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak(" i am CAPTAIN sir. please tell me how can i help you")


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said  : {query}\n")
        

    except Exception as e:
        # print(e)
        print("sorry sir i can't recognize ,please speak that again")
        speak("sorry sir i can't recognize ,please speak that again")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shubhamrathod0111@gmail.com','emailpass')
    server.sendmail('shubhamrathod0111@gmai.com', to, content)
    server.close()




if __name__ == "__main__":
    #wishme()
    #while True:
    if 1:
        query = takecommand().lower()
        if 'wikipedia' in query:
            print("searching in wikipedia...")
            speak("searching in wikipedia...")
            query = query.replace("wikipedia","")
            query = query.replace("captain","")
            result = wikipedia.summary(query, sentences = 2)
            speak("according to wilipedia")
            print(result)
            speak(result)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.in")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'open yahoo' in query:
            webbrowser.open("in.mail.yahoo.com")

        elif any(i in query for i in ('stack overflow','stackoverflow','stack over flow')):
            webbrowser.open("stackoverflow.com")
            
        elif any(i in query for i in ('play movies','play movie','play the movie','play the movies')):
            dirc = 'E:\\Movie'
            list = os.listdir(dirc)
            print(list)
            a = random.randint(16,22)
            os.startfile(os.path.join(dirc,list[a]))

        elif any(i in query for i in("the time","current time")):
            currentTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {currentTime}")

        elif any(i in query for i in("open vscode","open vs code","open visual studio code")):
            vscodePath = "C:\\Users\\yagni\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)
            print("VS CODE is Opened")
            speak("VS CODE is Opened")

        elif "open chrome" in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif any(i in query for i in ("open vlc","open vlc player")):
            vlcPath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcPath)
            
        elif any(i in query for i in ("open whatsapp","open whats app")):
            whatsapp_Path = "URL:whatsapp.ex"
            os.startfile(whatsapp_Path)


        elif "email to shubham" in query:
            try:
                speak("what will you want to say")
                #content = takecommand()
                content = "this mail is from jarvis"
                to = mailIds['shubham']
                sendEmail(to,content)
                speak("email has been sent!")

            except Exception as e:
                speak("sorry sir,i am not able to sent your email")
                print(e)

        elif any(i in query for i in("open the photos","open photo","open photos")):
            ptpath = "E:\\PHOTOS"
            os.startfile(ptpath)


        elif any(i in query for i in ("open the cleaner","open c cleaner","open cleaner")):
            clspath = "C:\\Program Files\\CCleaner\\CCleaner64.exe"
            os.startfile(clspath)

        elif any(i in query for i in ("sent message","send message")):
            wphour = datetime.datetime.now().hour
            wpmin = datetime.datetime.now().minute + 2
            print("speak message that you want to sent")
            speak("speak message that you want to sent")
            message = takecommand()
            pywhatkit.sendwhatmsg('+918140153621',message, wphour, wpmin)

        elif any(i in query for i in ("who made program captain","who make you","who write you","who made this program")):
            speak("I made by Mr.Shubham which is a software engineer")
            print("I made by Mr.Shubham which is a software engineer")


        elif any(i in query for i in("who are  you", "what are you","what is you", "what is captain")):
            print("i am CAPTAIN, Mr.Shubham  made this program for desktop assistant, So i can do what you command me")
            speak("i am CAPTAIN, Mr.Shubham made this program for desktop assistant, So i can do what you command me")

        elif any(i in query for i in("google search","in google","google")):
            max_result = 1
            for i in("google search","in google","google","captain"):
                if i in query:
                    query = query.replace(i,"")
            print(query)
            print("Searching in google")
            speak("Searching in google")
            pywhatkit.search(query)
            try:
                result = wikipedia.summary(query, sentences = 3)
                #result = wikipedia.page(query).summary # Thic can be use to search full page summary
                speak("i found something in google : \n")
                print("i found something in google")
                print(result)
                speak(str(result))
                
            except:
                print("No Data Found for Speak")
                speak("No Data Found for Speak")

            
        elif "no thanks" in query:
           speak("thanks for using me sir , have a good day")
           sys.exit()

        elif any(i in query for i in("weather in","weather")):
            print("which city wheather you want to know")
            speak("which city wheather you want to know")
            city = takecommand()
            # city = 'ahmedabad' #comment this when microphone is available
            url = f'https://www.google.com/search?q=weather+in+{city}'
            page = requests.get(url,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}).text
            soup = bs4.BeautifulSoup(page,'html.parser')
            degree = soup.find('span',id ="wob_tm").text
            celsius = soup.find('div',class_="vk_bk wob-unit").find('span',class_="wob_t").text
            wheather = soup.find('span',id ="wob_dc").text
            pywhatkit.search(f"wheather in {city}")
            print(f"Wheather in {city} is {degree} {celsius} {wheather}")
            speak(f"Wheather in {city} is {degree} {celsius} {wheather}")
            # print(degree,celsius,wheather)

        elif any(i in query for i in("set alarm","alarm set")):
            speak("set hour")
            hour = takecommand()
            speak("set minite")
            min = takecommand()
            speak("am or pm")
            shift = takecommand()
                        # hour = 'six'
            # shift = 'pm'
                        # b = {'one': 1,
                        # 'two': 2,
                        # 'three': 3,
                        # 'four': 4,
                        # 'five': 5,
                        # 'six': 6,
                        # 'seven': 7,
                        # 'eight': 8,
                        # 'nine': 9,
                        # 'ten': 10,
                        # 'eleven': 11,
                        # 'twelve': 12}
                        # hour = b[hour]
            
            hour = w2n.word_to_num(hour)
            if shift == 'pm':
                hour +=12
            minute = w2n.word_to_num(min)


            url = 'https://www.pagalworld.pw/iphone-6-remix-ringtone/download.html'
            page = requests.get(url).text
            soup = bs4.BeautifulSoup(page,'html.parser')
            box = soup.select('audio')[0]('source')[0]
            audio = box['src']
            song = requests.get(audio).content
            with open('alarm.mp3','wb') as f:
                f.write(song)
            try:
                while True:
                    if datetime.datetime.now().hour == hour and datetime.datetime.now().minute == minute:
                        print("playing....")
                        playsound.playsound("alarm.mp3")
                        break
                        
                        
            except: 
                print('over...')
        else:
            print("i can not able to do this")
            speak("i can not able to do this")
                





