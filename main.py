import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()  #Its used to recognize what we are speaking Recognizer is a class
engine = pyttsx3.init() #initialising text to  speech  engine

def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__" :
    speak("Initializing Jarvis......")
    #listen for the wake word Jarvis 
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            audio = r.listen(source)

        command = r.recognize_sphinx(audio)
        print(command)

        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))