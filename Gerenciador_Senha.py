import random
from tkinter import *



def senha():
    lower_case = "qwertyuiopasdfghjklzxcvbnm"
    upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
    number = "123456789"
    simbols = "@#$%&*!"



    for_pass = lower_case + upper_case + number + simbols
    tam_senha= 15

    password = "".join(random.sample(for_pass,tam_senha))

    senha= f''''
    Senha: {password}'''

    text_res['text'] = senha





janela= Tk()

janela.title("Gerenciador de Senhas")
titulo=Label(janela,text="Gerenciador de Senha")
titulo.grid(column=100, row=100, padx=10, pady=10)
botao = Button(janela,text="Gerar uma Senha", command=senha)
botao.grid(column=100, row=200)
text_res = Label(janela, text="")
text_res.grid(column=100, row=300)

janela = mainloop()



