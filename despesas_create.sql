CREATE TABLE main_despesas (
    id SERIAL PRIMARY KEY,
    procedimentos_aquisicoes VARCHAR(255) NOT NULL,
    quantidade DECIMAL(10, 2) NOT NULL,
    valor_medio DECIMAL(10, 2) NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL
);
