import speech_recognition as sp
import webbrowser
import pyttsx3
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer =sp.Recognizer()
ttsx3=pyttsx3.init()
music={
    "song1":"https://www.youtube.com/watch?v=8cM3j8SAvYg",
    "song2":"https://www.youtube.com/watch?v=DvVaW6bmggE",
    "song3":"https://www.youtube.com/watch?v=hzyEHCbtf1E"

}
newsapi="68de2a052fb54ad48987c0cac303206a"

def aiprocess(command):
    clint = OpenAI(
        api_key="openAi api_key"
    )

    completion = clint.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def speak_old(text):
    ttsx3.say(text)
    ttsx3.runAndWait()

def speak(text):
    tts=gTTS(text)
    tts.save("temp.mp3")
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
        speak("This is google!")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
        speak("This is facebook!")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        speak("This is youtube!")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
        speak("This is linkedin!")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
        speak("This is instagram!")
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link=music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
    # Make a GET request to the NewsAPI
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=pk&apikey={newsapi}")

        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Check if articles are available
            if articles:
                # speak the headlines 
                for article in articles:
                    speak(article["title"]) 
            else:
                speak("No articles found")
    else:
        # let openai handle the request
        try:
            output=aiprocess(c)
            speak(output)
        except Exception as e:
            speak("If you want the answer please purchae the paid version of OpenAi; {0}".format(e))
            print("If you want the answer please purchae the paid version of OpenAi; {0}".format(e))



    


if __name__=="__main__":
    speak("Initializing Jarvis.....! ")
    while True:
        # listen for the wake word "Jarvis"
        # obtain audio from microphone
        
        r=sp.Recognizer()
        

        # recongize speach using sphinx
        try:
            with sp.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word=r.recognize_google(audio)
           
            if(word.lower() == "jarvis"):
                speak("Ya")
            # listen for command
                with sp.Microphone() as source:
                    print("Jarvis Active...!")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    

                    processcommand(command)

        except Exception as e:
            print(" error; {0}".format(e))
