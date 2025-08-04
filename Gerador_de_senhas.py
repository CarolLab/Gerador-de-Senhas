import tkinter as tk
import random

def mostrar_senha():
    try:
        tamanho = int(tamanho_entry.get())#Obtêm o tamnho pretendido
        if 0 < tamanho < 31:
            senha = gerar_senha(tamanho)#Senha gerada
            label_resultado.config(text = senha, fg = "Black", font = "Roboto 10 bold")
        else:
            label_resultado.config(text = f"Insira um número positivo\nmenor que 31", fg = "#b55609")
    except:
        label_resultado.config(text = "Error", fg = "red3")


def gerar_senha(tamanho: int) -> str:#Gera a senha
        caracteres = "aAbcCdDeEfghHijklmnNpPqrsStTuvwxyz123456789#$%*@"
        senha = ""

        for _ in range(tamanho):
            senha += random.choice(caracteres)

        return senha


#################################################################

jan = tk.Tk()

jan.title("Gerador de senhas")
jan.geometry("355x255")
jan.minsize(355,255)

#Configuração de linhas e colunas da janela
jan.rowconfigure(0, weight = 3)
jan.rowconfigure(1, weight = 24)

jan.columnconfigure(0, weight = 1)


#Frames- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_1 = tk.Frame(jan,bg = "DarkOliveGreen3")
frame_2 = tk.Frame(jan)

#Configuração dos frames
#Frame1
frame_1.rowconfigure(0, weight = 1)
frame_1.columnconfigure(0, weight = 1)

#Frame2
frame_2.columnconfigure(0, weight = 1)

#Exibição dos frames
frame_1.grid(row = 0, column = 0, sticky = "nswe")
frame_2.grid(pady = 10,row = 1, column = 0, sticky = "nswe")


#Entrys - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
tk.Label(frame_2, text = "Insira um tamanho para a senha",
         font = ("Garamond", 10, "bold")).grid(row = 1, column = 0, pady = 10)#Label informativo
tamanho_entry = tk.Entry(frame_2) #Tamanho a senha

tamanho_entry.grid(row = 2, column = 0, pady = 8, ipady = 3)


#Labels- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
titulo = tk.Label(frame_1, text = "Gerador De Senhas",font = ("Rubix", 16, "bold"),
                  bg = "DarkOliveGreen3")#Título
label_resultado = tk.Label(frame_2, text = "", font = "Roboto 10 bold") #Label da senha

titulo.grid(pady = 8,row = 0, column = 0,sticky = "nswe")
label_resultado.grid(row = 4, column = 0, pady = 10)

#Buttons- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
butao_gerar = tk.Button(frame_2, text = "Gerar", padx=10, cursor = "hand2", bg = "#32a858",
               command= mostrar_senha) #Botão de gerar a senha
butao_gerar.grid(pady = 8,row = 3, column = 0)

jan.mainloop()