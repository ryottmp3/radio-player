import datetime
import os
import time


i = 0

while i < 1000000000:
    start = time.time()
    date = datetime.datetime.now()
    topHourTTS = date.strftime("%M")

    time.sleep(1)
    i += 1
    if topHourTTS == '00':
        os.system("mpg123 ./tts/1312.mp3")
    

