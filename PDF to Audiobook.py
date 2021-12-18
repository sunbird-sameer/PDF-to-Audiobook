import pyttsx3
import PyPDF2
engine = pyttsx3.init()
voices = engine.getProperty('voices')
book_name=input("Enter the book name: ")
full_book_name=book_name +'.pdf'
book = open(full_book_name,'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("Number Of Pages =", pages)
book_mark=int(input("Enter The Page You've Book Marked: "))
voice=int(input("Enter The Voice You Want: 0-Male 1-Female: "))
speed=int(input("Enter A Speed Between 1-5: "))
if speed == 1:
    engine.setProperty("rate", 125)
if speed == 2:
    engine.setProperty("rate", 135)
if speed == 3:
    engine.setProperty("rate", 145)
if speed == 4:
    engine.setProperty("rate", 155)
if speed == 5:
    engine.setProperty("rate", 165)
engine.setProperty('voice', voices[voice].id)
speaker =  pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(book_mark)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
