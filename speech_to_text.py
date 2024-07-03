import speech_recognition as sr

def recognize_speech_from_mic():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Set up the microphone
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        
        # Capture audio from the microphone
        audio = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Web Speech API
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    recognize_speech_from_mic()
