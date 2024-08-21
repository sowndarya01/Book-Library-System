# This query displays student, book and student_book_issue table's joined data
# Displayed fields are student_id, student_name, book_id, book_title, issue_date, to_be_returned_date, returned_date, days_due

student_book_issue_history_query = '''
    SELECT 
        sbi.student_id AS student_id, 
        s.full_name AS student_name, 
        sbi.book_id AS book_id, 
        b.title AS book_title,
        sbi.issue_date AS issue_date,
        DATE_ADD(issue_date, INTERVAL 7 DAY) AS to_be_returned_date,
        sbi.return_date AS returned_date,
        'Returned' AS days_due
    FROM school.student_book_issue AS sbi 
    INNER JOIN school.student AS s ON s.student_id = sbi.student_id
    INNER JOIN school.book AS b ON b.book_id = sbi.book_id
    WHERE return_date IS NOT NULL

    UNION

    SELECT 
        sbi.student_id AS student_id, 
        s.full_name AS student_name, 
        sbi.book_id AS book_id, 
        b.title AS book_title,
        sbi.issue_date AS issue_date,
        DATE_ADD(issue_date, INTERVAL 7 DAY) AS to_be_returned_date,
        'Not yet returned' AS returned_date,
        DATEDIFF(CURDATE(),DATE_ADD(sbi.issue_date, INTERVAL 7 DAY)) AS days_due
    FROM school.student_book_issue AS sbi 
    INNER JOIN school.student AS s ON s.student_id = sbi.student_id
    INNER JOIN school.book AS b ON b.book_id = sbi.book_id
    WHERE return_date IS NULL AND CURDATE() > DATE_ADD(issue_date, INTERVAL 7 DAY)

    UNION

    SELECT 
        sbi.student_id AS student_id, 
        s.full_name AS student_name, 
        sbi.book_id AS book_id, 
        b.title AS book_title,
        sbi.issue_date AS issue_date,
        DATE_ADD(issue_date, INTERVAL 7 DAY) AS to_be_returned_date,
        'Not yet returned' AS returned_date,
        0 AS days_due
    FROM school.student_book_issue AS sbi 
    INNER JOIN school.student AS s ON s.student_id = sbi.student_id
    INNER JOIN school.book AS b ON b.book_id = sbi.book_id
    WHERE return_date IS NULL AND CURDATE() <= DATE_ADD(sbi.issue_date, INTERVAL 7 DAY);
    '''

student_past_due_date_query = '''
    SELECT 
        sbi.student_id AS student_id, 
        s.full_name AS student_name, 
        sbi.book_id AS book_id, 
        b.title AS book_title,
        sbi.issue_date AS issue_date,
        DATE_ADD(issue_date, INTERVAL 7 DAY) AS to_be_returned_date,
        DATEDIFF(CURDATE(),DATE_ADD(sbi.issue_date, INTERVAL 7 DAY)) AS days_due
    FROM school.student_book_issue AS sbi 
    INNER JOIN school.student AS s ON s.student_id = sbi.student_id
    INNER JOIN school.book AS b ON b.book_id = sbi.book_id
    WHERE return_date IS NULL AND CURDATE() > DATE_ADD(issue_date, INTERVAL 7 DAY);
    '''