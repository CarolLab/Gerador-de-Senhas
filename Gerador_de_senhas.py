from tkinter import *
import random


def funcao():
    try:
        qt = int(size.get()) #get as a int, the valor of the entry SIZE


        sim = "aAbcCdDeEfghHijklmnNpPqrsStTuvwxyz123456789#$%*@"
        senha = ""

        for _ in range(qt):
            senha += random.choice(sim)

        senha_label.config(text = senha, fg = "Black", font = "Roboto 10 bold")

    except:
        senha_label.config(text="Error", fg = "red3")




jan = Tk()

jan.title("Gerador de senhas")
jan.geometry("250x150")


#Entrys
size = Entry(jan, cursor = "hand2")
size.grid(row = 1, column = 0, pady = 10)


#Labels
titl = Label(jan, text = "Gerador De Senhas", padx=10, pady=5, font = "Rubix 19")
titl.grid(row = 0, column = 0)



senha_label = Label(jan, text = "", pady= 8) #Label da senha
senha_label.grid(row = 3, column = 0)

#Buttons
gerar = Button(jan, text = "Gerar", padx=10,
               command= funcao) #Botão de gerar a senha
gerar.grid(row = 2, column = 0)

jan.mainloop()