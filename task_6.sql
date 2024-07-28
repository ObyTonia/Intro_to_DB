-- Ensure we are using the correct database
USE alx_book_store;

INSERT INTO customers (customer_id, first_name, last_name, email, address)
VALUES (2, 'Blessing', 'Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
       (3, 'Obed', 'Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
       (4, 'Nehemiah', 'Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');
-- Insert multiple rows into the customers table
INSERT INTO customers (customer_id, customer_name, email, address)
VALUES
    (customer_id= 2 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
    (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
    (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');