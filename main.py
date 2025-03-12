import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()  #Its used to recognize what we are speaking Recognizer is a class
engine = pyttsx3.init() #initialising text to  speech  engine

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    pass

if __name__ == "__main__" :
    speak("Initializing Jarvis......")
    #listen for the wake word Jarvis 
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
       
        # # recognize speech using Sphinx
        # try:
        #     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        # except sr.UnknownValueError:
        #     print("Sphinx could not understand audio")
        # except sr.RequestError as e:
        #     print("Sphinx error; {0}".format(e))

        # recognize speech using google cloud


        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yeah baby tell what happened !!")
                ##Listen for command
                with sr.Microphone() as source:
                    print("Jarvis is active...")
                    audio = r.listen(source,phrase_time_limit=2)
                    command = r.recognize_google(audio)
                    processCommand()

        # except sr.UnknownValueError:
        #     print("Sphinx could not understand audio")
        except Exception as e:
            print("Not recognizing...")
