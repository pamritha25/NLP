import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Input text
text = input("Enter text in English: ")

# Speak text
engine.say(text)
engine.runAndWait()