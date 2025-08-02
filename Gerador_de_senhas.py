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
jan.geometry("270x180")
jan.minsize(245,150)

#Configuração das colunas e linhas
#Colunas
jan.columnconfigure(0, weight = 1)

#Linhas
jan.rowconfigure([0,1,2], weight = 1)

#Entrys
#Label informativa
tk.Label(jan, text = "Insira o tamanho da senha").grid(row = 1, column = 0, pady = 10)
size = tk.Entry(jan) #size of the password
size.grid(row = 2, column = 0, pady = 10)


#Labels
titulo = tk.Label(jan, text = "Gerador De Senhas", padx=10, pady=5, font = "Rubix 19")
senha_label = tk.Label(jan, text = "") #Label da senha


titulo.grid(row = 0, column = 0)
senha_label.grid(row = 4, column = 0, pady = 10)


#Buttons
butao_gerar = tk.Button(jan, text = "Gerar", padx=10, cursor = "hand2", bg = "#32a858",
               command= gerar_senha) #Botão de gerar a senha
butao_gerar.grid(row = 3, column = 0)

jan.mainloop()