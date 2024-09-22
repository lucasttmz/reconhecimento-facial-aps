CREATE TABLE usuario (
    id_usuario INTEGER PRIMARY KEY,
    codigo VARCHAR(32),
    nome VARCHAR(65),
    tipo INTEGER(1)
);

CREATE TABLE materia (
    id_materia INTEGER PRIMARY KEY,
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