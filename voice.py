from function import text_to_speech
import speech_recognition as sr
import keyboard
import subprocess
subprocess.run("explorer.exe shell:appsFolder\Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App"
               ,shell = True)
text_to_speech("just say start to begin with the voice recording !!")
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
    except:
        print('waiting')
    return  text
def commands():
    text = recognition()
    print(text)
    if "start recording" in text:
        keyboard.press_and_release("ctrl + r")
    elif "stop recording" in text:
        keyboard.press_and_release("space")
    elif "exit" in text:
        keyboard.press_and_release("alt + f4")
        exit()
    else:
        print("waiting !!")
while True:
    commands()