/********** CRIAR O ARQUIVO DO BANCO DE DADOS **************
 *                                                         *
 * -- cmd ou powershell --                                 *
 * C:\[...]\backend\sistema_escolar\dal\db> sqlite3 aps.db *
 * sqlite3> aps.db < init.sql                              *
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

--Scripts para testes
--Usuarios
INSERT INTO usuario (id_usuario, codigo, nome, tipo)
VALUES
    (NULL, 'ADM123456', 'João da Silva', 3),
    (NULL, 'PRO123456', 'Maria Pereira', 2),
    (NULL, 'ALU123456', 'Pedro Santos', 1),
    (NULL, 'ALU123457', 'Ana Souza', 1),
    (NULL, 'ALU123468', 'Carlos Oliveira', 1),
    (NULL, 'ALU123459', 'Fernanda Gomes', 1);

--Materias
INSERT INTO materia (id_materia, nome, id_professor, data_inicio, data_fim)
VALUES
    (NULL, 'Banco de Dados', 2, '2023-09-01 08:00:00', '2023-12-15 17:00:00'),
    (NULL, 'Programação Orientada a Objetos', 2, '2024-01-15 10:00:00', '2024-06-30 18:00:00'),
    (NULL, 'Redes de Computadores', 2, '2024-09-01 14:00:00', '2025-01-31 16:00:00');

--Boletins
INSERT INTO boletim (id_boletim, id_usuario, id_materia, nota, faltas)
VALUES
    (NULL, 3, 1, 5, 0),
    (NULL, 3, 2, NULL, 3),
    (NULL, 4, 1, NULL, 0),
    (NULL, 5, 3, 10, 0),
    (NULL, 6, 2, 7.5, 3);