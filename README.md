# 🤖 Project Jarvis - AI Voice Assistant

A sophisticated voice-activated AI assistant built with Python that can perform various tasks through voice commands, including web browsing, music playback, news updates, and intelligent AI conversations.

## ✨ Features

- 🎤 **Voice Recognition** - Responds to "Jarvis" wake word
- 🗣️ **Text-to-Speech** - Speaks responses back to you
- 🌐 **Web Navigation** - Opens websites with voice commands
- 🎵 **Music Control** - Play songs from your music library
- 📰 **News Updates** - Get latest news headlines
- 🧠 **AI Conversations** - Powered by Groq's fast AI models
- 🔒 **Secure** - API keys stored safely in environment files

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Microphone for voice input
- Internet connection
- API keys (see setup section)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "Project Jarvis"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys** (see [API Setup](#-api-setup) section)

5. **Run Jarvis**
   ```bash
   python main.py
   ```

## 🔧 API Setup

### Required API Keys

1. **Groq AI API** (Free)
   - Visit [Groq Console](https://console.groq.com/)
   - Create account and generate API key
   - Copy your API key (starts with `gsk_`)

2. **News API** (Free)
   - Visit [NewsAPI](https://newsapi.org/)
   - Sign up and get your API key

### Configuration

1. **Create `api.env` file** in the project root:
   ```env
   NEWS_API_KEY=your_news_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

2. **Replace placeholder values** with your actual API keys

⚠️ **Important**: Never commit your `api.env` file to Git. It's already included in `.gitignore`.

## 🎯 Usage

### Wake Word
Say **"Jarvis"** to activate the assistant. You'll hear "Ya" as confirmation.

### Voice Commands

#### 🌐 Web Navigation
- *"Open Google"* - Opens Google.com
- *"Open YouTube"* - Opens YouTube.com
- *"Open Facebook"* - Opens Facebook.com
- *"Open X"* - Opens X.com (Twitter)
- *"Open my site"* - Opens bipanneupane.com

#### 🎵 Music Control
- *"Play [song name]"* - Plays song from music library
- Example: *"Play song1"*

#### 📰 News
- *"News"* - Reads latest US news headlines

#### 🧠 AI Conversations
- Ask any question: *"Who is Hrithik Roshan?"*
- General queries: *"What is artificial intelligence?"*
- The AI will provide intelligent responses for any unrecognized commands

## 📁 Project Structure

```
Project Jarvis/
├── main.py              # Main application file
├── client.py            # AI client testing
├── musicLibrary.py      # Music library configuration
├── api.env              # API keys (not in Git)
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🛠️ Technical Details

### Core Components

- **Speech Recognition**: Google Speech Recognition API
- **Text-to-Speech**: pyttsx3 library
- **AI Processing**: Groq AI (Llama3-8B model)
- **Web Control**: webbrowser module
- **News API**: NewsAPI.org integration

### Dependencies

```python
speech-recognition      # Voice input processing
pyttsx3                # Text-to-speech conversion
openai                 # Groq AI API client
python-dotenv          # Environment variable management
requests               # HTTP requests for news API
webbrowser             # Web browser automation
```

## 🎵 Music Library Setup

Edit `musicLibrary.py` to add your favorite songs:

```python
music = {
    "song1": "https://youtube.com/watch?v=example1",
    "song2": "https://youtube.com/watch?v=example2",
    # Add more songs here
}
```

## 🔍 Troubleshooting

### Common Issues

1. **Microphone not detected**
   ```bash
   pip install pyaudio
   ```

2. **Speech recognition errors**
   - Check internet connection
   - Ensure microphone permissions
   - Speak clearly after "Jarvis Active..." prompt

3. **AI not responding**
   - Verify GROQ_API_KEY in api.env
   - Check internet connection
   - Ensure API key is valid

4. **News not working**
   - Verify NEWS_API_KEY in api.env
   - Check NewsAPI.org status

### Debug Mode

Add print statements to see what's being recognized:
```python
print(f"Recognized command: {command}")
```

## 🛡️ Security

- ✅ API keys stored in environment files
- ✅ Environment files excluded from Git
- ✅ No hardcoded secrets in source code
- ✅ Secure API communication

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for fast AI inference
- [NewsAPI](https://newsapi.org/) for news data
- [OpenAI](https://openai.com/) for the API client library
- Python community for excellent libraries

## 📞 Support

If you have questions or need help:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an issue on GitHub
3. Visit [bipanneupane.com.np](https://bipanneupane.com.np) for more projects

---

**Made with ❤️ by Bipan Neupane**

*Say "Jarvis" and start your AI journey!* 🚀
