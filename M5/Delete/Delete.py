# 08_delete_data.py
#! python3
import sqlite3

#conectando...
conn = sqlite3.connect("C:\M5\lendo_dados\clients.db")

#definindo um cursor
cursor = conn.cursor()

id_cliente = 2
# excluindo um registro da tabela
cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))
conn.commit()
print('Registro excluido com sucesso.')

#desconectando...
conn.close()

