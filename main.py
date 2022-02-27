import pyttsx3
import datetime
import speech_recognition as sr
# import wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound
# from ecapture import ecapture as ec


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Hay-raah")

    elif 12 < hour < 18:
        speak("Good Afternoon Hay-raah")

    else:
        speak("Good Evening Hay-raah")

    speak("Hey Hay-raah, I am Zira How may I help you?")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Sorry, I didn't catch what you said.")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hira.zehra.ai.project@gmail.com', 'sendemail123')
    server.sendmail('hira.zehra.ai.project@gmail.com', to, content)
    server.close()


if __name__ == "__main__":

    wishme()

    query = takeCommand().lower()

        # if 'wikipedia' in query:
        #     speak('Searching Wikipedia...')
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=1)
        #     speak("According to Wikipedia")
        #     print(results)
        #     speak(results)


    if 'youtube' in query:
         webbrowser.open("https://www.youtube.com")
         speak("Youtube is opened")

    elif 'google' in query:
        webbrowser.open("https://www.google.com")
        speak("Google is opened")

    elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("Facebook is opened")

    elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("Instagram is opened")

    elif 'whatsapp web' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("Whatsapp web is opened")

    elif 'open gmail' in query:
            webbrowser.open_new_tab("https://gmail.com/")
            speak("Google Mail is opened")

    elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)

    elif 'play music' in query:
            print('playing your favourite song... \n \t \t E N J O Y (:')
            playsound('C:\\Users\\Dell\\Music\\myFavSong.mp3')

            # In music_dr = Give the path wherever you have your music saved
            # music_dir = 'C:\\Users\\Dell\\Music\\myFavSong.mp3'
            # songs = os.listdir(music_dir)  # This will list all the music you have
            # print(songs)
            # os.startfile(os.path.join(music_dir, songs[0]))

    elif 'open vs code' in query:
        codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'open android studio' in query:
        codePath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
        os.startfile(codePath)

    elif 'email to person' in query:
        try:
                speak("What should I say?")
                content = takeCommand()
                to = "heyraaahzehra@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Failed to send email.")

    elif 'about yourself' in query:
        speak('I am Zira. I am always here for you.')

    elif 'creator' in query:
        codePath = "C:\\Users\\Dell\\Documents\\creators.jpeg"
        os.startfile(codePath)

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Hey-Rah, the time is {strTime}")

    elif 'bye' in query:
        speak('Bye Hay-Rah Take care')
        exit()










