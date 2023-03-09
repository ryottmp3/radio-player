# This file will generate the TTS files
import os
from gtts import gTTS as tts

# Define Top of the Hour Announcement
topText = "It is 9 PM. This is the 13 12 Records Radio Show and you are listening to K T E Q F M Rapid City 91.3 MegaHertz"
en = "en"
topAudio = tts(topText, lang=en, slow=False)
topAudio.save("tts/1312.mp3")


# currentPlaylist = input("What is the name of the playlist you want to add? ")