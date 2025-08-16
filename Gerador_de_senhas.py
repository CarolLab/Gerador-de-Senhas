import tkinter as tk
import string
import random


def mostrar_senha():
    label_resultado.config(text = "")#Limpar o campo de texto oa gerar uma nova senha
    label_erro.config(text = "")

    try:
        tamanho = int(tamanho_entry.get())#Obtêm o tamnho pretendido
        if 0 < tamanho < 26:
            senha = gerar_senha(tamanho)#Senha gerada

            label_resultado.config(fg = "Black", font = "Roboto 10 bold",
                                   text = senha)

        else:#Se não for positivo menor que 31
            label_erro.config(text ="Digite um número de 0 a 25",fg = "#b55609", font = ("Roboto", 10, "bold"))

    except ValueError:
        label_erro.config(text = "Erro", fg = "red3")

    except IndexError:
        label_erro.config(text = "Selecione os caracteres da senha", fg = "red3", font = ("Roboto", 10, "bold"))


def gerar_senha(tamanho: int) -> str:#Gera a senha
    caracteres = ""

    #Verificar as opções selecionadas

    if var_maiusculas.get():#Se o valor de var_maiusculas for True
        caracteres += string.ascii_uppercase
    if var_minusculas.get():
        caracteres += string.ascii_lowercase
    if var_digitos.get():
        caracteres += string.digits
    if var_simbolos.get():
        caracteres += "@#£&$"

    #Sortea os caracteres e junta-os na variável senha
    senha = "".join([random.choice(caracteres) for _ in range(tamanho)])

    return senha


#################################################################

jan = tk.Tk()

jan.title("Gerador de senhas")
jan.geometry("300x300")
jan.minsize(300,300)
jan.config(bg = "#CED7E0")

#Configuração de linhas e colunas da janela
jan.rowconfigure(0, weight = 3)
jan.rowconfigure(1, weight = 25)

jan.columnconfigure(0, weight = 1)


#Frames- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_1 = tk.Frame(jan, bg = "#EAF4FB")
frame_2 = tk.Frame(jan, bg = "#f2f5f7")

#Configuração dos frames
#Frame1
frame_1.rowconfigure(0, weight = 1)
frame_1.columnconfigure(0, weight = 1)

#Frame2
frame_2.columnconfigure(0, weight = 1)
frame_2.rowconfigure([0,1,2,3,4,5,6], weight = 1)

#Exibição dos frames
frame_1.grid(row = 0, column = 0, sticky = "nswe")
frame_2.grid(row = 1, column = 0, sticky = "nswe", pady = (2,0))


#Título - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
titulo = tk.Label(frame_1, text = "Gerador De Senhas",font = ("Helvetica", 16, "bold"),
                  bg = "#EAF4FB",fg = "#1C2C4C",anchor = "center")

titulo.grid(row = 0, column = 0,sticky = "nswe", pady = 4)

#Entrys - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
tk.Label(frame_2, text = "Insira a quantidade de caracteres",bg = "#f2f5f7",
         font = ("Garamond", 10, "bold")).grid(row = 0, column = 0, pady = (8,0),padx = (5,0), sticky = "w")#Label informativo
tamanho_entry = tk.Entry(frame_2, width = 10, relief = "groove", bd = 2) #Tamanho a senha

tamanho_entry.grid(row = 1, column = 0,padx = (7,0), pady = 5, ipady = 3, sticky = "w")


#Checkbuttons -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Variaveis de controlo
var_maiusculas = tk.BooleanVar()#Variável de controlo da checkbutton de letras maiúsculas
var_minusculas = tk.BooleanVar()#Variável de controlo da checkbutton de letras minúsculas
var_digitos = tk.BooleanVar()#Variável de controlo da checkbutton dos digitos
var_simbolos = tk.BooleanVar()#Variável de controlo da checkbutton dos símbolos


check_maiusculas = tk.Checkbutton(frame_2, variable = var_maiusculas, text = "Letras maiúsculas", bg = "#f2f5f7")
check_minusculas = tk.Checkbutton(frame_2, variable = var_minusculas, text = "Letas minúsculas",bg = "#f2f5f7")
check_digitos = tk.Checkbutton(frame_2, variable = var_digitos, text = "Digitos",bg = "#f2f5f7")
check_simbolos = tk.Checkbutton(frame_2, variable = var_simbolos, text = "Símbolos:@# ...",bg = "#f2f5f7")


check_maiusculas.grid(row = 2, column = 0, sticky = "w", padx = (6,0), pady = 10)
check_minusculas.grid(row = 3, column = 0, sticky = "w", padx = (6,0))
check_digitos.grid(row = 2, column = 0,sticky = "e",padx = (0,49))
check_simbolos.grid(row = 3, column = 0, sticky = "e",padx = (0,5))

check_minusculas.select()


label_resultado = tk.Label(frame_2,font = "Roboto 10 bold", width = 32, height = 1,bg = "White",
                          relief = "groove", bd = 2) #Label da senha
label_erro = tk.Label(frame_2, text = "")

label_resultado.grid(row = 6, column = 0, pady = 10)
label_erro.grid(row = 5, column =0)
#Buttons- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
butao_gerar = tk.Button(frame_2, text = "Gerar", padx=25, cursor = "hand2", bg = "#2fad58",bd = 3,
               relief = "raised",overrelief="solid",command= mostrar_senha) #Botão de gerar a senha
butao_gerar.grid(row = 4, column = 0,pady = 15, padx = (100,0),ipadx = 4, sticky = "w")
jan.mainloop()