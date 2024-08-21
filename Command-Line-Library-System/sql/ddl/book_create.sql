DROP TABLE IF EXIST school.book;
CREATE TABLE school.book (
	book_id INTEGER NOT NULL AUTO_INCREMENT , -- Unique book_id that is auto-generated and auto-incremented
	title VARCHAR(100) NOT NULL ,
	author VARCHAR(40) ,
	published_year VARCHAR(4) ,
    PRIMARY KEY(book_id) -- book_id is made the primary key
);
