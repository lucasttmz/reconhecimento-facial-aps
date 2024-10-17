/********** CRIAR O ARQUIVO DO BANCO DE DADOS **************
 *                                                         *
 * -- cmd ou powershell --                                 *
 * C:\...\backend\sistema_escolar\dal\db> sqlite3 aps.db   *
 * sqlite3> .read init.sql                                 *
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
INSERT INTO usuario (id_usuario, codigo, nome, tipo)
VALUES
    (NULL, 'C3BFE4A7', 'Joaquim', 1),
    (NULL, 'EBB4A706', 'Raquel', 2),
    (NULL, 'F54CDC5E', 'Felipe', 1),
    (NULL, 'L478D1AE', 'Pedro', 3),
    (NULL, 'R7396D97', 'Zézão', 1),
    (NULL, 'W963D42D', 'Zézinho', 1),
    (NULL, 'C3BFE4A7', 'Joaquim', 1),
    (NULL, 'EBB4A706', 'Raquel', 2),
    (NULL, 'F54CDC5E', 'Felipe', 1),
    (NULL, 'L478D1AE', 'César', 3),
    (NULL, 'C3BFE4A7', 'Jaqueline', 1),
    (NULL, 'EBB4A706', 'Lorena', 2),
    (NULL, 'F54CDC5E', 'Moura', 1),
    (NULL, 'L478D1AE', 'Jean', 3),
    (NULL, 'R7396D97', 'Lucas', 2),
    (NULL, 'W963D42D', 'Raul', 1),
    (NULL, 'C3BFE4A7', 'Lino', 1),
    (NULL, 'EBB4A706', 'Samuel', 2),
    (NULL, 'F54CDC5E', 'Vinicius', 1),
    (NULL, 'L478D1AE', 'Josué', 3);

--Materias
INSERT INTO materia (id_materia, nome, id_professor, data_inicio, data_fim)
VALUES
    (NULL, 'Banco de Dados', 15, '2023-09-01 08:00:00', '2023-12-15 17:00:00'),
    (NULL, 'Programação Orientada a Objetos', 18, '2024-01-15 10:00:00', '2024-06-30 18:00:00'),
    (NULL, 'Redes de Computadores', 18, '2024-09-01 14:00:00', '2025-01-31 16:00:00');

--Boletins
INSERT INTO boletim (id_boletim, id_usuario, id_materia, nota, faltas)
VALUES
    (NULL, 16, 1, 5, 0),
    (NULL, 16, 2, NULL, 3),
    (NULL, 19, 1, NULL, 0),
    (NULL, 19, 3, 10, 0),
    (NULL, 6, 2, 7.5, 3),
    (NULL, 7, 2, NULL, 3),
    (NULL, 9, 1, NULL, 0),
    (NULL, 9, 2, NULL, 5),
    (NULL, 11, 1, NULL, 2),
    (NULL, 11, 2, NULL, 1),
    (NULL, 11, 3, NULL, 0);