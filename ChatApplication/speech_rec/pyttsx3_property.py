import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
rate = engine.getProperty("rate")
print("the default speed of the speech is", rate)
vol = engine.getProperty("volume")
print("the default volume of the speech is", vol)

voice_id = 1
engine.setProperty('voice', voices[voice_id].id)
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.5)
engine.say("This is a test of my speech id, speed, and volume.")
engine.runAndWait()