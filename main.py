import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('api.env')
api_key = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def aiProcess(command):
    groq_api_key = os.getenv('GROQ_API_KEY')
    
    if not groq_api_key:
        return "Sorry, AI service is not configured properly."
    
    try:
        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )
        
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": command}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Sorry, I couldn't process that request. Error: {str(e)}"

def processCommand(c):
    if "open google" in c.lower():
      webbrowser.open("https://google.com")
    elif "open facebbok" in c.lower():
      webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
    elif "open mysite" in c.lower():
      webbrowser.open("https://bipanneupane.com")
    elif "open x" in c.lower():
      webbrowser.open("https://x.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}")
        if r.status_code == 200:
            
            #parse the json response
            data = r.json()
            
            #Extract the articles
            articles = data.get("articles", [])
            #Speak the headlines
            for article in articles:
                speak(article["title"])
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    #listen for the word "Jarvis"
    #Obtain audio from microphone
  
    while True:
        r = sr.Recognizer()
        #recognize speech using google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout =2, phrase_time_limit=1)
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if(word.lower() =="jarvis"):
                speak("Ya")
                print(word)
                #listen for word
                with sr.Microphone() as source:
                    print("Jarvis Active...")   
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)

            # print(command)
        except Exception as e:
            print("Error; {0}".format(e))