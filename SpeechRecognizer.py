import speech_recognition as sr
from TextAnalyzer import *

from os import path
audioFile = path.join(path.dirname(path.realpath(__file__)), "FB_Q1_2018_Financials_test.wav")

speechRecognizer = sr.Recognizer()

with sr.AudioFile(audioFile) as audioSource:
    audio = speechRecognizer.record(audioSource, offset = 20, duration = 15)

speechText = speechRecognizer.recognize_google(audio)

#try:
#    print("Google Speech Recognition thinks you said " + speechText)
#except sr.UnknownValueError:
#    print("Google Speech Recognition could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results from Google Speech Recognition service; {0}".format(e))

textAnalyzer = TextAnalyzer()
textAnalysisResult = textAnalyzer.AnalyzeText(speechText)

print("The results of the text analysis: ")
for key in textAnalysisResult:
    print(key + ": " + str(textAnalysisResult[key]))
