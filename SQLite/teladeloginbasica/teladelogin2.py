import customtkinter as ctk
import tkinter as tk
import sqlite3 as sql
import os
#to importando as bibliotecas que eu vou usar
os.system('cls') # to limpando o terminal
con = sql.connect('tabela.db') # to criando uma database
cur = con.cursor() #to definindo uma variavel pra ser o meu cursor(pra codar no tabela)
cur.execute('''
            CREATE TABLE IF NOT EXISTS tabela
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL)
            ''')
# aqui eu criei uma tabela com uma chave primaria id e duas segundarias, uma sendo o usuario e outra a senha, ambas sendo um texto nao nulo
con.commit()
con.close()
# aqui eu so salvei as mudanças na minha tabela
janela = ctk.CTk()
janela.geometry('600x300') 
janela.resizable(False, False)
#criei minha janela
usuario = ctk.CTkLabel(janela, text = 'Usuario')
usuario.pack(pady=10)
entrada_usuario = ctk.CTkEntry(janela, show='')
entrada_usuario.pack(pady=1)
#fiz uma entrada pro usuario
senha = ctk.CTkLabel(janela, text='Senha')
senha.pack(pady=10)
entrada_senha = ctk.CTkEntry(janela, show='*')
entrada_senha.pack(pady=1)
# fiz uma entrada pra senha, mostrando '*'
def login():
    tentativa_usuario = entrada_usuario.get()
    tentativa_senha = entrada_senha.get()
    con = sql.connect('tabela.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM tabela WHERE usuario=? AND senha=?', (tentativa_usuario, tentativa_senha))
    resultado = cur.fetchone()
    con.close()
    if resultado:
        janela_resultado = ctk.CTkToplevel(janela)
        janela_resultado.geometry('300x300')
        texto_nova_tela = ctk.CTkLabel(janela_resultado, text='Login feito com sussexo')
        texto_nova_tela.pack(pady=50)
        janela_resultado.mainloop()
    else:
        janela_resultado = ctk.CTkToplevel(janela)
        janela_resultado.geometry('300x300')
        texto_nova_tela = ctk.CTkLabel(janela_resultado, text='Usuario ou senha incorretos!')
        texto_nova_tela.pack(pady=50)
        janela_resultado.mainloop()
def novo_usuario():
    janela_novo_usuario = ctk.CTkToplevel(janela)
    janela_novo_usuario.geometry('400x300')
    janela_novo_usuario.resizable(False, False)
    janela_novo_usuario.title('Criar novo usuario')
    novo_usuario_textofoda = ctk.CTkLabel(janela_novo_usuario, text='Novo usuario')
    novo_usuario_textofoda.pack(pady=20)
    entrada_novo_usuario = ctk.CTkEntry(janela_novo_usuario, show='')
    entrada_novo_usuario.pack(pady=1)
    senha_nova_foda = ctk.CTkLabel(janela_novo_usuario, text='Nova senha')
    senha_nova_foda.pack(pady=20)
    entrada_nova_senha = ctk.CTkEntry(janela_novo_usuario, show='*')
    entrada_nova_senha.pack(pady=1)
    def salvar_novo_usuario():
        novo_usuario = entrada_novo_usuario.get()
        if novo_usuario.strip() == "":
            alert = tk.Toplevel(janela_novo_usuario)
            alert.geometry('200x100')
            alert_label = tk.Label(alert, text="O nome de usuário não pode estar vazio.")
            alert_label.pack(pady=20)
            alert_button = tk.Button(alert, text="OK", command=alert.destroy)
            return
        nova_senha = entrada_nova_senha.get()
        if nova_senha.strip() == "":
            alert = tk.Toplevel(janela_novo_usuario)
            alert.geometry('200x100')
            alert_label = tk.Label(alert, text="A senha não pode estar vazia.")
            alert_label.pack(pady=20)
            alert_button = tk.Button(alert, text="OK", command=alert.destroy)
            return
        con = sql.connect('tabela.db')
        cur = con.cursor()
        cur.execute('INSERT INTO tabela (usuario, senha) VALUES (?, ?)', (novo_usuario, nova_senha))
        con.commit()
        con.close()
        janela_novo_usuario.destroy()
    botao_salvar = ctk.CTkButton(janela_novo_usuario, text='Salvar', command=salvar_novo_usuario)
    botao_salvar.pack(pady=20)
    janela_novo_usuario.mainloop()
botao_novo_usuario = ctk.CTkButton(janela, text='Criar novo usuario', command=novo_usuario)
botao_novo_usuario.pack(pady=10)
botao_login = ctk.CTkButton(janela, text='login', command=login)
botao_login.pack(pady=20)
janela.mainloop()