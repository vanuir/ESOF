# 04_create_data_sql.py
#! python3
import sqlite3

#conectando...
conn = sqlite3.connect("C:\M5\inserindo_um_registro_definido\clients.db")

#definindo um cursor
cursor = conn.cursor()

# solicitando os dados ao usuario
p_nome = input('Nome: ')
p_idade = input('Idade: ')
p_cpf = input('CPF: ')
p_email = input('Email: ')
p_fone = input('Fone: ')
p_cidade = input('Cidade: ')
p_uf = input('UF: ')
p_criado_em = input('Criado em (yyyy-mm-dd): ')

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_uf, p_criado_em))

conn.commit()

print('Dados inseridos com sucesso.')

#desconectando...
conn.close()

