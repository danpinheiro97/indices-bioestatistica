from tkinter import *

root = Tk()
root.title("Calculadora")

e = Entry(root, width=45, borderwidth=5, bg ="Black", fg="White")
e.grid(row= 0, column=0, columnspan=3, padx=10, pady=10)
def button_click(num):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))
def button_clear():
    e.delete(0, END)

def button_add():
    firstn = e.get()
    global num
    global math
    math = "soma"
    num = int(firstn)
    e.delete(0, END)
def button_equal():
    secondn = e.get()
    e.delete(0, END)
    if math == "soma":
        e.insert(0, num + int(secondn))
    if math =="multiplicacao":
        e.insert(0, num * int(secondn))
    if math =="divisao":
        e.insert(0, num / int(secondn))
    if math == "subtracao":
        e.insert(0, num - int(secondn))
def button_sub():
    firstn = e.get()
    global num
    global math
    math = "subtracao"
    num = int(firstn)
    e.delete(0, END)
def button_mul():
    firstn = e.get()
    global num
    global math
    math = "multiplicacao"
    num = int(firstn)
    e.delete(0, END)
def button_div():
    firstn = e.get()
    global num
    global math
    math = "divisao"
    num = int(firstn)
    e.delete(0, END)

#Definindo os botões
button1 = Button(root, text = '1', padx=39, pady=20, bg ="Black", fg="White", command= lambda : button_click(1))
button2 = Button(root, text = '2', padx=39, pady=20, bg ="Black", fg="White", command= lambda: button_click(2))
button3 = Button(root, text = '3', padx=39, pady=20, bg ="Black", fg="White",command= lambda: button_click(3))
button4 = Button(root, text = '4', padx=39, pady=20, bg ="Black", fg="White",command=lambda:button_click(4))
button5 = Button(root, text = '5', padx=39, pady=20, bg ="Black", fg="White",command=lambda:button_click(5))
button6 = Button(root, text = '6', padx=39, pady=20, bg ="Black", fg="White",command=lambda:button_click(6))
button7 = Button(root, text = '7', padx=39, pady=20, bg ="Black", fg="White",command=lambda:button_click(7))
button8 = Button(root, text = '8', padx=39, pady=20, bg ="Black", fg="White",command=lambda:button_click(8))
button9 = Button(root, text = '9', padx=39, pady=20, bg ="Black", fg="White",command=lambda:button_click(9))
button0 = Button(root, text = '0', padx=39, pady=20, bg ="Black", fg="White",command=lambda:button_click(0))
buttonadd = Button(root, text = '+', padx=38, pady=20, bg ="Black", fg="White",command=button_add)
buttonclear = Button(root, text = 'Clear', padx=79, pady=20, bg ="Black", fg="White",command=lambda:button_clear())
buttonigual = Button(root, text = '=', padx=91, pady=20, bg ="Black", fg="White",command=button_equal)
buttonsub = Button(root, text= '-', padx=39, pady=20, bg ="Black", fg="White",command = button_sub)
buttonmul = Button(root, text='*', padx=40, pady=20, bg ="Black", fg="White",command= button_mul)
buttondiv = Button(root, text='/', padx=39, pady=20, bg ="Black", fg="White",command = button_div)


#Mostrar na tela = Aqui a gente põe na tela
buttonsub.grid(row=6, column = 0)
buttonmul.grid(row=4, column = 1)
buttondiv.grid(row=4, column = 2)

button1.grid(row =3, column=0)
button2.grid(row =3, column=1)
button3.grid(row =3, column=2)

button4.grid(row =2, column=0)
button5.grid(row =2, column=1)
button6.grid(row =2, column=2)

button7.grid(row =1, column=0)
button8.grid(row =1, column=1)
button9.grid(row =1, column=2)

button0.grid(row =4, column=0)
buttonclear.grid(row=5, column=1, columnspan=2)
buttonadd.grid(row=5, column=0)
buttonigual.grid(row=6, column=1, columnspan=2)




root.mainloop()



# Funções do botão
# padx = aumenta o tamanho no eixo X
# pady = aumenta o tamanho no eixo y
# state = DISABLED - desativa
# command = nome da sua função def - Ativa o botão de acordo com a função, se  por () ele vira uma label fixa
# fg ="color" - Muda a cor do texto do botão
# bg ="color" = muda a cordo do botão - BackGround

# Input
# Entry = Função que abre o Input
# variavel.pack() = Empacota e mostra o input
# width = 50 - Muda o tamanho do input
# bg e fg = muda a cor do background e texto
# borderwidth = Muda o tamanho das bordas do input
# input.get() = Pega o resultado do input e joga onde você codou o comando
# Pode se usar um comando de texto nas label e utilizar o sinal + input.get() para colocar a entrada junto
# insert(0, "") Acrescenta um texto previews no input