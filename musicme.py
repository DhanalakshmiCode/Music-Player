#import modules
import speech_recognition as sr
import pyttsx3
import pyaudio
import os
import pandas as pd

#speaking engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',120)
print(voices[0].id)

#speaking tools audio output
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speech recognizer tools audio input
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 5
        audio = r.listen(source)
        print("I heared you")
        try:
            print("wait for few moments")
            query = r.recognize_google(audio,language='en-in')
            print("user said",query)
        except Exception as e:
            print(e)
            speak("Say that again please")
        return query


if __name__ == '__main__':
    query=takecommand().lower()
    #query="open"
    if 'open' in query:
        
        musicdir = "C:\songs_of"
        songs= os.listdir(musicdir)
        for i in range(len(songs)):
            song = songs[i].rstrip(songs[i][-4:])
            print(song)

        ax = song
        dg = pd.Series(ax)
        print(dg[0])
        
        
        #query='play the songs'             
        query  = takecommand().lower()
        if 'play the songs' in query:
            for i in range(len(dg)):
                os.startfile(os.path.join(musicdir,songs[i]))
                speak("Lets enjoy the song")
        elif 'play one' in query:
            query  = takecommand().lower()
            for i in range(len(dg)):
                a = query
                if a in query:
                    os.startfile(os.path.join(musicdir,a+".mp3"))
                    speak("Lets enjoy the song")
                else:
                    print("there is no song what you are telling is")
            
        else:
            print("Nothing in your playlist what you are saying is")


