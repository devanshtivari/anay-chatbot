import pyttsx3
import datetime
#pyttsx3 module is python text to speech
#hello : in speech
#microsoft : sapi5
#hello
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#engine->voices[voice]
print(voice[0].id)
#voice[1] : female {zira}
#voice[0] : male {david}
engine.setProperty('voice' , voice[0].id)

#speak->text->variable->text->speech

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning")
    if hour>12 and hour<=16:
        speak("good Afternoon")
    else:
        speak("Good Evening")
    


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    WishMe()



