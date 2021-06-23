from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import tkinter.font as font
from PIL import ImageTk, Image
from googletrans import Translator
from translate import Translator
import os
from gtts import gTTS
from subprocess import call
win = Tk()
win.geometry('1080x450')
win.resizable(0, 0)




win.iconbitmap(r'C:\Users\DELL\Downloads\hnet.com-image.ico')
win.title("Speech Translator")
canvas1=Canvas(win,width=1080,height=450)
image1=ImageTk.PhotoImage(file="images/pic1.png")
canvas1.create_image(0,0,anchor=NW,image=image1)
canvas1.pack()
myFont = font.Font(family='Londrina Solid',weight="bold")





Input_text1 = Text(win, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=58)
Input_text1.place(x=34, y=155)



Output_text1 = Text(win, font='arial 10 bold', height=11, wrap=WORD, padx=5, pady=5, width=58)
Output_text1.place(x=600, y=155)

fontExample = ("Courier", 16, "bold")
language = ["English", "Hindi", "Gujarati", "Spanish", "German", "French", "persian", "Chinese"]
src_lang1 = ttk.Combobox(win, values=language, font=fontExample, width=25)
src_lang1.place(x=34, y=99)
src_lang1.set('choose input language')

dest_lang1 = ttk.Combobox(win, values=language, font=fontExample, width=25)
dest_lang1.place(x=600, y=99)
dest_lang1.set('choose output language')


def speak():
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            txt = r.recognize_google(audio)
            Input_text1.insert("0.1", txt)
            print(txt)
        except Exception as e:
            print(e)
            break


def translate1():
    from translate import Translator
    from gtts import gTTS
    translator = Translator(from_lang=src_lang1.get(), to_lang=dest_lang1.get())
    translated1 = translator.translate(Input_text1.get(1.0, END))
    Output_text1.insert("0.1", translated1)



speakbttn = Button(win,text='SPEAK',font=myFont ,width=10,command=speak,bg = 'MediumSeaGreen', pady = 2)
speakbttn.place(x=875, y=33)


def exit():
    win.destroy()
def image():
    call(["python", "image.py"])
def text():
    call(["python","text.py"])

trans_btn = Button(win, text='TRANSLATE',font=myFont, pady=1, command=translate1, bg='royal blue1',
                   activebackground='sky blue')
trans_btn.place(x=460, y=220)
btn2 = Button(win,text ="IMAGE",width=10,command=image,bg = 'red', activebackground = 'sky blue',font =myFont,pady = 2)
btn2.place(x=470,y=363)

btn3 = Button(win, text='TEXT',width=10, command=text,bg = 'red',activebackground = 'sky blue',font =myFont,pady = 2)
btn3.place(x=62,y=363)

btn4 = Button(win,text ="EXIT",width=10,command=exit,bg = 'red', activebackground = 'sky blue',font =myFont,pady = 2)
btn4.place(x=900,y=363)
mainloop()