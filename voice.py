import speech_recognition as sr
import pyttsx3 

# Inisialisasi speech recognizer
r = sr.Recognizer() 

# Fungsi untuk mengubah teks menjadi suara
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

# Fungsi untuk mendengarkan suara dan mengubahnya menjadi teks
def spToText(): 
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)

            # Mengubah suara menjadi teks
            text = r.recognize_google(audio)
            return text.lower()
    except sr.RequestError as e:
        print("Could not request results:", e)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    return None