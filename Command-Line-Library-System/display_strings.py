# ---------------------------- General strings ----------------------------

hit_enter_text = '\nPress Enter to continue'

# ---------------------------- String related to main file ----------------------------

# ASCII text pattern generator from link https://manytools.org/hacker-tools/ascii-banner/   Font = Stop
welcome_message = '''
 _ _ _                                                               
| (_) |                                              _               
| |_| | _   ____ ____  ____ _   _     ___ _   _  ___| |_  ____ ____  
| | | || \ / ___) _  |/ ___) | | |   /___) | | |/___)  _)/ _  )    \ 
| | | |_) ) |  ( ( | | |   | |_| |  |___ | |_| |___ | |_( (/ /| | | |
|_|_|____/|_|   \_||_|_|    \__  |  (___/ \__  (___/ \___)____)_|_|_|
                           (____/        (____/                      
=====================================================================
=====================================================================
'''

# Text displayed in the main menu of the main program
main_menu_text = '''
Choose an option from the main menu:
------------------------------------
1. Issue a book to the student
2. Student returning a book
3. Display issue history
4. Display students past due date
5. Book management
6. Student management
7. Exit
'''

# ---------------------------- String related to student file ----------------------------

student_menu_text = '''
Student Menu
============
1. Add new student
2. Delete student
3. Display all students
4. Go to main menu
'''

student_details_header = '''
==============================================================
********************   STUDENT DETAILS   *********************
==============================================================
|  ID  |           Full Name           | Class |     DOB     |
==============================================================
==============================================================
'''

student_details_footer = '=============================================================='

# ---------------------------- String related to book file ----------------------------

book_menu_text = '''
Book Menu
============
1. Add new book
2. Delete book
3. Display all book
4. Go to main menu
'''

book_details_header = '''
=================================================================================================================
***********************************************   BOOK DETAILS   ************************************************
=================================================================================================================
|  ID  |                      Title                       |               Author               | Published year |
=================================================================================================================
=================================================================================================================
'''

book_details_footer = '================================================================================================================='

# ---------------------------- String related to student book file ----------------------------

issue_history_details_header = '''
============================================================================================================================================
************************************************************   ISSUE HISTORY   ************************************************************
============================================================================================================================================
| student_id |       student_name        | book_id |      book_title      | issue_date | to_be_returned_date |   returned_date  | days_due |
============================================================================================================================================
============================================================================================================================================
'''

issue_history_details_footer = '============================================================================================================================================'



students_past_due_date_header = '''
=========================================================================================================================
**********************************************   STUDENTS PAST DUE DATE   **********************************************
=========================================================================================================================
| student_id |       student_name        | book_id |      book_title      | issue_date | to_be_returned_date | days_due |
=========================================================================================================================
=========================================================================================================================
'''

students_past_due_date_footer = '========================================================================================================================='