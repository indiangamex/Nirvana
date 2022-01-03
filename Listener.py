import speech_recognition as sr
from main_beta import commands
def recognition1():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = 8000
            print("listening.....")
            audio = r.listen(source)
        text = r.recognize_google(audio, language='en-in')
        text = text.lower()
        if "alexa" in text:
            print(text)
            commands()
    except:
        pass
while True:
    recognition1()