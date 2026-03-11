import customtkinter as ctk
import tkinter as tk
import sqlite3 as sql
import os 
janela = ctk.CTk()
janela.title("Sistema de Compras")
janela.geometry("800x600")
janela.configure(bg="#f0f0f0")
ctk.set_appearance_mode("system")
con = sql.connect("sistema_de_compras.db")
cursor = con.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)
''')
con.commit()
con.close()

janela.mainloop()