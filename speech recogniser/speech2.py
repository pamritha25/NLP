from deep_translator import GoogleTranslator

text = input("Enter text in English: ")

translated = GoogleTranslator(source='en', target='ml').translate(text)

print("Malayalam:", translated)