from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Daniel")
root.iconbitmap('c:/users/gusta/imagens/teste2.ico')


photo1 = ImageTk.PhotoImage(Image.open("c:/users/gusta/imagens/teste.png"))
photo2 = ImageTk.PhotoImage(Image.open("c:/users/gusta/imagens/teste1.png"))
photo3 = ImageTk.PhotoImage(Image.open("c:/users/gusta/imagens/teste2.ico"))

image_list = [photo1, photo2, photo3]

mylabel = Label(image = photo1)
mylabel.grid(row=0, column=0, columnspan=3)

def forward(imgn):
    global mylabel
    global bbutton
    global nbutton
    mylabel.grid_forget()
    mylabel = Label(image=image_list[imgn+1])

    nbutton = Button(root, text=">>", command= lambda: forward(imgn + 1))
    bbutton = Button(root, text="<<", command = lambda: back(imgn - 1))

    if imgn == 2:
        nbutton = Button(root, text=">>", state= DISABLED)
    mylabel.grid(row=0, column=0, columnspan=3)
    bbutton.grid(row=1, column=0)
    nbutton.grid(row=1, column=2)


def back():
    global mylabel
    global bbutton
    global nbutton
bbutton = Button(root, text='<<', command=back)
ebutton = Button(root, text='Sair', command=root.quit)
nbutton = Button(root, text='>>',command = lambda: forward(0))


bbutton.grid(row=1, column=0)
ebutton.grid(row=1, column=1)
nbutton.grid(row=1, column=2)


root.mainloop()











root.mainloop()