import tkinter as tk
import string
import random
import pyperclip as pycp

def copiar(senha):
    if senha:
        pycp.copy(senha)
        botao_copiar.config(text = "Copiado!", bg = "lightgreen")
        jan.after(2000, lambda: botao_copiar.config(text = "Copiar", bg = "#CED7E0"))



def mostrar_senha():
    var_senha.set("")#Limpar o campo de texto oa gerar uma nova senha
    var_erro.set("")

    try:
        tamanho = int(var_spinbox_scale.get())#Obtêm o tamnho pretendido
        if 2 < tamanho < 26:
            senha = gerar_senha(tamanho)#Senha gerada

            var_senha.set(senha)


        else:#Se não for positivo menor que 31
            label_erro.config(fg = "#b55609")
            var_erro.set("Digite um número de 3 a 25")

    except ValueError:
        label_erro.config(fg = "red3")
        var_erro.set("Digite um número de 3 a 25")

    except IndexError:
        label_erro.config(fg = "red3")
        var_erro.set("Selecione os caracteres da senha")


def gerar_senha(tamanho: int) -> str:#Gera a senha
    caracteres = ""

    #Verificar as opções selecionadas

    if var_simbolos.get():
        caracteres += "@#£&$"
    if var_digitos.get():
        caracteres += string.digits
    if var_maiusculas.get():#Se o valor de var_maiusculas for True
        caracteres += string.ascii_uppercase
    if var_minusculas.get():
        caracteres += string.ascii_lowercase


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

#Fontes- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
bg_frame2 = "#f2f5f7" #Usado em no background dos elementos do frame2


#Frames- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_1 = tk.Frame(jan, bg = "#EAF4FB")
frame_2 = tk.Frame(jan, bg = bg_frame2)

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


#Variáveis de controlo dos checkbuttons
var_maiusculas = tk.BooleanVar()
var_minusculas = tk.BooleanVar()
var_digitos = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

var_spinbox_scale = tk.IntVar()
var_senha = tk.StringVar() #Variável de controlo do label da senha
var_erro = tk.StringVar() #Variável de controlo do label de erro


#Entrys - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
tk.Label(frame_2, text = "Insira a quantidade de caracteres",bg =  bg_frame2,
         font = ("Garamond", 10, "bold")).grid(row = 0, column = 0, pady = (8,0),padx = (5,0), sticky = "w")#Label informativo
tamanho_spinbox = tk.Spinbox(frame_2, from_ = 3, to = 25, wrap = True,
                             width = 10, relief = "groove", bd = 2, textvariable = var_spinbox_scale) #Tamanho a senha

tamanho_spinbox.grid(row = 1, column = 0,padx = (7,0), pady = 5, ipady = 3, sticky = "w")


#Checkbuttons -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
check_maiusculas = tk.Checkbutton(frame_2, variable = var_maiusculas, text = "Letras maiúsculas", bg = bg_frame2,
                                  activebackground = bg_frame2)
check_minusculas = tk.Checkbutton(frame_2, variable = var_minusculas, text = "Letas minúsculas",bg = bg_frame2,
                                  activebackground = bg_frame2)
check_digitos = tk.Checkbutton(frame_2, variable = var_digitos, text = "Dígitos",bg = bg_frame2,
                               activebackground = bg_frame2)
check_simbolos = tk.Checkbutton(frame_2, variable = var_simbolos, text = "Símbolos:@# ...",bg = bg_frame2,
                                activebackground= bg_frame2)


check_maiusculas.grid(row = 2, column = 0, sticky = "w", padx = (6,0), pady = 10)
check_minusculas.grid(row = 3, column = 0, sticky = "w", padx = (6,0))
check_digitos.grid(row = 2, column = 0,sticky = "e",padx = (0,49))
check_simbolos.grid(row = 3, column = 0, sticky = "e",padx = (0,5))
check_minusculas.select()


label_senha = tk.Label(frame_2,font = "Roboto 10 bold", width = 23, height = 1,
                          relief = "groove", bd = 2, textvariable = var_senha) #Label da senha

label_erro = tk.Label(frame_2,bg = bg_frame2,font = ("TkDefaultFont",10,"bold"),
                      textvariable = var_erro)

label_senha.grid(row = 5, column = 0, pady = (2,1), padx = (5,0),sticky = "nsw")
label_erro.grid(row = 6, column =0, pady = (0,2))


#Scale - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
scale = tk.Scale(frame_2,from_ = 3, to = 25, orient = "horizontal", length= 120,
                 troughcolor = "#CED7E0",variable = var_spinbox_scale)
scale.grid(row = 1, column = 0,pady = (0,13), padx = (60,0))


#Botões- - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
botao_gerar = tk.Button(frame_2, text = "Gerar", padx=25, cursor = "hand2", bg = "#2fad58",bd = 2,
                        activebackground = "lightgreen",relief = "raised",overrelief="solid",
                        command= mostrar_senha) #Botão de gerar a senha

botao_copiar = tk.Button(frame_2, bg = "#CED7E0",text = "Copiar",width = 10, relief = "groove", bd = 2,
                         command = lambda: copiar(var_senha.get()))

botao_gerar.grid(row = 4, column = 0,pady = (4,12), padx = (100,0),ipadx = 4, sticky = "w")
botao_copiar.grid(row = 5, column = 0, padx = (2,20),sticky = "nse")


#Loop
jan.mainloop()