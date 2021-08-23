from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Daniel")
root.iconbitmap('c:/users/gusta/star.ico')

photo = ImageTk.PhotoImage(Image.open("c:/users/gusta/icon.png"))

root.mainloop()
