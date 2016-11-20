# Conectando e desconectando do Banco
# connect_db.py
# 01_create_db.py

import sqlite3

conn = sqlite3.connect("C:\M5\conectando_e_desconectando_do_banco\clientes.db")
conn.close()
