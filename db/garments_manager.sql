DROP TABLE IF EXISTS garments;
DROP TABLE IF EXISTS brands;


CREATE TABLE brands (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255)
);

CREATE TABLE garments (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    brand_id INT NOT NULL REFERENCES brands(id),
    description TEXT,
    stock_quantity INT,
    buying_cost FLOAT,
    selling_price FLOAT
);