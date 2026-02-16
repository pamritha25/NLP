from textblob import TextBlob
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Get text input from user
text = input("Enter some text: ")
print("Text:", text)

# Analyze sentiment
sentiment = TextBlob(text).sentiment.polarity
print("Polarity:", sentiment)

# Determine sentiment label
if sentiment > 0:
    result = "Positive 😊"
elif sentiment < 0:
    result = "Negative 😞"
else:
    result = "Neutral 😐"

print("Sentiment:", result)

# Speak the sentiment
engine.say(f"The sentiment is {result}")
engine.runAndWait()

