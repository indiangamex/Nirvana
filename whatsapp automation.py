import speech_recognition as sr
import subprocess
from function import text_to_speech
import pyautogui
import keyboard
import time
def recognition():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.....")
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = 7000
            audio = r.listen(source)
        text = r.recognize_google(audio, language='en-in')
        text = text.lower()
        print(text)
    except:
        print("not getting")
        pass
    return text
def commands():
    text = recognition()
    if "open chat room of" in text:
        text = text.replace("open chat room of", "")
        subprocess.run("WhatsApp.lnk",
                       shell=True,
                       cwd="C:\\Users\\ghosh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp")
        text_to_speech("estimated time 5 seconds until program is fully initiated")
        time.sleep(2)
        pyautogui.moveTo(200, 165)
        pyautogui.click()
        time.sleep(1)
        keyboard.write(text)
        time.sleep(1)
        pyautogui.moveTo(200, 400)
        pyautogui.click()
        text_to_speech("opened the chatroom you asked for")
    elif "text" in text:
        text = text.replace("text", "")
        keyboard.write(text)
        keyboard.press_and_release("enter")
        text_to_speech("texted")
    elif "voice call" in text:
        text = text.replace("voice call", "")
        time.sleep(1)
        subprocess.run("WhatsApp.lnk",
                       shell=True,
                       cwd="C:\\Users\\ghosh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp")
        text_to_speech("estimated time 8 seconds until program is fully initiated")
        time.sleep(2)
        pyautogui.moveTo(200, 165)
        pyautogui.click()
        time.sleep(1)
        keyboard.write(text)
        time.sleep(1)
        pyautogui.moveTo(200, 400)
        pyautogui.click()
        time.sleep(1)
        t = time.ctime()
        keyboard.write("voice call done by bot at " + t)
        keyboard.press_and_release("enter")
        while True:
            vc_1 = pyautogui.locateOnScreen("vc_1.png")
            if vc_1 != None:
                pyautogui.click(vc_1)
                print("initiated !")
                text_to_speech("voice call initiated")
                break
            else:
                print("initiating !!!")
                continue
    elif "video call" in text:
        text = text.replace("video call", "")
        subprocess.run("WhatsApp.lnk",
                       shell=True,
                       cwd="C:\\Users\\ghosh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp")
        text_to_speech("estimated time 8 seconds until program is fully initiated")
        time.sleep(3)
        pyautogui.moveTo(200, 165)
        pyautogui.click()
        time.sleep(1)
        keyboard.write(text)
        time.sleep(1)
        pyautogui.moveTo(200, 400)
        pyautogui.click()
        time.sleep(1)
        t = time.ctime()
        keyboard.write("video call done by bot at  " + t)
        keyboard.press_and_release("enter")
        while True:
            vc_1 = pyautogui.locateOnScreen("vc_2.png")
            if vc_1 != None:
                pyautogui.click(vc_1)
                print("initiated !")
                text_to_speech("video call initiated")
                break
            else:
                print("initiating !!!")
                continue
    elif "exit" in text:
        text_to_speech("thanks for using whatsapp automation feature")
        exit()
    else:
        pass
while True:
    commands()
