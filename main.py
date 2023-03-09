# This python file will parse the playlist and break it into sets of three songs. 

import os
import random 
import playsound
from gtts import gTTS as tts


currentPlaylist = input("What is the name of the playlist? ")
currentPlaylistDir = "./playlists/" + currentPlaylist + "/"

songs = []
en = "en"

def getPlaylistSongs(PlaylistDir):
    for file in os.listdir(currentPlaylistDir):
        if file.endswith(".mp3"):
            songs.append(file)
    random.shuffle(songs)
    return songs



if not os.path.exists(currentPlaylistDir):
    print('This playlist does not exist in the local repository.')
else:
    print('Playlist found:' + str(currentPlaylistDir))
    getPlaylistSongs(currentPlaylistDir)

    length = len(songs)
    
    appendedLength = length // 3

    for i in range(0, appendedLength):
        # print(songs[i])
        playSet = random.choices(songs, k=3)
        for song in playSet:
            songDir = currentPlaylistDir + song 
            print("Currently Playing: " + song)
            playsound.playsound(songDir)
        announcePlaySetText = "That was " + str(playSet[0]) + " followed by " + str(playSet[1]) + " and ending out the set with " + str(playSet[2]) + "."
        announcePlaySetAudio = tts(announcePlaySetText, lang=en, slow=False)
        announcePlaySetAudio.save("./tts/announcePlaySet.mp3")
        announcement = './tts/announcePlaySet.mp3'
        playsound.playsound(announcement)
        print(announcePlaySetText)
        


print(songs)







