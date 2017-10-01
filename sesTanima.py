import speech_recognition as sr
import json
import requests
import webbrowser
import urllib3
import sys
import pygame
import os
import random
from threading import Thread
import copypaste
##
urllib3.disable_warnings()
## Komutlar
weat = "hava durumu"
ara = "internette ara"
youtube = "video ara"
bye = "güle güle"
music = "şarkı çal"
##
yer =  os.getcwd()
##
def main():
    print("Sistem: Giriş yapman bekleniyor.")
    deneme = True
    sayac = 0
    while deneme == True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source,timeout = None)
            try:
                metin = r.recognize_google(audio,language="tr-TR")
                if "ses kontrol" in metin.lower():
                    print("Sistem: Giriş başarılı.Hoşgeldin.")
                    os.chdir(yer)
                    calis()
                elif "kendini kapat" in metin.lower():
                    print("Asistan kapatılıyor.")
                    sys.exit()
            except sr.UnknownValueError:
                sayac += 1
            except sr.RequestError:
                sayac += 1
def calis():
    deneme = True
    while deneme == True:
        print("Ne istemiştin?")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source,timeout=None)
            try:
                metin = r.recognize_google(audio,language="tr-TR")
                print("Sen söyledin: " + metin)
                if weat in metin.lower():
                    print("Hangi şehrin hava durumunu merak ediyorsun?")
                    audio2 = r.listen(source,timeout=None)
                    try:
                        metin = r.recognize_google(audio2,language="tr-TR")
                        print("Söyledin: " + metin)
                        appid = "APPID" ## Openweather sitesine kayıt olup alabilirsiniz.
                        url = "http://api.openweathermap.org/data/2.5/weather?q=" + metin + "&appid=" + appid
                        istek = requests.get(url,verify=False)
                        try:
                            istek = istek.json()
                            name = istek["name"]
                            istek = istek["main"]
                            istek = istek["humidity"]
                            istek = (istek - 32) / 1.8
                            print(name,"hava durumu:",int(istek),"derece")
                        except:
                            print("Böyle bir yer yok.")
                    except sr.UnknownValueError:
                        print("Anlamadım.")
                    except sr.RequestError:
                        print("Bad Request")
                elif "güle güle" in metin.lower():
                    print("Sistem: Asistan arka plana alındı.\n")
                    os.chdir(yer)
                    main()
                elif ara in metin.lower():
                    print("İnternette ne aramamı istiyorsun?")
                    audio2 = r.listen(source,timeout=None)
                    try:
                        metin = r.recognize_google(audio2,language="tr-TR")
                        print("Bunu mu arayayım?: " + metin)
                        print("Evet/Hayır")
                        audio3 = r.listen(source,timeout=None)
                        try:
                            metin2 = r.recognize_google(audio3,language="tr-TR")
                            print("Söyledin: " + metin2)
                            url = "https://www.google.com/search?q=" + metin
                            if "evet" in metin2.lower():
                                webbrowser.open_new(url)
                        except sr.UnknownValueError:
                            print("Anlamadım.")
                        except sr.RequestError:
                            print("Bad request.")
                    except sr.UnknownValueError:
                        print("Anlamadım.")
                    except sr.RequestError:
                        print("Bad request.")
                elif youtube in metin.lower():
                    print("Youtube'da ne aramamı istiyorsun?")
                    audio2 = r.listen(source,timeout=None)
                    try:
                        metin = r.recognize_google(audio2,language="tr-TR")
                        print("Bunu mu arayayım?: " + metin)
                        print("Evet/Hayır")
                        audio3 = r.listen(source,timeout=None)
                        try:
                            metin2 = r.recognize_google(audio3,language="tr-TR")
                            print("Söyledin: " + metin2)
                            url = "https://www.youtube.com/search?q=" + metin
                            if "evet" in metin2.lower():
                                webbrowser.open_new(url)
                        except sr.UnknownValueError:
                            print("Anlamadım.")
                        except sr.RequestError:
                            print("Bad request")
                    except sr.UnknownValueError:
                        print("Anlamadım.")
                    except sr.RequestError:
                        print("Bad request.")
                elif music in metin.lower():
                    t = Thread(target = Cal)
                    t.start()
                elif "durdur" in metin.lower():
                    pygame.mixer.init()
                    pygame.mixer.music.stop()
                    print("Şarkı durduruldu.")
                elif "kopyala" in metin.lower():
                    print("Neyi kopyalamamı istiyorsun?")
                    audio2 = r.listen(source,timeout=None)
                    try:
                        metin = r.recognize_google(audio2,language = "tr-TR")
                        print("Kopyalandı: " + metin)
                        copypaste.copy(metin)
                    except sr.UnknownValueError:
                        print("Anlamadım.")
                    except sr.RequestError:
                        print("Bad Request")
            except sr.UnknownValueError:
                print("Anlamadım.")
            except sr.RequestError:
                print("Bad Request")
def Cal():
    sarkiList = []
    pygame.mixer.init()
    try:
        direc = yer + "\music"
        os.chdir(direc) ## Şarkılar kod dosyası ile aynı konumda olacaksa bu koda gerek yok.
        for i in os.listdir():
            if i.endswith(".mp3"):
                sarkiList.append(i)
        sayi = (random.randint(1,len(sarkiList))) - 1
        print(sarkiList)
        print("Çalan şarkı: " + sarkiList[sayi] + "\n")
        pygame.mixer.music.load(sarkiList[sayi])
        pygame.mixer.music.play()
    except:
        print("Şu an şarkı çalamıyorum.")
