from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
from googletrans import Translator
from translate import Translator
from subprocess import call
import os
import pytesseract
import tkinter.font as font
rin=Tk()
rin.geometry('1080x450')
rin.resizable(0,0)
rin.title("Image Translator")
rin.iconbitmap(r'C:\Users\DELL\Downloads\hnet.com-image.ico')
canvas=Canvas(rin,width=1080,height=450)
image=ImageTk.PhotoImage(file="images/pic1.png")
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
myFont = font.Font(family='Londrina Solid',weight="bold")
Label(rin, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()
Input_text = Text(rin,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 58)
Input_text.place(x=34,y = 155)
Output_text = Text(rin,font = 'arial 10 bold', height = 11, wrap = WORD, padx=5, pady= 5, width =58)
Output_text.place(x = 600 , y = 155)
fontExample = ("Courier", 16, "bold")
language = [ "English","Hindi","Gujarati","Spanish","German","French","persian","Chinese"]
src_lang = ttk.Combobox(rin, values= language,font = fontExample, width =25)
src_lang.place(x=34,y=99)
src_lang.set('choose input language')
dest_lang = ttk.Combobox(rin, values= language,font = fontExample, width =25)
dest_lang.place(x=600,y=99)
dest_lang.set('choose output language')
def dialogbox():
    from tkinter import filedialog
    from PIL import ImageTk, Image
    import pytesseract

    filename = filedialog.askopenfilename(initialdir="/", title="Select An Image",
                                          filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))


    pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image = Image.open(filename)
    image_to_text = pytesseract.image_to_string(image)
    Input_text.insert("0.1",image_to_text)

def Translate():
    translator = Translator(from_lang= src_lang.get(), to_lang = dest_lang.get())
    translated=translator.translate( Input_text.get(1.0, END) )

    Output_text.insert("0.1", translated)

trans_btn = Button(rin, text='TRANSLATE',font=myFont, pady=1, command=Translate, bg='royal blue1',
                   activebackground='sky blue')
trans_btn.place(x=460, y=220)

def exit():
    rin.destroy()
def speech():
    call(["python","speech.py"])
def text():
    call(["python","text.py"])
btn3 = Button(rin,text ="TEXT",width=10, command=text,bg = 'red',activebackground = 'sky blue',font =myFont,pady = 2)
btn3.place(x=62,y=363)
btn4 = Button(rin,text ="EXIT",width=10,command=exit,bg = 'red', activebackground = 'sky blue',font =myFont,pady = 2)
btn4.place(x=900,y=363)
btn2 = Button(rin,text ="SPEECH",width=10,command=speech,bg = 'red', activebackground = 'sky blue',font =myFont,pady = 2)
btn2.place(x=470,y=363)
btn5= Button(rin,text ="CHOOSE",command=dialogbox ,font=myFont ,width=10,bg = 'MediumSeaGreen', pady = 2)
btn5.place(x=910, y=33)
mainloop()