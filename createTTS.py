# This file will generate the TTS files
import os
from gtts import gTTS as tts

# Define Top of the Hour Announcement
topText = "It is 9 PM. This is the 13 12 Records Radio Show and you are listening to K T E Q F M Rapid City 91.3 MegaHertz"
en = "en"
topAudio = tts(topText, lang=en, slow=False)
topAudio.save("announcements/1312.mp3")


def songList():
    """
    This function will generate the list of songs
    :return: list of songs
    """
    songList = []
    for root, dirs, files in os.walk("songs"):
        for file in files:
            songList.append(os.path.join(root, file))
    return songList