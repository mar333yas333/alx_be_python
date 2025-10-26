-- alx_book_store.sql
-- Database for ALX Bookstore

-- Create the database
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

-- AUTHORS TABLE
CREATE TABLE IF NOT EXISTS AUTHORS (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    author_name VARCHAR(215) NOT NULL
);

-- BOOKS TABLE
CREATE TABLE IF NOT EXISTS BOOKS (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES AUTHORS(author_id)
);

-- CUSTOMERS TABLE
CREATE TABLE IF NOT EXISTS CUSTOMERS (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) UNIQUE,
    address TEXT
);

-- ORDERS TABLE
CREATE TABLE IF NOT EXISTS ORDERS (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id)
);

-- ORDER_DETAILS TABLE
CREATE TABLE IF NOT EXISTS ORDER_DETAILS (
    orderdetailid INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES ORDERS(order_id),
    FOREIGN KEY (book_id) REFERENCES BOOKS(book_id)
);

-- Optional sample data
INSERT INTO AUTHORS (author_name) VALUES
('J.K. Rowling'),
('George Orwell'),
('Jane Austen');

INSERT INTO BOOKS (title, author_id, price, publication_date) VALUES
('Harry Potter and the Philosopher''s Stone', 1, 29.99, '1997-06-26'),
('1984', 2, 19.99, '1949-06-08'),
('Pride and Prejudice', 3, 14.50, '1813-01-28');

INSERT INTO CUSTOMERS (customer_name, email, address) VALUES
('Ali', 'ali@example.com', 'Cairo, Egypt'),
('Mona', 'mona@example.com', 'Giza, Egypt');

INSERT INTO ORDERS (customer_id, order_date) VALUES
(1, '2025-10-24'),
(2, '2025-10-25');

INSERT INTO ORDER_DETAILS (order_id, book_id, quantity) VALUES
(1, 1, 2),
(1, 2, 1),
(2, 3, 1);
