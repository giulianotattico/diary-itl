import speech_recognition as sr


def speech(lang="it_IT"):
    mic= sr.Microphone()
    recog= sr.Recognizer()

    with mic as audio_file:
        print("si prega di parlare")
        recog.adjust_for_ambient_noise(audio_file)
        audio= recog.listen(audio_file)

        return recog.recognize_google(audio, language=lang )
if __name__=="__name__":  
    print("conversione dell'audio in testo...")
    print(f"hai detto:{speech()}")
    
