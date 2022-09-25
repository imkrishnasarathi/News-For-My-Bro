import requests
import json
import pyttsx3

def speak(str):
    engine = pyttsx3.init()
    print(str)
    engine.say(str)
    engine.runAndWait()

if __name__ == '__main__':
    speak('Oh Hello! I am the News Reader Programmed By Krishna. I will read out the latest news for you!')
    speak("How Many News Do You Want to Hear?")
    a = int(input("How Many Latest News do you want to hear?: "))

    url1 = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=YOUR_API_KEY'

    news1= requests.get(url1).text
    news_json = json.loads(news1)
    art = news_json['articles']

    for index, article in enumerate(art):
        if index == a: 
            break
        speak(f'''News Number - {index+1}.. 
        Title - {article['title']}
        Description - {article['description']}
        Content - {article['content']}
        ''')

    speak("Thanks For Listening. Come Back Tomorrow For More News...")







