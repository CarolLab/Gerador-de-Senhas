import tkinter as tk
import random


def gerar_senha():
    try:
        if 0 < int(size.get()) < 31:
            qt = int(size.get()) #get as a int, the valor of the entry SIZE

            abc = "aAbcCdDeEfghHijklmnNpPqrsStTuvwxyz123456789#$%*@"
            senha = ""

            for _ in range(qt):
                senha += random.choice(abc)

            senha_label.config(text = senha, fg = "Black", font = "Roboto 10 bold")
        else:
            senha_label.config(text="Insira um número positivo\nmenor que 31", fg="#b55609", font="Roboto 10 bold")

    except:
        senha_label.config(text="Error", fg = "red3")


#################################################################

jan = tk.Tk()

jan.title("Gerador de senhas")
jan.geometry("250x160")
jan.minsize(245,150)


#Entrys
size = tk.Entry(jan) #size of the password
size.grid(row = 1, column = 0, pady = 10)


#Labels
titl = tk.Label(jan, text = "Gerador De Senhas", padx=10, pady=5, font = "Rubix 19")
senha_label = tk.Label(jan, text = "") #Label da senha


titl.grid(row = 0, column = 0)
senha_label.grid(row = 3, column = 0, pady = 10)


#Buttons
gerar = tk.Button(jan, text = "Gerar", padx=10, cursor = "hand2", bg = "#32a858",
               command= gerar_senha) #Botão de gerar a senha
gerar.grid(row = 2, column = 0)

jan.mainloop()