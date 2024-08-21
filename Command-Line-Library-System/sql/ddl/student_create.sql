DROP TABLE IF EXIST school.student;
CREATE TABLE school.student (
	student_id INTEGER NOT NULL AUTO_INCREMENT , -- Unique student_id that is auto-generated and auto-incremented
	full_name VARCHAR(40) NOT NULL ,
	class VARCHAR(2) NOT NULL ,
	dob VARCHAR(10) NOT NULL ,
    PRIMARY KEY(student_id) -- student_id is made the primary key
);
