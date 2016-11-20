BEGIN TRANSACTION;
CREATE TABLE clientes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	idade INTEGER,
	cpf	VARCHAR(11) NOT NULL,
	email TEXT NOT NULL UNIQUE,
	fone TEXT,
	cidade TEXT,
	uf VARCHAR(2) NOT NULL,
	criado_em DATETIME NOT NULL
, bloqueado BOOLEAN);
INSERT INTO "clientes" VALUES(1,'Regis da Silva',35,'12345678901','regis@email.com','(11) 9876-5342','São Paulo','SP','2014-07-30 11:23:00.199000',NULL);
INSERT INTO "clientes" VALUES(2,'Lincoln',19,'11111111111','lincolm@mail.com','1122223333','uberlandia','mg','2016-11-16 14:49:17.330460',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',3);
COMMIT;
