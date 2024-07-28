 -- USE alx_book_store;

CREATE TABLE authors (
  author_id INT PRIMARY KEY AUTO_INCREMENT,
  author_name VARCHAR(255)
);

CREATE TABLE books (
  book_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255),
  author_id INT,
  publisher VARCHAR(255),
  publish_date DATE,
  price DECIMAL(10,2),
  FOREIGN KEY (author_id) REFERENCES authors(author_id)
);