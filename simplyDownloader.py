import vk_api
from vk_api import audio
import requests
from time import time
import os
from pprint import pprint
import sys

REQUEST_STATUS_CODE = 200
login = 'PHONE_NUMBER'  # Номер телефона
password = 'PASSWORD'  # Пароль
my_id = 'YOURID'  # Ваш id vk

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()  # Теперь можно обращаться к методам API как к обычным классам
vk_audio = audio.VkAudio(vk_session)  # Получаем доступ к audio

time_start = time()
#pprint(vk_audio.get())
def download(q):
    path = 'E:\\UB8CLB\\Music\\' + q
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    os.chdir(path)
    
    for i in vk_audio.search(q, count=3000, offset=0):
        try:
            url = i["url"]
            artist = i["artist"]
            title = i["title"]
            fileName = path + '\\' + artist + '_' + title + '.mp3'
            if not os.path.isfile(fileName):
                cmdLine = 'ffmpeg -http_persistent false -i ' + url + ' -c copy ' + '"' + artist + '_' + title + '.mp3' + '"'
                #print(cmdLine)
                os.system(cmdLine)
            
        except OSError:
            print(i["artist"] + '_' + i["title"])
    time_finish = time()
    print("Time seconds:", time_finish - time_start)

if __name__ == "__main__":
    q = sys.argv[1]
    download(q)