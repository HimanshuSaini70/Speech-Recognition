# Python program to translate 
#text to speech 
#Install following
#pip install pyttsx3

import pyttsx3 
 
converter = pyttsx3.init() # Initialize the converter 
   
converter.setProperty('rate', 200)  # Sets speed percent 
converter.setProperty('volume', 1)  # Set volume 0-1 
  
# entered text  There will be a pause between each one like a pause in  a sentence 
converter.say("Hello how are you") 
converter.say("Program will not continue until all speech is done talking ") 
  
converter.runAndWait()  # Program will not continue until all speech is done talking 
