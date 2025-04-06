import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
import pygame
import time
from client import ask_jarvis
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapikey = os.getenv("NEWS_API_KEY")

def speak(text):
    engine.say(text)
    engine.runAndWait()

pygame.mixer.init()

def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    # Wait until playback finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def processcommand(command):
    if "open" in command.lower():
        words = command.lower().split()
        try:
            index = words.index("open")
            site = words[index + 1]
            url = f"https://{site}.com"
            webbrowser.open(url)
            speak(f"Opening {site}")
        except IndexError:
            speak("I didn't catch the website name.")
        except Exception as e:
            speak("Something went wrong.")
            print("Error:", e)

    elif command.lower().startswith("play"):
        song = command.lower().split("play", 1)[1].strip()
        try:
            link = music_library.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        except KeyError:
            speak(f"Sorry, I couldn't find the song {song}")

    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapikey}")
        if r.status_code == 200:
            #Parse the JSON response
            data = r.json()
            #Extract the articles
            articles = data.get("articles", [])[:5]  # Limiting to top 5
            if not articles:
                speak("Sorry, I couldn't find any news right now.")
            for i, article in enumerate(articles, start=1): 
                speak(f"News {i}: {article['title']}")
        else:
            print("Failed to fetch news:", r.status_code)
            speak("Failed to fetch news.")

    else:
        #Let OpenAI handle the API request
        output=ask_jarvis(command)
        speak(output)    

      

if __name__ == "__main__":
    play_sound("activation.mp3")
    speak("Initializing Jarvis.....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening ...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio).lower()
            print("Recognized: Jarvis ")

            if "jarvis" in word:
                speak("Yes, how can I help?")

                no_response_count=0
                # Conversation mode loop
                while True:
                    try:
                        with sr.Microphone() as source:
                            print("Jarvis Listening...")
                            audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        command = r.recognize_google(audio).lower()
                        #print("Command:", command)


                        if "stop" in command or "exit" in command or "sleep" in command or "bye" in command:
                            speak("Okay, going back to standby.")
                            play_sound("standby.mp3")
                            break  # Exit inner loop, go back to standby mode

                        processcommand(command)
                        no_response_count = 0  # Reset on successful response

                    except sr.UnknownValueError:
                        no_response_count += 1
                        #print(f"Didn't catch that. Count: {no_response_count}")
                        speak("Sorry, I didn't catch that.")
                    except sr.WaitTimeoutError:
                        no_response_count += 1
                        #print(f"No response detected. Count: {no_response_count}")
                        speak("Are you still there?")

                    if no_response_count >= 5:
                        speak("No response detected. Going back to standby.")
                        play_sound("standby.mp3")
                        break  # Exit inner loop
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            print("Error;", e)
