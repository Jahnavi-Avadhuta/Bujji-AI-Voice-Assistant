# 🤖 Bujji – Intelligent AI Voice Assistant

Bujji is an AI-powered voice assistant developed using Python. It responds to voice commands, performs various desktop and web-based tasks, fetches real-time news, answers user queries using OpenAI's GPT model, and automates everyday operations through voice interaction.

This project was developed as a Python Mega Project to demonstrate the integration of Speech Recognition, Text-to-Speech, Artificial Intelligence, Web Automation, and System Utilities.

---

# 📌 Features

### 🎙 Voice Recognition
- Listens for the wake word **"Bujji"**
- Recognizes voice commands using Google's Speech Recognition API
- Automatically adjusts for background noise

### 🔊 Text-to-Speech
- Converts text responses into speech
- Uses **pyttsx3** for offline voice output

### 🤖 AI Assistant
- Answers general questions using OpenAI GPT
- Handles unknown commands intelligently
- Internet availability check before AI requests

### 🌐 Web Automation
Open websites using voice commands:
- Google
- YouTube
- Facebook
- LinkedIn
- GitHub
- ChatGPT

### 🔍 Search Engine Integration
- Search anything on Google
- Search videos on YouTube

### 🎵 Music Player
- Plays songs using predefined links from the music library.

### 📰 Latest News
- Reads top Indian news headlines using NewsAPI.

### 📅 Date & Time
- Announces current date
- Announces current time
- Announces current day

### 💻 Windows Utilities
- Open Calculator
- Open Notepad
- Open Visual Studio Code
- Open File Explorer

### 🔋 System Utilities
- Announces battery percentage
- Captures screenshots

### 💬 Friendly Conversation
- Greetings
- Thank you responses
- Introduces itself
- Tells who created it
- Random wake responses for a natural interaction

### ❌ Exit Command
- Ends the program gracefully using voice commands.

---

# 🛠 Technologies Used

- Python 3.12
- SpeechRecognition
- pyttsx3
- OpenAI API
- NewsAPI
- Requests
- python-dotenv
- PyAutoGUI
- psutil
- Webbrowser
- Subprocess

---

# 📂 Project Structure

```
Bujji/
│
├── main.py
├── musicLibrary.py
├── .env
├── requirements.txt
├── README.md
└── screenshots/
```

---

# ⚙ Installation

## Clone the repository

```bash
git clone https://github.com/yourusername/Bujji-AI-Voice-Assistant.git
```

or simply download the project folder.

---

## Create Virtual Environment

```bash
python -m venv env
```

Activate it.

### Windows

```bash
env\Scripts\activate
```

---

## Install Required Packages

```bash
pip install -r requirements.txt
```

or

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install requests
pip install openai
pip install python-dotenv
pip install pyautogui
pip install psutil
pip install pyaudio
```

---

# 🔑 Environment Variables

Create a file named **.env**

```text
OPENAI_API_KEY=your_openai_api_key
NEWS_API_KEY=your_newsapi_key
```

Never upload your API keys to GitHub.

---

# 🎤 Sample Voice Commands

### Wake Word

```
Bujji
```

---

### Websites

```
Open Google
Open YouTube
Open Facebook
Open LinkedIn
Open GitHub
Open ChatGPT
```

---

### Search

```
Search Google for Python tutorials

Search YouTube for Java Full Stack
```

---

### Music

```
Play Believer

Play Shape of You
```

---

### Utilities

```
What is the time?

What is today's date?

What day is today?

Battery percentage

Take screenshot

Open Calculator

Open Notepad

Open Visual Studio Code

Open File Explorer
```

---

### News

```
Tell me today's news
```

---

### AI Questions

```
Explain Artificial Intelligence.

Who invented Python?

What is Machine Learning?

Tell me a joke.
```

---

### Conversation

```
Hello

Thank you

Who are you?

Who created you?
```

---

### Exit

```
Goodbye

Exit

Stop
```

---

# 📸 Screenshots

Add screenshots of:

- Application startup
- Voice command recognition
- News reading
- Google Search
- Music playback
- AI response
- Screenshot feature

---

# 🚀 Future Enhancements

- Weather Forecast
- Email Automation
- WhatsApp Messaging
- Face Recognition Login
- Home Automation
- Voice Authentication
- Voice Notes
- Calendar Integration
- Reminder System
- Smart Home Device Control

---

# 📖 Learning Outcomes

This project demonstrates:

- Speech Recognition
- Text-to-Speech Conversion
- REST API Integration
- Artificial Intelligence Integration
- Web Automation
- Desktop Automation
- Error Handling
- Environment Variable Management
- Python Modular Programming

---

# 👩‍💻 Developer

**Jahnavi**

B.Tech – Computer Science and Engineering

Python Mega Project

---

# 📄 License

This project is developed for educational purposes.