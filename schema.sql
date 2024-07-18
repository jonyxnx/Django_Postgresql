CREATE TABLE paises (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    capital VARCHAR(100),
    poblacion BIGINT,
    area FLOAT,
    is_active BOOLEAN DEFAULT TRUE  /* Borrado lógico */
);

