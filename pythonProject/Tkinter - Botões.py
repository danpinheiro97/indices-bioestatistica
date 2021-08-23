from tkinter import *

root = Tk()

e = Entry(root)

def myclick():
    mylabel = Label(root, text='Olha, eu cliquei em um bottão!!', fg="white", bg ="black")
    mylabel.pack()

mybutton = Button(root, text= 'Clique aqui!',  padx = 50, pady = 50, command=myclick, fg="blue", bg="black")
mybutton.pack()

root.mainloop()

# Funções do botão
# padx = aumenta o tamanho no eixo X
# pady = aumenta o tamanho no eixo y
# state = DISABLED - desativa
# command = nome da sua função def - Ativa o botão de acordo com a função, se  por () ele vira uma label fixa
# fg ="color" - Muda a cor do texto do botão
# bg ="color" = muda a cordo do botão - BackGround
