import atexit
from operator import mod
import profile
import datetime
from sqlite3 import Time
import sys
from typing import Final, final
from unittest import result
from winreg import QueryInfoKey
from winsound import PlaySound
import instaloader
import pyttsx3
import subprocess
from tkinter.ttk import Progressbar
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import ctypes
import time
import requests
import shutil
import requests
from bs4 import BeautifulSoup
from click import command
import os.path
from requests import get, request
import requests
import time
import pyjokes
import requests
import smtplib
import cv2
import random
import pyautogui
import instaloader
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUiType
from GoneUi import Ui_GoneUi
import pywhatkit as kit
import subprocess as sp
import wikipedia as googleScrap
import pywhatkit
 



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("G1")
	speak("I am your Assistant")
	speak(assname)

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('194530316073@asoit.edu.in', 'raj_vraj')
    server.sendmail('your email id', to, content)
    server.close()

def play_on_youtube(video):
    kit.playonyt(video)

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def news():
	main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bc6b5f7a1bb949e5af655d4df8ef0d84"
	main_page = requests.get(main_url).json()
	articles = main_page["articles"]
	head = []
	day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
	for ar in articles:
		head.append(ar["title"])
	for i in range(len(day)):
		speak(f"today's {(day[i])} news is:{head[i]}")

def Date():
    date= datetime.datetime.now()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExecution() 

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout=5,phrase_time_limit=5)
            
        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language ='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"
        return self.query.lower()




    def TaskExecution(self):
        wishMe()
        while True:
            self.query= self.takeCommand().lower ()

            if "open notepad" in self.query:
                npath ="C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open command prompt" in self.query:
                os. system("start cmd")

            elif "play music" in self.query:
                music_dir="music"
                songs=os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
            
            elif 'youtube' in self.query:
                speak('what do you play on youtube , sir?')
                video = self.takeCommand().lower ()
                play_on_youtube(self.query)
		

            elif "ip address" in self.query:
                ip=get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak ("searching wikipedia....")
                self.query=self.query .replace("wikipedia","")
                results = wikipedia.summary (self.query, sentences=2) 
                speak ("according to wikipedia")
                speak (results)
                print(results)

            elif "youtube search" in self.query:
                speak("OK sIR , This Is What I found For Your Search!")
                self.query = self.query.replace("G-1","")
                self.query = self.query.replace("youtube search","")
                self.query = self.query.replace("search youtube","")
                web = 'https://www.youtube.com/results?search_query=' + self.query
                webbrowser.open(web)
                speak("Done sir!")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm =self.takeCommand().lower()
                webbrowser.open(f"{cm}")
                speak("This is what i found on the web")

            elif "search on google" in self.query:
                self.query = self.query.replace("Gone","")
                self.query = self.query.replace("search on google","")
                self.query = self.query.replace("Google","")
                speak("This is what i found on the web")
                pywhatkit.search(self.query)

                try:
                    result = googleScrap.summary(self.query,2)
                    speak(result)
                except:
                    speak("No speakahle data avalable")

            elif "send email" in self.query:
                try:
                    speak("what should i say?")
                    content=self.takeCommand().lower()
                    to="vrajypatel2003@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent ")

                except Exception as e:
                    print(e)
                    speak ("sorry sir,iam not able to sent this email to vraj")

            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os. system("taskkill /f /im notepad.exe")

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")

            elif "news" in self.query:
                speak("wait sir")
                news()

            elif "where i am" in self.query or "where we are" in self.query:
                speak ("wait sir, let me check")
                try:
                    ipAdd=requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url='https:///get.geojs.io/v1/ip/geo/'+ipAdd+'.json'    
                    geo_requests = requests.get(url) 
                    geo_data = geo_requests.json()
                    City = geo_data['City']
                    Country = geo_data['Country']
                    speak(f"sir i am not sure, but i think we are in {City} city of {Country} country")
                except Exception as e:
                    speak ("sorry sir, Due to network issueiam not able to find where we are.")
                    pass
                
            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name=input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}") 
                speak (f"Sir here is the profile of the user {name}")
                speak("sir would you like to download profile picture of this account.")
                condition=self.takeCommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name,profile_pic_only=True)
                    speak ("i am done sir, profile picture is saved in our main folder. nowiam ready")

        
            elif "take screenshot" in self.query or "take a screenshort" in self.query:
                speak ("sir, please tell me the name for this screenshot file")
                name=self.takeCommand().lower()
                speak ("please sir hold the screen for few seconds,iam taking screenshot")
                img=pyautogui.screenshot()
                img.save(f"{name}.png")
                speak ("i am done sir, the screenshot is saved in our main folder")

            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir the time is {strTime}")
            
            elif 'date' in self.query:
                strDate = datetime.datetime.now().strftime("%D:%d:%Y")
                speak(f"sir the date and time  is {strDate}")

            elif"how are you" in self.query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")
            
            elif 'fine' in self.query or "good" in self.query:
                speak("It's good to know that your fine")

            elif "temperature" in self.query:
                self.query = self.query.replace("temperature","")
                self.query = self.query.replace("what temperature ","")
                self.query = self.query.replace("what's temperature ","")
                self.query = self.query.replace("today ","")
                self.query = self.query.replace("G-1","")
                search = "temperature in"+self.query
                url = f"https://www.google.com/search?q={search}"
                r  = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div", class_= "BNeawe").text
                speak(f"current{search} is {temp}")


            elif 'open camera' in self.query:
                open_camera()

            elif "who i am" in self.query:
                speak("If you talk then definitely your human.")
            
            elif "why you came to world" in self.query:
                speak("Thanks to vraj patel. further It's a secret")
            
            elif "who are you" in self.query:
                speak("I was created as a Minor project by Mister vraj patel ")

            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()


            elif "alarm" in self.query:
                speak("enter the time !")
                time = input (":Enter the time :")
                while True:
                    Time_Ac = datetime.datetime.now()
                    now =Time_Ac.strftime("%H:%M:%S")

                    if now == time:
                        speak("Time to Wake Up Sir!")
                        speak("Alarm closed!")
                        now>time
                        wishMe()

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())

            elif 'shutdown system' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
            
            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")

            elif "restart" in self.query:
                subprocess.call(["shutdown", "/r"])

            elif "open" in self.query:
                self.query = self.query.replace("open","")
                self.query = self.query.replace("Gone","")
                self.query = self.query.replace("open google","")
                self.query = self.query.replace("open youtube","")
                pyautogui.press("super")
                pyautogui.typewrite(self.query)
                pyautogui.press("enter")
            
            elif "name" in self.query:
                speak(" i am G1")
            

            

startExecution = MainThread()
            
class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_GoneUi() 
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/Vraj Raj/OneDrive/Desktop/gone/Siri.gif") 
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("C:/Users/Vraj Raj/OneDrive/Desktop/gone/Initiate.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString('hh:mm:ss')
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText (label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
Gone = Main()
Gone.show()
atexit(app.exec_())