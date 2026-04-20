import speech_recognition as sr
import pyttsx3
import webbrowser
import sitelib
import musiclib
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
NEWS_KEY = os.getenv("NEWS_API_KEY")

if not OPENAI_KEY or not NEWS_KEY:
    raise ValueError("API keys missing, check .env file")
client = OpenAI(api_key=OPENAI_KEY)
API_KEY = NEWS_KEY

def speak(text):
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()  

def ask_ai(text):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Reply in Hinglish (mix Hindi and English): {text}"
    )
    return response.output[0].content[0].text

def processcommand(command):
    if command.startswith('open'):
        site= command.split(' ')[1]
        link= sitelib.sites.get(site)
        if link:
            webbrowser.open(link)
        else:
            speak("Site not found")
    elif command.startswith('play'):
        music = command.split(' ')[1]
        link= musiclib.music.get(music)
        if link:
            webbrowser.open(link)
        else:
            speak("music not found")
    elif 'news' in command:
        try:
            response = requests.get(f"https://newsapi.org/v2/top-headlines?language=en&pageSize=5&apiKey={API_KEY}")
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])
                if not articles:
                    speak("Koi news nahi mili")
                else:
                    for article in articles[:5]:
                        print(article['title'])
                        speak(article['title'])
            else:
                speak("Sorry, news fetch nahi hui")
        except Exception as e:
            speak("News mein error aa gaya")
    else:
        speak("Let me think...")
        ai_reply = ask_ai(command)
        ai_reply = ai_reply[:200]
        print("AI:", ai_reply)
        speak(ai_reply)
if __name__ == '__main__':
    speak('Initializing NOVA')
    while True:
        r = sr.Recognizer()
        r.energy_threshold = 300 
        r.dynamic_energy_threshold = False  
        try:
            with sr.Microphone() as source:
                print("Listening......")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            print("Recognizing......")
            word = r.recognize_google(audio)
            print(f"Heard: {word}")

            if 'nova' in word.lower():
                print(word)
                speak('Yeah')
                
                with sr.Microphone() as source:
                    print("NOVA Activated - Listening for command......")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=4, phrase_time_limit=5)
                    print("Recognizing command......")
                    command = r.recognize_google(audio)
                    command= command.lower()
                    if not command:
                        speak("Please say something")
                    else:
                        print(f"Command: {command}")
                processcommand(command)

        except sr.WaitTimeoutError:
            print("Timeout - kuch suna nahi")
        except sr.UnknownValueError:
            print("Google could not understand audio")
        except sr.RequestError as e:
            print(f"Google error: {e}")