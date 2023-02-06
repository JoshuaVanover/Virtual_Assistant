import speech_recognition
import vaFunc

recognizer = speech_recognition.Recognizer()

while True:

    vaFunc.setupMicrophone()

    while True:

        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                recognizer.pause_threshold = 0.8
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                print(f"$$$ {text}")

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            vaFunc.proccessComplete()
            break

        if 'play classic rock' in text:
            vaFunc.stopListen()
            exec(open(r"Executables\classicrock.py").read())
            vaFunc.proccessComplete()
            break

        if 'play diamond city radio' in text:
            vaFunc.stopListen()
            exec(open(r"Executables\diamondcity.py").read())
            vaFunc.proccessComplete()
            break

        if 'open tech news' in text:
            vaFunc.stopListen()
            exec(open(r"Executables\technews.py").read())
            vaFunc.proccessComplete()
            break

        if '3d printing' in text:
            vaFunc.stopListen()
            exec(open(r"Executables\printing.py").read())
            vaFunc.proccessComplete()
            break

        if 'stop music' in text:
            vaFunc.stopListen()
            vaFunc.closeInstance('firefox.exe')
            break

        if "what's the weather" in text:
            exec(open(r"Executables\weather.py").read())
            break
