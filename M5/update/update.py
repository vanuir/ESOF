# 07_update_data.py
#! python3
import sqlite3

#conectando...
conn = sqlite3.connect("C:\M5\lendo_dados\clients.db")

#definindo um cursor
cursor = conn.cursor()

id_cliente = 1
novo_fone = '11-1000-2014'
novo_criado_em = '2014-06-11'
# alterando os dados da tabela
cursor.execute("""
UPDATE clientes
SET fone = ?, criado_em = ?
WHERE id = ?
""", (novo_fone, novo_criado_em, id_cliente))
conn.commit()

print('Dados atualizados com sucesso.')

#desconectando...
conn.close()

