#!/usr/bin/env python
# coding: utf-8



from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from googletrans import Translator
from translate import Translator
from subprocess import call
import tkinter.font as font
root = Tk()
root.geometry('1080x450')
root.resizable(0,0)
root.title("Language Translator")
root.iconbitmap(r'C:\Users\DELL\Downloads\hnet.com-image.ico')
canvas=Canvas(root,width=1080,height=450)
image5=ImageTk.PhotoImage(file="images/pic1.png")
canvas.create_image(0,0,anchor=NW,image=image5)
canvas.pack()
myFont = font.Font(family='Londrina Solid',weight="bold")
Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 58,highlightbackground='blue')
Input_text.place(x=34,y = 155)
Output_text = Text(root,font = 'arial 10 bold', height = 11, wrap = WORD, padx=5, pady= 5, width =58)
Output_text.place(x = 600 , y = 155)
fontExample = ("Courier", 16, "bold")
language = [ "English","Hindi","Gujarati","Spanish","German","French","persian","Chinese"]
src_lang = ttk.Combobox(root, values= language,font = fontExample, width =25)
src_lang.place(x=34,y=99)
src_lang.set('choose input language')
dest_lang = ttk.Combobox(root, values= language,font = fontExample, width =25)
dest_lang.place(x=600,y=99)
dest_lang.set('choose output language')
def Translate():
    translator = Translator(from_lang= src_lang.get(), to_lang = dest_lang.get())
    translated=translator.translate( Input_text.get(1.0, END) )

    Output_text.insert("0.1", translated)

trans_btn = Button(root, text='TRANSLATE',font=myFont, pady=1, command=Translate, bg='royal blue1',
                   activebackground='sky blue')
trans_btn.place(x=460, y=220)

def speech():
    call(["python","speech.py"])

def image():
    call(["python", "image.py"])





btn4 = Button(root,text ="EXIT",width=10,command=exit,bg = 'red', activebackground = 'sky blue',font =myFont,pady = 2)
btn4.place(x=900,y=363)
def exit():
    root.destroy()
btn2 = Button(root,text ="SPEECH",command=speech,width=10,bg = 'red', activebackground = 'sky blue',font =myFont,pady = 2)

btn2.place(x=62,y=363)
btn3 = Button(root,text ="IMAGE",width=10,command=exit,bg = 'red', activebackground = 'sky blue',font =myFont,pady = 2)
btn3.place(x=470,y=363)
mainloop()   






