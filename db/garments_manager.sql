DROP TABLE IF EXISTS images;
DROP TABLE IF EXISTS garments;
DROP TABLE IF EXISTS types;
DROP TABLE IF EXISTS brands;


CREATE TABLE brands (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255)
);

CREATE TABLE types (
    id SERIAL PRIMARY KEY, 
    type VARCHAR(255)
);



CREATE TABLE garments (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    brand_id INT NOT NULL REFERENCES brands(id),
    type_id INT NOT NULL REFERENCES types(id),
    description TEXT,
    stock_quantity INT,
    buying_cost FLOAT,
    selling_price FLOAT
);

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    name TEXT,
    garment_id INT NOT NULL REFERENCES garments(id)
);
