import tkinter as tk
import random


def mostrar_senha():
    label_resultado.delete(0.0, "end")

    try:
        tamanho = int(tamanho_entry.get())#Obtêm o tamnho pretendido
        if 0 < tamanho < 26:
                senha = gerar_senha(tamanho)#Senha gerada

                label_resultado.config(fg = "Black", font = "Roboto 10 bold")
                label_resultado.insert("end", senha)

        else:#Se não for positivo menor que 31
                label_resultado.config(fg = "#b55609",font = ("Roboto", 10, "bold") )
                label_resultado.insert("end","Digite um número de 0 a 25")

    except:
        label_resultado.config(fg = "red3")
        label_resultado.insert("end", "Erro")


def gerar_senha(tamanho: int) -> str:#Gera a senha
    caracteres = ""

    if var_maiusculas.get():
        caracteres +="ABCDEFGHIJKLMNOPKRSTUVWXYZ"
    if var_minusculas.get():#Se dentro da string for True
        caracteres += "abcdefghijklmnopqrstuvwxyz"
    if var_digitos.get():
        caracteres += "0123456789"
    if var_simbolos.get():
        caracteres += "@#£&$"


    senha = "".join(random.choice(caracteres) for _ in range(tamanho))

    return senha


#################################################################

jan = tk.Tk()

jan.title("Gerador de senhas")
jan.geometry("300x300")
#jan.minsize(355,255)
jan.config(bg = "#CED7E0")

#Configuração de linhas e colunas da janela
jan.rowconfigure(0, weight = 3)
jan.rowconfigure(1, weight = 25)

jan.columnconfigure(0, weight = 1)


#Frames- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_1 = tk.Frame(jan, bg = "#32a858")
frame_2 = tk.Frame(jan)

#Configuração dos frames
#Frame1
frame_1.rowconfigure(0, weight = 1)
frame_1.columnconfigure(0, weight = 1)

#Frame2
frame_2.columnconfigure(0, weight = 1)

#Exibição dos frames
frame_1.grid(row = 0, column = 0, sticky = "nswe")
frame_2.grid(row = 1, column = 0, sticky = "nswe", pady = (2,0))


#Título - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
titulo = tk.Label(frame_1, text = "Gerador De Senhas",font = ("Helvetica", 16, "bold"),
                  bg = "#32a858",anchor = "center")

titulo.grid(row = 0, column = 0,sticky = "nswe", pady = 4)

#Entrys - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
tk.Label(frame_2, text = "Insira a quantidade de caracteres",
         font = ("Garamond", 10, "bold")).grid(row = 0, column = 0, pady = (8,0),padx = (5,0), sticky = "w")#Label informativo
tamanho_entry = tk.Entry(frame_2, width = 10) #Tamanho a senha

tamanho_entry.grid(row = 1, column = 0,padx = (7,0), pady = 5, ipady = 3, sticky = "w")


#Checkbuttons -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Variaveis de controlo
var_maiusculas = tk.BooleanVar()#Variável de controlo da checkbutton de letras maiúsculas
var_minusculas = tk.BooleanVar()#Variável de controlo da checkbutton de letras minúsculas
var_digitos = tk.BooleanVar()#Variável de controlo da checkbutton dos digitos
var_simbolos = tk.BooleanVar()#Variável de controlo da checkbutton dos símbolos


check_maiusculas = tk.Checkbutton(frame_2, variable = var_maiusculas, text = "Letras maiúsculas")
check_minusculas = tk.Checkbutton(frame_2, variable = var_minusculas, text = "Letas minúsculas")
check_digitos = tk.Checkbutton(frame_2, variable = var_digitos, text = "Digitos")
check_simbolos = tk.Checkbutton(frame_2, variable = var_simbolos, text = "Símbolos:@# ...")


check_maiusculas.grid(row = 2, column = 0, sticky = "w", padx = (6,0), pady = 10)
check_minusculas.grid(row = 3, column = 0, sticky = "w", padx = (6,0))
check_digitos.grid(row = 2, column = 0,padx = (83,0))
check_simbolos.grid(row = 3, column = 0, padx = (127,0))

check_minusculas.select()

#Labels- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
label_resultado = tk.Text(frame_2,font = "Roboto 10 bold", width = 32, height = 1) #Label da senha

label_resultado.grid(row = 6, column = 0, pady = 10)

#Buttons- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
butao_gerar = tk.Button(frame_2, text = "Gerar", padx=25, cursor = "hand2", bg = "#32a858",
               command= mostrar_senha) #Botão de gerar a senha
butao_gerar.grid(row = 4, column = 0,pady = 15, sticky = "w", padx = (100,0))
jan.mainloop()