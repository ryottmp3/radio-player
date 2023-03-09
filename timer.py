import datetime
import os
import time
import playsound

i = 0

while i < 1000000000:
    start = time.time()
    date = datetime.datetime.now()
    topHourTTS = date.strftime("%M")
    topOfTheHour = './tts/1312.mp3'

    time.sleep(1)
    i += 1
    if topHourTTS == '00':
        playsound.playsound(topOfTheHour)
        
