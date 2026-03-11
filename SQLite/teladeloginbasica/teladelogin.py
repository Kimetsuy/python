import customtkinter as ctk
import tkinter as tk
import sqlite3
janela = ctk.CTk()
janela.title("Tela de Login")
janela.geometry("600x500")
janela.configure(bg="#f0f0f0")
ctk.set_appearance_mode("system")
con = sqlite3.connect('usuarios.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS usuarios
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                senha TEXT NOT NULL)''')
con.commit()
con.close()
def abrir_tela_novo_usuario():
    nova_janela = ctk.CTkToplevel(janela)
    nova_janela.title("Adicionar Novo Usuário")
    nova_janela.geometry("400x300")
    label_novo_usuario = ctk.CTkLabel(nova_janela, text="Novo Usuário:")
    label_novo_usuario.pack(pady=10)
    entrada_novo_usuario = ctk.CTkEntry(nova_janela, width=200)
    entrada_novo_usuario.pack(pady=5)
    label_nova_senha = ctk.CTkLabel(nova_janela, text="Nova Senha:")
    label_nova_senha.pack(pady=10)
    entrada_nova_senha = ctk.CTkEntry(nova_janela, width=200, show="*")
    entrada_nova_senha.pack(pady=5)
    def salvar_novo_usuario():
        usuario = entrada_novo_usuario.get()
        senha = entrada_nova_senha.get()
        adicionar_usuario(usuario, senha)
        nova_janela.destroy()
    botao_salvar = ctk.CTkButton(nova_janela, text="Salvar", command=salvar_novo_usuario)
    botao_salvar.pack(pady=20)
def adicionar_usuario(usuario, senha):
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
    conexao.commit()
    conexao.close()
def tema_claro():
    ctk.set_appearance_mode("light")
def tema_escuro(): 
    ctk.set_appearance_mode("dark")
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        label_resultado.configure(text="Login bem-sucedido!", fg="green")
    else:
        label_resultado.configure(text="Usuário ou senha incorretos.", fg="red")
label_usuario = ctk.CTkLabel(janela, text="Usuário:")
label_usuario.pack(pady=10)
entrada_usuario = ctk.CTkEntry(janela, width=200)
entrada_usuario.pack(pady=5)
label_senha = ctk.CTkLabel(janela, text="Senha:")
label_senha.pack(pady=10)
entrada_senha = ctk.CTkEntry(janela, width=200, show="*")
entrada_senha.pack(pady=5)
botao_login = ctk.CTkButton(janela, text="Login", command=verificar_login)
botao_login.pack(pady=20)
label_resultado = ctk.CTkLabel(janela, text="")
label_resultado.pack(pady=10)
botao_login_novo_usuario = ctk.CTkButton(janela, text="Adicionar Novo Usuário", command=abrir_tela_novo_usuario)
botao_login_novo_usuario.pack(pady=5)
frame_tema = ctk.CTkFrame(janela)
janela.mainloop()
