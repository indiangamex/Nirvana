import subprocess
import wikipedia
import pyautogui
import socket
import time
import pyjokes
import keyboard
import requests, json
import webbrowser
import pyttsx3
from PyDictionary import PyDictionary
from gnewsclient import gnewsclient
import random
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

wel = ["You're welcome", "You're very welcome", "That's all right", "No problem",
       "No worries", "Don't mention it", "It's my pleasure", "My pleasure"]
def text_to_speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
def sound_control(c):
    text_to_speech("volume is set to {} percent".format(c))
    # --- THIS IS FOR THE INITIALIZATION OF THE SOUND MODULE ---
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    scalarVolume = int(c) / 100
    volume.SetMasterVolumeLevelScalar(scalarVolume, None)
def google_search(search):
    text_to_speech("searching it on google")
    webbrowser.open("https://www.google.com/search?q={}".format(search))
    text_to_speech("here goes your result")
def jokes():
    joke = (pyjokes.get_joke())
    text_to_speech(joke)
def welcome_msg():
    no = random.randint(0, 7)
    print(no)
    text_to_speech(wel[no])
#weather country
def weather(country):
    api_key = "15926d7e7795f7af02a75a5a2088281c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = (country)
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        current_temperature = int(current_temperature - 273.5)

        print(current_temperature)
        # print following values

        w = "weather in {} is {} and temperature there is {} degree celcius and humidity is {} percent".format(
            country, weather_description, current_temperature, current_humidity)
        text_to_speech(w)
        print(w)
    else:
        print(" City Not Found ")
        text_to_speech("sorry city you are searching for ")
# weather local
def weather_local():
        api_key = "15926d7e7795f7af02a75a5a2088281c"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "faridabad"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            current_temperature = int(current_temperature - 273.5)

            print(current_temperature)
            # print following values

            w = "weather in faridabad is {} and temperature outside is {} degree celcius and humidity is {} percent".format(
                weather_description, current_temperature, current_humidity)
            text_to_speech(w)
            print(w)
#selfie/pic
def selfie():
    try:
        subprocess.run("start microsoft.windows.camera:", shell=True)
        lines = ["Dude give a badass pose","you look great today","you have got a photogenic face"]
        no = random.randint(0,2)
        print(no)
        text_to_speech(lines[no])
        text_to_speech("taking your shot in three seconds")
        text_to_speech("three")
        time.sleep(1)
        text_to_speech("two")
        time.sleep(1)
        text_to_speech("one")
        keyboard.press_and_release("space")
        keyboard.press_and_release("alt + f4")
    except:
        text_to_speech("sorry encountered a technical issue while reaching the camera")
#news podcast
def news_podcast():
    text_to_speech("playing live news podcast on youtube")
    webbrowser.open('https://www.youtube.com/watch?v=G1tXyOLlTTA')
#news international
def international_news():
    client = gnewsclient.NewsClient(language='english',
                                    location='international',
                                    max_results=5)
    news_list = client.get_news()
    count = 0
    text_to_speech("top headlines of international news")
    for i in range(5):
        s = (news_list[count]["title"])
        text_to_speech(s)
        count += 1
#national news
def national_news():
    client = gnewsclient.NewsClient(language='english',
                                    location='india',
                                    max_results=5)
    news_list = client.get_news()
    count = 0
    text_to_speech("top headlines of national news")
    for i in range(5):
        s = (news_list[count]["title"])
        text_to_speech(s)
        count += 1
#news sports
def sports_news():
    client = gnewsclient.NewsClient(language = 'english',
                                    location = 'india',
                                    topic = "sports",
                                    max_results = 5)
    news_list = client.get_news()
    count = 0
    text_to_speech("top headlines of sports news")
    for i in range(5):
        s = (news_list[count]["title"])
        text_to_speech(s)
        count += 1
#music

#weather


#wikipedia
def wiki(name):
    text_to_speech("give me a moment to find")
    try:
        s = wikipedia.summary(name, sentences=2)
        text_to_speech(s)
        print(s)
    except:
        text_to_speech("sorry could not resolve your query let me search it for you on google")
        webbrowser.open("https://www.google.com/search?q={}".format(name))
        pass
#oxford dictionary
def word_meaning(word):
    try:
        dictionary = PyDictionary()
        meaning = (dictionary.meaning(word))
        meaning = meaning["Noun"][0]
        print(meaning)
        text_to_speech(meaning)
    except:
        print("can't find meaning of it")
        text_to_speech("can't find meaning of it or maybe try asking meaning of single word at a time")



# teams auto joiner
def class_join ():
    subprocess.run("\"Microsoft Teams.lnk\"",
                   shell=True,
                   cwd="C:\\Users\\ghosh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs")

    while True:
        join1 = pyautogui.locateOnScreen("assets\\join1.png")
        if join1 != None:
            pyautogui.click(join1)
            print("clicked join1")
            break
        else:
            print("not clicked join1")
            continue

    while True:
        join2 = pyautogui.locateOnScreen("assets\\s.png")
        if join2 != None:
            pyautogui.click(join2)
            print("clicked join 2")
            break
        else:
            print("not clicked join 2 ")
            continue

#subprocess to auto login instagram
def insta_autologin():
    text_to_speech("logging onto Instagram")
    subprocess.run("python autologin.py", shell=True)
    text_to_speech("logged into your instagram")

#chrome opener
def open_chrome():
    try:
        text_to_speech("opening chrome")
        subprocess.run("start chrome", shell = True)
    except:
        text_to_speech("sorry couldn't open it seems chrome is not on your device")
        text_to_speech("redirecting to the software download page")
        webbrowser.get("https://www.google.com/chrome/")
#opera opener
def open_opera():
    try:
        text_to_speech("opening Opera GX gaming browser")
        subprocess.run("start opera", shell=True)
    except:
        text_to_speech("sorry couldn't open it seems opera is not on your device")
        text_to_speech("redirecting to the software download page")
        webbrowser.get("www.opera.com")
#ip teller
def ip_q():
    name = socket.gethostname()
    ip = socket.gethostbyname(name)
    print("Your device name is {} and device ip is {}".format(name,ip))
    s = "Your device name is {} and device ip is {}".format(name,ip)
    text_to_speech(s)

#vmware opener
def open_vmware():
    try:
        text_to_speech("opening VMware")
        subprocess.run("start vmplayer", shell=True)
    except:
        text_to_speech("failed to load vmware it seems VMware is not on your device")
        text_to_speech("redirecting you to the software download page")
        webbrowser.get("https://www.vmware.com")
#zoom auto joiner
def zoom_auto_join(id, password):
    def zoom_open():
        subprocess.run("\"Zoom.lnk\"",
                       shell=True,
                       cwd="C:\\Users\\ghosh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom")

    time.sleep(5)
    while True:
        join = pyautogui.locateOnScreen("assets\\join.png")
        if join != None:
            pyautogui.click(join)
            print("initiated !")
            time.sleep(1)
            keyboard.write(id)
            break
        else:
            print("initiating !!!")
            continue
    while True:
        video_off = pyautogui.locateOnScreen("assets\\video_off.png")
        if video_off != None:
            pyautogui.click(video_off)
            print("turned of video !")
            break
        else:
            print("not yet turned of video !")
            continue
    while True:
        join_2 = pyautogui.locateOnScreen("assets\\join_2.png")
        if join_2 != None:
            pyautogui.click(join_2)
            time.sleep(3)
            keyboard.write(password)
            keyboard.press_and_release("enter")
            print("we made it to the class room !")
            break
        else:
            print("not clicked")
            continue

if __name__ == "__main__":
    selfie()
    welcome_msg()
    class_join()
    open_vmware()
    zoom_auto_join()
    open_chrome()
    open_opera()
    ip_q()
    insta_autologin()
    word_meaning()
    international_news()
    sports_news()
    national_news()
    sound_control()
