from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

cse = Tk()




filename = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(("jpeg files", "*.jpg"),  ("png files", "*.png")))
image_label = Label(cse, text=filename)
image_label.pack()
my_image = ImageTk.PhotoImage(Image.open(filename))
my_image_label = Label(cse, image=my_image)
my_image_label.photo = my_image
my_image_label.pack()


cse.mainloop()
