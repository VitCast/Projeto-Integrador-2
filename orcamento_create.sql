CREATE TABLE main_orcamento (
    id SERIAL PRIMARY KEY,
    categoria VARCHAR(255) NOT NULL,
    previsao DECIMAL(10, 2) NOT NULL,
    despesas DECIMAL(10, 2) NOT NULL,
    porct_utilizado DECIMAL(5, 2) NOT NULL,
    anotacoes VARCHAR(255)
);
