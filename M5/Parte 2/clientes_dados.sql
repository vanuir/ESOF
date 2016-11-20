def inserir_com_lista(self):
 # criando uma lista de dados
 lista = [('Agenor de Sousa', 23, '12345678901', 'agenor@email.com',
 '(10) 8300-0000', 'Salvador', 'BA', '2014-07-29
11:23:01.199001'),
 ('Bianca Antunes', 21, '12345678902', 'bianca@email.com',
 '(10) 8350-0001', 'Fortaleza', 'CE', '2014-07-28
11:23:02.199002'),
 ('Carla Ribeiro', 30, '12345678903', 'carla@email.com',
 '(10) 8377-0002', 'Campinas', 'SP', '2014-07-28
11:23:03.199003'),
 ('Fabiana de Almeida', 25, '12345678904', 'fabiana@email.com',
 '(10) 8388-0003', 'São Paulo', 'SP', '2014-07-29
11:23:04.199004'),
 ]
 try:
 self.db.cursor.executemany("""
 INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf,
criado_em)
 VALUES (?,?,?,?,?,?,?,?)
 """, lista)
 # gravando no bd
 self.db.commit_db()
 print("Dados inseridos da lista com sucesso: %s registros." %
 len(lista))
 except sqlite3.IntegrityError:
 print("Aviso: O email deve ser único.")
 return False