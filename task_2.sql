CREATE TABLE Authors (
  author_id INT PRIMARY KEY AUTO_INCREMENT,
  author_name VARCHAR(255)
);

CREATE TABLE Books (
  book_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255),
  author_id INT,
  publisher VARCHAR(255),
  publish_date DATE,
  price DECIMAL(10,2),
  FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE Customers (
  customer_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  customer_name VARCHAR(215)
  email VARCHAR(215),
  address TEXT,
  city VARCHAR(50),
  state VARCHAR(50),   

  zip_code VARCHAR(20),
  country VARCHAR(50),
  phone_number VARCHAR(20)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT,
  order_date DATE,
  shipping_address VARCHAR(255),
  shipping_city VARCHAR(50),
  shipping_state VARCHAR(50),
  shipping_zip_code VARCHAR(20),
  shipping_country VARCHAR(50),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_details (
  order_id INT,
  book_id INT,
  quantity INT,   

  PRIMARY KEY (order_id, book_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id)   

);