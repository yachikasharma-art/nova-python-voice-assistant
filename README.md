# 🤖 NOVA Voice Assistant

NOVA is a Python-based voice assistant that can listen to your voice commands and perform tasks like opening websites, playing music, fetching news, and answering unknown queries using AI.

---

## 🚀 Features

* 🎤 Voice recognition using microphone
* 🔊 Text-to-speech response
* 🌐 Open websites (e.g., YouTube, Google)
* 🎵 Play music from predefined library
* 📰 Fetch latest news headlines
* 🤖 AI fallback (handles unknown commands using OpenAI)

---

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* pyttsx3
* Requests
* OpenAI API
* NewsAPI

---

## 📁 Project Structure

```
NOVA-Assistant/
│── main.py
│── sitelib.py
│── musiclib.py
│── requirements.txt
│── README.md
│── .gitignore

└── assets/
     ├── demo.mp4
     └── screenshot.png
```

---

## ⚙️ Setup Instructions

1. Clone the repository
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create a `.env` file in root directory:

```
OPENAI_API_KEY=your_openai_key
NEWS_API_KEY=your_newsapi_key
```

4. Run the project:

```
python main.py
```

---

## 🎯 Usage

1. Run the program
2. Say **"nova"** to activate
3. Give commands like:

   * "open youtube"
   * "play song"
   * "tell me news"
   * Ask any random question (AI will respond)

---

## 📸 Demo

(Add your demo video or screenshot in the `assets/` folder)

---

## ⚠️ Important Notes

* Do NOT upload your `.env` file
* Make sure your microphone is working
* Internet connection is required for AI and news features

---

## 📌 Future Improvements

* Add memory feature
* Improve voice accuracy
* GUI interface (Jarvis style)
* More command integrations

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

Developed by yachika Sharma 🚀
