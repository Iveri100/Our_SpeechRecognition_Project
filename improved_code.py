import speech_recognition as sr
import webbrowser as wb

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please, say anything: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("Right now you said : {}".format(text))
        if "google search" in text:
            text = text.replace("google search", '')
            wb.open_new_tab(f'https://www.google.com/search?rlz=1C2CHZL_enGE685GE776&source=hp&ei=DAjMXL6zAcfZwQL9j56gBw&q={text}&btnK=Google+%E1%83%AB%E1%83%94%E1%83%91%E1%83%9C%E1%83%90&oq={text}&gs_l=psy-ab.3..0i19l3j0i10i19j0i19l4j0i10i19j0i19.5635.5671..6144...0.0..0.431.1701.0j1j1j0j3......0....1..gws-wiz.....0..35i39i19j0i324j0i3j35i39.A6jItbFbxCY')

    except:
        print("Google Speech Recognition could not understand audio!")
