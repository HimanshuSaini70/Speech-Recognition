import speech_recognition as sr 
  
AUDIO_FILE = ("Record Example.wav")   # use the audio file as the audio source 
  
r = sr.Recognizer() 
  
with sr.AudioFile(AUDIO_FILE) as source: 
    audio = r.record(source)   
  
try: 
    print("The Text from audio file are: " + r.recognize_google(audio)) 
  
except sr.UnknownValueError: 
    print("Audio is not Clear") 
  
except sr.RequestError as e: 
    print("Try Again; {0}".format(e)) 
