from tkinter import *
import random


def funcao():

    sim = "aAbcCdDeEfghHijklmnNpPqrsStTuvwxyz123456789#$%*@"
    senha = ""

    for _ in range(5):
        senha += random.choice(sim)

    result = Label(jan, text=senha, pady = 10, padx = 10)
    result.grid(row=2, column=0)



jan = Tk()

jan.title("Gerador de senhas")
jan.geometry("250x100")


titl = Label(jan, text = "Gerador De Senhas", padx=10, pady=5, font = "Rubix 19")
titl.grid(row = 0, column = 0)


gerar = Button(jan, text = "Gerar", command= funcao, padx=10)
gerar.grid(row = 1, column = 0)

jan.mainloop()