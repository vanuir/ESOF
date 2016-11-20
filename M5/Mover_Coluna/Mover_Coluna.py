# 09_alter_table.py
#! python3
import sqlite3

#conectando...
conn = sqlite3.connect("C:\M5\mova_coluna\clients.db")

#definindo um cursor
cursor = conn.cursor()

# adicionando uma nova coluna na tabela clientes
cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloqueado BOOLEAN;
""")
conn.commit()
print('Novo campo adicionado com sucesso.')


#desconectando...
conn.close()

