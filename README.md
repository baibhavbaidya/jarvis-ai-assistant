# 🤖 Jarvis - Your Personal A.I. Voice Assistant

Jarvis is a smart voice assistant built with Python that listens to your voice commands and performs tasks just like Alexa or Google Assistant — but cooler because **you built it**.

---

## 🚀 Features

- 🎤 **Voice Activated** – Just say "Jarvis" to get its attention
- 🌐 **Web Automation** – Say "Open YouTube", "Open GitHub", etc.
- 🎵 **Play Music** – Built-in YouTube music links. Try saying “Play Perfect”
- 📰 **News Reader** – Gets live news using the News API
- 🧠 **ChatGPT-Powered Conversations** – For anything else, Jarvis responds intelligently using the **OpenAI API**, delivering fast, context-aware, and highly natural conversations
- 🔊 **Sound Effects** – Cool MP3 sounds for activation and standby
- ⚠️ **Timeout Handling** – Automatically goes to standby if you're inactive

---

## 📁 Project Structure

```
project-jarvis/
│
├── .env.example           # Sample .env file for API keys
├── activation.mp3         # Sound when Jarvis activates
├── standby.mp3            # Sound when going to sleep
├── main.py                # Main Jarvis logic
├── client.py              # Handles OpenAI API requests
├── music_library.py       # Song-to-link mapping
├── requirements.txt       # Python dependencies
├── README.md              # You're reading this!
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/baibhav-baidya/jarvis-ai-assistant.git
cd jarvis-ai-assistant
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure your environment variables**

Create a `.env` file based on the `.env.example` file:
```
OPENAI_API_KEY=your_openai_key
NEWS_API_KEY=your_newsapi_key
```

5. **Run Jarvis**
```bash
python main.py
```

Now speak “Jarvis” and give it commands like:

- "Open YouTube"
- "Play Shape of You"
- "Tell me the news"
- "What is the capital of Japan?"
- "Bye" or "Stop" to send it to standby

---

## 📦 Dependencies

- `speechrecognition`
- `pyttsx3`
- `pygame`
- `openai`
- `python-dotenv`
- `requests`

---

## 🧠 OpenAI API Integration

One of Jarvis's standout features is its **natural language understanding** powered by the OpenAI API. When you ask a question that doesn't match a pre-programmed command (like playing music or opening a website), Jarvis:

1. Recognizes your voice input using Google Speech Recognition.
2. Sends the query to the OpenAI API.
3. Instantly responds with a clear, intelligent answer.

This gives Jarvis the ability to handle **open-ended questions**, engage in casual conversation, and provide accurate responses that feel truly conversational.

---

## ✨ Cool Extras

- 🎧 Smooth transition sounds (`activation.mp3` & `standby.mp3`)
- ↺ Smart response cycle with up to 5 retries for no voice detected
- 🧠 GPT-3.5 Turbo powered conversations
- 🛠️ Easily extendable: Add more songs, commands, or even control smart devices!

---

## 📌 To Do / Future Features

- Add more dynamic command capabilities (like setting alarms or reminders)
- Integrate with smart home APIs (IoT devices)
- GUI version for non-terminal users
- Offline fallback using local ML model

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

