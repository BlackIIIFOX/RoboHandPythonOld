import requests
import uuid
import pyaudio,wave
import os
import urllib.request as url_req
import xml.etree.cElementTree as ET
import receotion


def Record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 2
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Done recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


#data = ({'key': "be227abb-a848-41a0-bf7d-a547e9d62068"},{'uuid':str(uuid.uuid4())}, {"topic":"queries"}, {"lang": "ru-RU"})



import time
def Send():
    #start=time.time()
    data = open('output.wav', "rb").read()
    headers = {"Content-Type": 'audio/x-wav'}
    uuid = '88F1A7CB90D9D1B6A40D50465DE28C54'
    key='be227abb-a848-41a0-bf7d-a547e9d62068'
    url = 'https://asr.yandex.net/asr_xml?key=' + key + '&uuid=' + uuid + '&topic=queries&lang=ru-RU'
    r = requests.post(url, headers=headers, data=data)
    #print(time.time()-start)
    print(r.text)
    return r.text

'''
Record()

xml_answer = Send()
xml_file = open('DATA/XML/file.xml','w')
#print(xml_answer)
xml_file.write(xml_answer)
xml_file.close()
#xml_file.write(line.decode('utf8').encode('cp1251'))
'''

text = """<?xml version="1.0" encoding="utf-8"?>
<recognitionResults success="1">
	<variant confidence="0">сжаыытьыфв</variant>
	<variant confidence="0">сжать</variant>
</recognitionResults>"""

hand_rec = receotion.Hand("COM14",9600)

if __name__ == "__main__":
    while(1):
        print("Нажмите кнопку")
        input()
        Record()
        xml_answer = Send()
        root = ET.fromstring(xml_answer)

        for appt in root.getchildren():
            print(appt.text)
            res = hand_rec.contol_hand(appt.text)
            if (res == True): break
