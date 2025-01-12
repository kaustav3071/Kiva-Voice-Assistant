import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as pyt
import requests as r
from openai import OpenAI
import datetime
from config import NEWS_API_KEY, WEATHER_API_KEY, OPENAI_API_KEY

recogniser = sr.Recognizer()
engine = pyt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    print("You Said: " + command)
    print("Processing Command...")

    commands = {
        "open google": "https://www.google.com",
        "open youtube": "https://www.youtube.com",
        "open facebook": "https://www.facebook.com",
        "open twitter": "https://www.twitter.com",
        "open instagram": "https://www.instagram.com",
        "open linkedin": "https://www.linkedin.com",
        "open github": "https://www.github.com",
        "open cricbuzz": "https://www.cricbuzz.com",
        "open whatsapp": "https://web.whatsapp.com",
        "open gmail": "https://mail.google.com",
        "open amazon": "https://www.amazon.com",
        "open flipkart": "https://www.flipkart.com",
    }

    if "who created you" in command.lower():
        speak("I was created by KAUSTAV DAS ")

    elif command.lower().startswith("play"):
        song = command.replace("play", "")
        speak(f"Playing {song}")
        wb.open(f"https://www.youtube.com/results?search_query={song}")

    elif command.lower().startswith("search"):
        search = command.replace("search", "")
        speak(f"Searching {search}")
        wb.open(f"https://www.google.com/search?q={search}")

    elif command.lower() in commands:
        speak(f"Opening {command.split(' ')[1].capitalize()}")
        wb.open(commands[command.lower()])

    elif "time" in command.lower():
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "date" in command.lower():
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        speak(f"The date is {date}")

    elif "day" in command.lower():
        day = datetime.datetime.now().strftime("%A")
        speak(f"Today is {day}")

    elif "news" in command.lower():
        speak("I tell only US news")
        speak("Please wait, fetching the latest news for you")
        print("Fetching News...")
        response = r.get(f"http://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}")
        speak("Here are some top 5 news for you")
        if response.status_code == 200:
            news = response.json()
            if "articles" in news:
                articles = news["articles"]
                for article in articles[0:5]:
                    speak(article["title"])
            else:
                speak("No news articles found.")
        else:
            speak("Sorry, I couldn't fetch the news. Please try again later.")

    elif "weather" in command.lower():
        speak("Please wait, fetching the weather for you")
        print("Fetching Weather...")
        response = r.get(f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q=India&aqi=no")
        speak("Here is the weather report for you")
        if response.status_code == 200:
            weather = response.json()
            speak(f"The temperature is {weather['current']['temp_c']} degree celsius")
        else:
            speak("Sorry, I couldn't fetch the weather. Please try again later.")

    elif command.lower() in ["shutdown", "quit", "exit"]:
        speak("Shutting down. Goodbye!")
        exit()

    elif "open" in command.lower():
        for key, value in commands.items():
            if key in command.lower():
                speak(f"Opening {key.split(' ')[1].capitalize()}")
                wb.open(value)
                break
        else:
            speak("Sorry, I cannot process this command.")

    else:
        try:
            client = OpenAI(api_key=OPENAI_API_KEY)    
            speak("Let me think about that...")
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": command}]
            )
            reply = response['choices'][0]['message']['content']
            speak(reply)
            print(reply)
        except Exception as e:
            speak("Sorry, I couldn't process your request with OpenAI.")
            print(f"OpenAI Error: {e}") 

if __name__ == "__main__":
    speak("Hello, I am kiva")
    while True:
        with sr.Microphone() as source:
            print("Kiva Listening...")
            print("Say 'Kiva' or 'Hello Kiva' to activate me")
            audio = recogniser.listen(source, phrase_time_limit=5)

        print("Kiva Recognizing...")
        try:
            word = recogniser.recognize_google(audio)
            if "kiva" in word.lower() or "shiva" in word.lower() or "hello" in word.lower():
                speak("Yes, How can I help you?")
                with sr.Microphone() as source:
                    print("Kiva Listening Your Command...")
                    audio = recogniser.listen(source, timeout=2, phrase_time_limit=5)
                    command = recogniser.recognize_google(audio)
                    process_command(command)

        except sr.UnknownValueError:
                speak("Sorry, I didn't catch that. Could you repeat?")
        except sr.RequestError as e:
                speak("There seems to be an issue with my speech service. Please try again later.")
                print(f"Speech Recognition Error: {e}")
