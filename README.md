# 🎙️ Kiva Voice Assistant

Kiva is a powerful and intelligent voice assistant built with Python. It helps you perform various tasks hands-free, from searching the web to playing music and fetching the latest news.

## ✨ Features

- **🗣️ Voice Interaction**: Responds to voice commands using speech recognition and text-to-speech.
- **🔍 Web Search**: Performs Google searches instantly.
- **🎵 Media Playback**: Plays songs directly on YouTube.
- **📰 News Updates**: Fetches top 5 headlines from the US via NewsAPI.
- **☀️ Weather Reports**: Provides current weather updates for India (default) or other locations using WeatherAPI.
- **🚀 App & Website Launching**: Opens popular websites like Google, YouTube, Facebook, Instagram, etc.
- **🤖 AI-Powered Chat**: Uses OpenAI's GPT-3.5 Turbo to answer general questions and engage in conversation when a specific command isn't recognized.
- **⏰ Time & Date**: Tells you the current time, date, and day.

## 🛠️ Prerequisites

- Python 3.8 or higher
- An active internet connection
- API Keys for:
    - [NewsAPI](https://newsapi.org/)
    - [WeatherAPI](https://www.weatherapi.com/)
    - [OpenAI](https://platform.openai.com/)

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kaustav3071/Kiva-Voice-Assistant.git
   cd Kiva-Voice-Assistant
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *Note: You may need to install PyAudio manually if `pip install` fails. For Windows, you might need `pip install pipwin` followed by `pipwin install pyaudio` if standard installation issues occur.*

## ⚙️ Configuration

1. **Locate the configuration file:**
   The configuration file is located at `src/config.py`.

2. **Add your API Keys:**
   Open `src/config.py` and replace the placeholder text with your actual API keys:

   ```python
   NEWS_API_KEY = "your_news_api_key_here"
   WEATHER_API_KEY = "your_weather_api_key_here"
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```

## 🚀 Usage

1. **Run the assistant:**
   ```bash
   python src/assistant.py
   ```

2. **Activate Kiva:**
   The assistant listens for the wake word. Say:
   > "Kiva" or "Hello Kiva"

3. **Give a command:**
   Once activated, Kiva will ask how it can help. Try commands like:
   - *"Play [song name]"* (e.g., "Play Believer")
   - *"Search [query]"* (e.g., "Search for Python tutorials")
   - *"Tell me the news"*
   - *"What's the weather?"*
   - *"Open YouTube"*
   - *"What time is it?"*
   - *"Who created you?"*
   - *"Shutdown"* to exit.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
