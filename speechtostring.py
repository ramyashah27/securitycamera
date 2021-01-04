import speech_recognition as s 
# create a object of Recognizer
sr=s.Recognizer()
print("i am your script and listening you")
with s.Microphone() as m:
    audio=sr.listen(m)
    query=sr.recognize_google(audio,language='eng-in')
    print(query)

if query==str('good'):
    print('yes')