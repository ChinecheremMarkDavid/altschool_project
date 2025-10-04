-- create the necessary tables for the mini-mart analysis

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    join_date DATE NOT NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT FOREIGN KEY REFERENCES Customers(customer_id),
    product_id INT FOREIGN KEY REFERENCES products(product_id),
    quantity INT NOT NULL,
    order_date DATE NOT NULL
);



-- alter the Customers table to add a phone_number column
ALTER TABLE Customers
ADD COLUMN phone_number VARCHAR(15);

