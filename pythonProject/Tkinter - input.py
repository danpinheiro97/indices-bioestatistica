from tkinter import *

root = Tk()

e = Entry(root, width=50, bg ="blue", fg = "white", borderwidth=10)
e.pack()
e.insert(0, "Entre com seu nome: ")

def myclick():
    hello = "Hellow" + e.get()
    mylabel = Label(root, text= hello , fg="white", bg ="black")
    mylabel.pack()

mybutton = Button(root, text= 'Entre com seu nome',  padx = 50, pady = 50, command=myclick, fg="blue", bg="black")
mybutton.pack()

root.mainloop()

# Input
# Entry = Função que abre o Input
# variavel.pack() = Empacota e mostra o input
# width = 50 - Muda o tamanho do input
# bg e fg = muda a cor do background e texto
# borderwidth = Muda o tamanho das bordas do input
# input.get() = Pega o resultado do input e joga onde você codou o comando
# Pode se usar um comando de texto nas label e utilizar o sinal + input.get() para colocar a entrada junto
# insert(0, "") Acrescenta um texto previews no input