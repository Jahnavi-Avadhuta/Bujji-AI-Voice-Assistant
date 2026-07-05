# ==========================================================
#                Bujji – Intelligent AI Voice Assistant
# ==========================================================

# -----------------------
# Import Required Modules
# -----------------------
import speech_recognition as sr
import random
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
import sys
import psutil
import pyautogui
import subprocess
from datetime import datetime
from openai import OpenAI

# -----------------------
# API Keys
# -----------------------
from dotenv import load_dotenv

import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Create OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)

# -----------------------
# Internet Check
# -----------------------

def isConnected():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

# -----------------------
# Initialize Speech Engine
# -----------------------
engine = pyttsx3.init()

# Optional: Adjust voice speed
engine.setProperty("rate", 170)

# Optional: Set volume (0.0 to 1.0)
engine.setProperty("volume", 1.0)

# Create Recognizer
recognizer = sr.Recognizer()


# ==========================================================
# Text to Speech Function
# ==========================================================
def speak(text):
    """
    Converts text to speech.
    """
    print(f"Bujji : {text}")
    engine.say(text)
    engine.runAndWait()

# ==========================================================
# OpenAI Function
# ==========================================================
def askAI(prompt):
    """
    Sends user query to OpenAI and returns the response.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# ==========================================================
# News Function
# ==========================================================
def getNews():
    """
    Fetches top headlines using NewsAPI.
    """

    if not isConnected():
        speak("Internet connection is unavailable.")
        return

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"

    response = requests.get(url)

    news = response.json()

    articles = news.get("articles", [])

    if not articles:
        speak("Sorry, I couldn't fetch the news.")
        return

    speak("Here are today's top headlines.")

    for article in articles[:5]:
        print(article["title"])
        speak(article["title"])


# ==========================================================
# Command Processing
# ==========================================================
def processCommand(command):

    command = command.lower()

    # ---------------- Website Commands ----------------

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "open chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    # ---------------- Music ----------------

    elif command.startswith("play"):

        song = command.replace("play", "").strip()

        song = song.lower()

        for key in musicLibrary.music:
            if song in key.lower():
                speak(f"Playing {key}")
                webbrowser.open(musicLibrary.music[key])
                return

        speak("Sorry, I couldn't find that song.")

    # ---------------- Time ----------------

    elif "time" in command:

        current = datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current}")

    # ---------------- Date ----------------

    elif "date" in command:

        today = datetime.now().strftime("%d %B %Y")

        speak(f"Today's date is {today}")

    # ---------------- News ----------------

    elif "news" in command:

        getNews()

    # ---------------- Day ----------------

    elif "day" in command:

        day = datetime.now().strftime("%A")

        speak(f"Today is {day}.")

    # ---------------- Battery ----------------

    elif "battery" in command:

        battery = psutil.sensors_battery()

        speak(
            f"The battery percentage is {battery.percent} percent."
        )

    # ---------------- Screenshot ----------------

    elif "take screenshot" in command:

        filename = f"screenshot_{int(time.time())}.png"

        pyautogui.screenshot(filename)

        speak("Screenshot taken successfully.")

    # ---------------- Calculator ----------------

    elif "calculator" in command:

        speak("Opening Calculator")

        subprocess.Popen("calc.exe")

    # ---------------- Notepad ----------------

    elif "notepad" in command:

        speak("Opening Notepad")

        subprocess.Popen("notepad.exe")

    # ---------------- VS Code ----------------

    elif "visual studio code" in command:

        speak("Opening Visual Studio Code")

        subprocess.Popen("code")

    # ---------------- File Explorer ----------------

    elif "file explorer" in command:

        speak("Opening File Explorer")

        subprocess.Popen("explorer")

    # ---------------- Exit ----------------

    elif any(word in command for word in ["exit","stop","quit","goodbye","bye"]):

        goodbye = [
        "Goodbye. Have a wonderful day.",
        "See you soon.",
        "Take care.",
        "Happy to help. Goodbye."
        ]

        speak(random.choice(goodbye))

        sys.exit()

    # ---------------- Google Search ----------------

    elif command.startswith("search google for"):

        query = command.replace("search google for", "").strip()

        speak(f"Searching Google for {query}")

        webbrowser.open(f"https://www.google.com/search?q={query}")

    # ---------------- Youtube Search ----------------

    elif command.startswith("search youtube for"):

        query = command.replace("search youtube for", "").strip()

        speak(f"Searching YouTube for {query}")

        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    # ---------------- Thank You ----------------

    elif "thank" in command:

        speak("You're welcome. Happy to help.")

    # ---------------- Greetings ----------------

    elif any(word in command for word in ["hello", "hi", "hey"]):

        speak("Hello! Hope you're having a great day.")

    # ---------------- Who Are You? ----------------

    elif "who are you" in command:

        speak(
            "I am Bujji, your AI powered personal voice assistant. "
            "I can open websites, play music, read news and answer your questions."
        )

    # ---------------- Who Created You? ----------------

    elif "who created you" in command:

        speak(
            "I was created by Jahnavi as a Python mega project."
        )

    # ---------------- AI ----------------

    else:
        speak("Let me think.")

        try:
            if not isConnected():
                speak("Internet connection is unavailable.")
                return
            answer = askAI(command)
            print("AI:", answer)
            speak(answer)

        except Exception as e:
            print(f"OpenAI Error: {e}")
            speak("Sorry, I can't answer that right now because the AI service is unavailable.")


# ==========================================================
# Main Program
# ==========================================================

if __name__ == "__main__":

    with sr.Microphone() as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=2)

    speak("Hello! I am Bujji, your intelligent personal voice assistant. How can I help you today?")

    while True:

        try:

            # Use microphone
            with sr.Microphone() as source:

                print("\nListening for wake word...")

                # Listen for wake word
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=2
                )

            # Convert speech to text
            wake_word = recognizer.recognize_google(audio)
            del audio
            time.sleep(0.2)

            print("You said :", wake_word)

            # Check wake word
            wake = wake_word.lower()

            if any(word in wake for word in ["bujji", "buji", "booji"]):

                responses = [
                    "Yes?",
                    "I'm listening.",
                    "How can I help you?",
                    "Tell me.",
                    "What can I do for you?"
                ]

                speak(random.choice(responses))

                # Listen for actual command
                with sr.Microphone() as source:

                    print("Bujji is listening...")

                    recognizer.adjust_for_ambient_noise(source, duration=0.5)

                    audio = recognizer.listen(
                        source,
                        timeout=8,
                        phrase_time_limit=6
                    )

                command = recognizer.recognize_google(audio)

                print("Command :", command)
                del audio
                time.sleep(0.2)

                processCommand(command)

        except sr.UnknownValueError:
            print("Couldn't understand.")
            # Don't speak here to avoid unnecessary interruptions.

        except sr.WaitTimeoutError:
            print("Listening timed out.")

        except KeyboardInterrupt:
            print("\nProgram Stopped.")
            break

        except Exception as e:
            print("OpenAI Error :", e)

            if "429" in str(e):
                speak("My AI quota has been exceeded.")

            elif "401" in str(e):
                speak("My API key is invalid.")

            else:
                speak("Sorry, I cannot answer right now.")
