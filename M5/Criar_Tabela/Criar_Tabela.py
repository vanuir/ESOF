# 02_create_schema.py
import sqlite3

#conectando...
conn = sqlite3.connect("C:\M5\criando_uma_tabela\clients.db")

#definindo um cursor
cursor = conn.cursor()

#crindo a tabela (schema)
cursor.execute("""
CREATE TABLE clientes (
 id,
 nome,
 idade,
 cpf,
 email,
 fone,
 cidade,
 uf,
 criado_em
);""")
print('Tabela criada com sucesso.')

#desconectando...
conn.close()
