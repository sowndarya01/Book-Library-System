import display_strings
import book_issue_query

def issue_book_to_student(mycursor, mydb):

    student_id = input('Enter student ID: ')
    book_id = input('Enter book ID: ')

    # Check if student_id and book_id are numeric values
    if ( not student_id.isnumeric() or not book_id.isnumeric() ):
        print('One if the ID you have entered is not numeric and is incorrect.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Checks if student with student_id exist
    check_if_student_exists_query = "SELECT * FROM student WHERE student_id=%s;"
    val = (student_id,)
    mycursor.execute(check_if_student_exists_query, val)
    if (mycursor.rowcount == 0):
        print('Student with student_id',student_id,'does not exist.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Checks if book with book_id exist
    check_if_book_exists_query = "SELECT * FROM book WHERE book_id=%s;"
    val = (book_id,)
    mycursor.execute(check_if_book_exists_query, val)
    if (mycursor.rowcount == 0):
        print('Book with book_id',book_id,'does not exist.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Checks if student has a pending book
    student_book_pending_query = "SELECT * FROM student_book_issue WHERE student_id=%s AND return_date IS NULL;"
    val = (student_id,)
    mycursor.execute(student_book_pending_query, val)
    if (mycursor.rowcount != 0):
        print('Student already has a book pending to be returned.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Checks if book is available
    check_book_availability_query = "SELECT * FROM student_book_issue WHERE book_id=%s AND return_date IS NULL;"
    val = (book_id,)
    mycursor.execute(check_book_availability_query, val)
    if (mycursor.rowcount != 0):
        print('The book is taken by another user.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Inserts details to database
    insert_student_book_issue_query = "INSERT INTO student_book_issue (student_id, book_id, issue_date) VALUES (%s, %s, CURDATE())"
    val = (student_id, book_id)
    mycursor.execute(insert_student_book_issue_query, val)
    print(mycursor.rowcount, "record inserted.") # mycursor contains the rowcount field which has the count of rows affected

    mydb.commit() # Saves all changes to database

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see


def returning_book(mycursor, mydb):

    student_id = input('Enter student ID: ')
    book_id = input('Enter book ID: ')

    # Check if student_id book_id pair exists
    student_book_id_query = "SELECT 1 FROM student_book_issue WHERE student_id=%s AND book_id=%s AND return_date IS NULL "
    val = (student_id, book_id)
    mycursor.execute(student_book_id_query, val)
    if (mycursor.rowcount == 0):
        print('Incorrect student ID or book ID. No such combination found.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Adds return date to the entry
    update_student_book_issue_query = "UPDATE student_book_issue SET return_date=CURDATE() WHERE student_id=%s AND book_id=%s AND return_date IS NULL;"
    val = (student_id, book_id)
    mycursor.execute(update_student_book_issue_query, val)
    print(mycursor.rowcount, "record updated.")

    mydb.commit() # Saves all changes to database

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see


def display_issue_history(mycursor, mydb):

    # Displays all student book issue history
    student_book_issue_history_query = book_issue_query.student_book_issue_history_query
    mycursor.execute(student_book_issue_history_query)
    history = mycursor.fetchall()

    print(display_strings.issue_history_details_header, end='') # Displays a issue history heading. We add an end='' since the issue_history_details_footer already has a new line

    for row in history:
        
        # Extracting issue history data from tuple
        student_id = row[0]
        student_name = row[1]
        book_id = row[2]
        book_title = row[3]
        issue_date = row[4]
        to_be_returned_date = row[5]
        returned_date = row[6]
        days_due = row[7]

        # Prints row of issue history in an organized row
        print('| %10s | %25s | %7s | %20s | %10s | %19s | %16s | %8s |' % (student_id, student_name, book_id, book_title, issue_date, to_be_returned_date, returned_date, days_due))

    print(display_strings.issue_history_details_footer) # Displays a issue history details footer

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see


def display_students_past_due_date(mycursor, mydb):

    # Displays students past due date
    student_past_due_date_query = book_issue_query.student_past_due_date_query
    mycursor.execute(student_past_due_date_query)
    student_past_due = mycursor.fetchall()

    print(display_strings.students_past_due_date_header, end='') # Displays a students past due date heading. We add an end='' since the issue_history_details_footer already has a new line

    for row in student_past_due:
        
        # Extracting students past due date data from tuple
        student_id = row[0]
        student_name = row[1]
        book_id = row[2]
        book_title = row[3]
        issue_date = row[4]
        to_be_returned_date = row[5]
        days_due = row[6]

        # Prints row of students past due date in an organized row
        print('| %10s | %25s | %7s | %20s | %10s | %19s | %8s |' % (student_id, student_name, book_id, book_title, issue_date, to_be_returned_date, days_due))

    print(display_strings.students_past_due_date_footer) # Displays a students past due date footer

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
