from re import A
import display_strings

dbcursor = None # Stores the database cursor
db = None # Stores the database connection

# Function checks if entered student data is valid or not (Utitlity function)
def is_student_data_correct(student_data):

    (student_name, student_class, student_dob) = student_data # Unpack tuple student data

    # Student name validation
    # Checks the length of the student full_name
    if (len(student_name) > 40 or len(student_name) == 0):
        print('Please enter a name with at least 1 to 40 characters. ')
        return False

    # Checks if student name contains characters other than alphabets, spaces and periods
    if (not student_name != '' and all(chr.isalpha() or chr.isspace() or chr == '.' for chr in student_name)):
        print('Student can only have alphabets, spaces and periods(.)')

    # Student class validation
    # Checks the length of the student class
    if (len(student_class) > 2 or len(student_class) == 0):
        print('Please enter a valid class')
        return False

    # Checks if the student class is a number or not
    if (not student_class.isnumeric()):
        print('Please enter a valid class number')
        return False
    
    # Checks whether the student class is in range 1 to 12
    if (int(student_class) > 12 or int(student_class) == 0):
        print('Enter a class that is from 1 to 12.')
        return False

    # Student DOB validation
    # Checks the length of DOB
    if (len(student_dob) != 10):
        print('Please enter data in the format (dd-mm-yyyy)')
        return False

    # To check if date is in dd-mm-yyyy format
    import datetime
    try:
        datetime.datetime.strptime(student_dob, '%d-%m-%Y')
    except ValueError:
        print('Please enter data in the format (dd-mm-yyyy)')

    return True # The data is correct


# Displays student menu (MAIN)
def student_menu(mycursor, mydb):

    # Initialize database variables
    dbcursor = mycursor
    db = mydb

    print(display_strings.student_menu_text) # Displays student menu
    student_menu_choice_number = input('Enter your choice: ')
    
    if (student_menu_choice_number.strip() == '1'): 
        create_student(dbcursor, db) # Function to inserts a new student and the details into the database

    elif (student_menu_choice_number.strip() == '2'):
        delete_student(dbcursor, db) # Function to delete student of a particular student ID from the database

    elif (student_menu_choice_number.strip() == '3'):
        display_all_students(dbcursor, db) # Function to display all students from database

    elif (student_menu_choice_number.strip() == '4'):
        return # Does not do anything. Returns to main menu

    else:
        print('Invalid option selected.\n')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see


# This function inserts a new student and the details into the database
def create_student(mycursor, mydb): # The function receives the database cursor parameter

    # Accepts student details from user
    print('Student details\n---------------')
    student_name = input('Enter the student full name (40 characters max): ')
    student_class = input('Enter the class of the student (1,2,...,10,11,12): ')
    student_dob = input('Enter the date of birth of the student (dd-mm-yyyy): ')

    # Trim student data
    student_name, student_class, student_dob = student_name.strip(), student_class.strip(), student_dob.strip()

    # Check student data
    student_data = (student_name, student_class, student_dob) # Pack the student data into a tuple

    # Checks whether the student data is correct
    if not is_student_data_correct(student_data):
        print('Check the data you\'ve entered.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return
    
    # Inserts details to database
    insert_student_query = "INSERT INTO student (full_name, class, dob) VALUES (%s, %s, %s)"
    val = (student_name, student_class, student_dob)
    mycursor.execute(insert_student_query, val)
    print(mycursor.rowcount, "record inserted.") # mycursor contains the rowcount field which has the count of rows affected

    # Displays the new student ID
    latest_student_id_query = "SELECT MAX(student_id) FROM student;"
    mycursor.execute(latest_student_id_query)
    student_id_result = mycursor.fetchone() # It fetches one row
    print('The new student ID is', student_id_result[0])

    mydb.commit() # Saves all changes to database

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see

# Deletes a student which has a student ID specified by user
def delete_student(mycursor, mydb):

    # Accepts student ID from user whose entry needs to be deleted
    student_id_to_delete = input('Enter the ID of student to be deleted: ')

    # Validation of the user entered student ID
    if (not student_id_to_delete.isnumeric()):
        print('Please enter a numeric student ID.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Fetches all student IDs for validation
    get_student_ids_query = 'SELECT student_id FROM student WHERE student_id = %s;'
    val = (student_id_to_delete,)
    mycursor.execute(get_student_ids_query, val)
    
    # Query to check if the student with student_id exists. If query returns 0 rows, then we notify the user that that student doesn't exist to delete
    if (mycursor.rowcount == 0 ):
        print('The student with student_id',student_id_to_delete,'does not exist.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return      

    delete_student_query = 'DELETE FROM student WHERE student_id = ' + student_id_to_delete
    mycursor.execute(delete_student_query)
    print(mycursor.rowcount, "record(s) deleted") # mycursor contains the rowcount field which has the count of rows affected

    mydb.commit() # Saves all changes to database

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see


# Displays all students from database
def display_all_students(mycursor, mydb):

    # Displays all student data
    latest_student_id_query = "SELECT student_id, full_name, class, dob FROM student;"
    mycursor.execute(latest_student_id_query)
    all_students = mycursor.fetchall()

    print(display_strings.student_details_header, end='') # Displays a nice student details heading. We add an end='' since the student_details_header already has a new line

    for student in all_students:
        
        # Extracting student data from tuple
        student_id = student[0]
        student_full_name = student[1]
        student_class = student[2]
        student_dob = student[3]

        # Prints row of student detail in an organized row
        print('| %4s | %29s | %5s | %11s |' % (student_id, student_full_name, student_class, student_dob))

    print(display_strings.student_details_footer) # Displays a student details footer

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
