DROP TABLE IF EXIST school.student_book_issue;
CREATE TABLE school.student_book_issue (
	issue_id INTEGER NOT NULL AUTO_INCREMENT , -- Unique issue_id that is auto-generated and auto-incremented
	student_id VARCHAR(5) NOT NULL , -- The student_id of the student who borrowerd the book
	book_id VARCHAR(7) NOT NULL , -- The book_id of the book the student borrowed
	issue_date DATE NOT NULL , -- The date when the book was issued to the student
    return_date DATE DEFAULT NULL , -- The date the book was returned by the student
    PRIMARY KEY(issue_id) -- issue_id is made the primary key
);
