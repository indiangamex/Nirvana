import speech_recognition as sr
from function import *
from datetime import datetime
def wish():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        text_to_speech("good morning")
    elif hour >= 12 and hour < 18:
        text_to_speech("good evening")
    else:
        text_to_speech("hey how can I help you ?")
def recognition():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = 6000
            print("listening.....")
            audio = r.listen(source)
        text = r.recognize_google(audio, language='en-in')
        text = text.lower()
        if "alexa" in text:
            text = text.replace("alexa", "")
            print(text)
    except sr.WaitTimeoutError:
        text_to_speech("you didn't say anything so i am stopping")
    except sr.UnknownValueError:
        text_to_speech("didn't get what you said !")
    except sr.RequestError:
        text_to_speech("Network problem try checking your network connection")
    return text

def commands():
    wish()
    text = recognition()
    print(text)
    if "search" in text:
        text = text.replace("search", "")
        text = text.replace("on google", "")
        google_search(text)
        exit()
    if "what" or "which" or "tell me" in text:
        if "meaning of" in text:
                text = text.replace("what is the meaning of", "")
                word_meaning(text)
        elif "date" in text:
            from datetime import date
            today = date.today()
            date = today.strftime("%B %d, %Y")
            text_to_speech(date)
        elif "day" in text:
            day = datetime.now()
            value = day.strftime("%A")
            text_to_speech(value)

        elif "time" in text:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            text_to_speech(current_time)

        elif "month" in text:
            month = datetime.now()
            value = month.strftime("%B")
            text_to_speech(value)

        elif "year" in text:
            year = datetime.now()
            value = year.strftime("%Y")
            text_to_speech(value)

        elif "international news" in text:
            international_news()

        elif "news" in text:
            national_news()

        elif "my ip" in text:
            ip_q()

        elif "sports news" in text:
            sports_news()

        elif "joke" in text:
            jokes()

    if "open" or "login" or "join" or "initiate" in text:
        if "opera" in text:
            open_opera()

        elif "chrome" in text:
            open_chrome()

        elif "vmware" in text:
            open_vmware()

        elif "voice recorder" in text:
            subprocess.run("python voice.py", shell=True)

        elif "whatsapp automation" in text:
            subprocess.run("WhatsApp.lnk",
                           shell=True,
                           cwd="C:\\Users\\ghosh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp")
            text_to_speech("whatsapp automation initiated elapsed time 10 seconds ")
            subprocess.run("python \"whatsapp automation.py\"", shell=True)

        elif "instagram" in text:
            insta_autologin()

        elif "my class" in text:
            text_to_speech("joining class 10th S on teams")
            class_join()

        elif "maths tuition" in text:
            text_to_speech("joining prateek sir tution on zoom")
            zoom_auto_join("8587659513", "prateeksir")




    if "selfie" in text:
        selfie()
    if "volume" in text:
        text = text.replace("%", "")
        vol = []
        for word in text.split():
            if word.isdigit():
                vol.append(int(word))
        sound_control(vol[0])

    if "show" or "watch" or "series" in text:
        if "movie" in text:
            webbrowser.open("www.soap2day.cx")
            text_to_speech("showing you a video library from where you can watch great movies and web series")
        elif "anime" in text:
            text_to_speech("from here you can watch the anime you wanted to watch")
            webbrowser.open("www.animefox.io")

    if "who is" in text:
        text = text.replace("who is", "")
        wiki(text)
    if "love you" in text:
        text_to_speech("I too love you but unfortunately as a friend")
    if "f*** you" in text:
        text_to_speech("I can understand you are angry")
    if "shut down" in text:
        text_to_speech("shutting down your system in a minute")

    else:
        text_to_speech("")



commands()





