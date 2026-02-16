# Simple language detector
from langdetect import detect

# Get user input
text = input("Enter some text: ").strip()

# Only run if text is not empty
if text:
    try:
        language = detect(text)
        print("Text:", text)
        print("Detected Language:", language)
    except Exception as e:
        print("Could not detect language:", e)
else:
    print("You entered empty text!")






