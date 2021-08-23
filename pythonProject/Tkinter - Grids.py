import tkinter

root = tkinter.Tk()

#Criamos um Widget de Label = Aqui nós criamos
mylabel1 = tkinter.Label(root, text ='Olá, Mundo!')
mylabel2 = tkinter.Label(root, text ='Meu nome é Daniel Pinheiro!')
mylabel3 = tkinter.Label(root, text='')

#Mostrar na tela = Aqui a gente põe na tela
mylabel1.grid(row=0, column =0)
mylabel2.grid(row=1, column =5)
mylabel3.grid(row=1, column=1)


root.mainloop()

