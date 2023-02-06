import speech_recognition
from selenium import webdriver
from playsound import playsound
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


def findMusic(playlist):
    driver = webdriver.Firefox()
    driver.minimize_window()

    driver.get(playlist)

    path = os.path.abspath(r'C:\FoxExt\adblock_for_firefox-5.3.3.xpi')
    driver.install_addon(path)

    notExec = True

    while notExec:
        try:
            time.sleep(5)
            driver.find_element(By.XPATH,
                                '/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-browse-response/div[2]/div[2]/ytmusic-detail-header-renderer/div/ytmusic-menu-renderer/div/yt-button-renderer/a').click()
            notExec = False
        except NoSuchElementException:
            continue


def startListen():
    playsound(r"Sounds\Listening.wav")


def stopListen():
    playsound(r"Sounds\NotListening.wav")


def proccessComplete():
    playsound(r"Sounds\ProcessedFinished.wav")


def setupMicrophone():
    recognizer = speech_recognition.Recognizer()

    while True:

        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                print(f"$$$ {text}")

        except speech_recognition.UnknownValueError:

            recognizer = speech_recognition.Recognizer()
            continue

        if "hey computer" in text:
            startListen()
        else:
            continue

        break

def closeInstance(instance):
    os.system(f"TASKKILL /IM {instance} /F")

