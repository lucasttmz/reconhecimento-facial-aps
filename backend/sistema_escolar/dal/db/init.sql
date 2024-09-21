CREATE TABLE usuario (
    id_usuario INTEGER PRIMARY KEY,
    codigo VARCHAR(32),
    nome VARCHAR(65),
    tipo INTEGER -- pode ser 0, 1 ou 2
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
    faltas FLOAT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_materia) REFERENCES materia(id_materia)
);

--Scripts para testes
--Materias
INSERT INTO materia (nome, id_professor, data_inicio, data_fim)
VALUES
    ('Banco de Dados', 2, '2023-09-01 08:00:00', '2023-12-15 17:00:00'),
    ('Programação Orientada a Objetos', 2, '2024-01-15 10:00:00', '2024-06-30 18:00:00'),
    ('Redes de Computadores', 2, '2024-09-01 14:00:00', '2025-01-31 16:00:00');

--Usuarios
INSERT INTO usuario (codigo, nome, tipo)
VALUES
    ('ADM123456', 'João da Silva', 3),
    ('PRO123456', 'Maria Pereira', 2),
    ('ALU123456', 'Pedro Santos', 1),
    ('ALU123457', 'Ana Souza', 1),\
    ('ALU123468', 'Carlos Oliveira', 1),
    ('ALU123459', 'Fernanda Gomes', 1);

--Boletins
INSERT INTO boletim (id_usuario, id_materia)
VALUES
    (3, 1),
    (3, 2),
    (4, 1),
    (5, 3),
    (6, 2);