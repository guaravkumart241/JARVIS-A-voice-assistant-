# Take input using Text
def take_input(i):
    # i=input('ME:')
    return i


# Take Input using Microphone
# import speech_recognition as sr
# def take_input():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said:-{query}")
#     except Exception:
#         print("Say that again please!")
#         return "None"
#     return query


