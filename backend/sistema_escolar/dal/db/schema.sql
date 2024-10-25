/********** CRIAR O SCHEMA DO BANCO DE DADOS ***************
 *                                                         *
 * -- cmd ou powershell --                                 *
 * C:\...\backend\sistema_escolar\dal\db> sqlite3 aps.db   *
 * sqlite3> .read schema.sql                               *
 *                                                         *
 ***********************************************************/

CREATE TABLE usuario (
    id_usuario INTEGER PRIMARY KEY,
    codigo VARCHAR(32),
    nome VARCHAR(65),
    tipo INTEGER -- pode ser 1, 2 ou 3
);

CREATE TABLE materia (
    id_materia INTEGER PRIMARY KEY,
    nome VARCHAR(65),
    id_professor INTEGER,
    data_inicio DATETIME,
    data_fim DATETIME
);

CREATE TABLE boletim (
    id_boletim INTEGER PRIMARY KEY,
    id_usuario INTEGER,
    id_materia INTEGER,
    nota FLOAT,
    faltas INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_materia) REFERENCES materia(id_materia)
);