# 06_read_data.py
#! python3
import sqlite3

#conectando...
conn = sqlite3.connect("C:\M5\lendo_dados\clients.db")

#definindo um cursor
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM clientes;
""")


for linha in cursor.fetchall():
 print(linha)


#desconectando...
conn.close()

