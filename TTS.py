from gtts import gTTS 
import os
file = open("abc.txt", "r").read()
speech = gTTS(text=file, lang='en' )
speech.save("voice.mp3")
os.system("voice.mp3")
print(file)
