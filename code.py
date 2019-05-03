import speech_recognition as sr
#ამ ბრძანებით მოქმედებაში მოდის მიკროფონი:
r = sr.Recognizer()
#ამ ბრძანებით მიკროფონის wav ფაილის წაკითხვა ხდება.
with sr.Microphone() as source:
    print("Tqvi rame :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("sheni sityvaa : {}".format(text))
    except:
        print("bodishi ver gavige!")
