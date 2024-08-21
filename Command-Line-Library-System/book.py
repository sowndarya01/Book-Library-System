import display_strings

dbcursor = None # Stores the database cursor
db = None # Stores the database connection

# Function checks if entered book data is valid or not
def is_book_data_correct(book_data):
    
    (book_title, book_author, book_published_year) = book_data # Unpack tuple book data

    # Book title validation
    # Checking Book title length
    if (len(book_title) == 0 or len(book_title) > 100):
        print('Please enter a book title with at least 1 to 100 characters. ')
        return False
    
    # Book author validation
    # Checking Book author length
    if (len(book_author) == 0 or len(book_author) > 40):
        print('Please enter a book author with at least 1 to 100 characters. ')
        return False

    # Book book published year validation
    # Checking if published year is a valid year
    if (int(book_published_year) < 1000 or int(book_published_year) > 2025):
        print('Please enter a published year between 1000 to 2025. ')
        return False
    
    return True

# Displays book menu
def book_menu(mycursor, mydb):

    print(display_strings.book_menu_text) # Displays book menu
    book_menu_choice_number = input('Enter your choice: ')
    
    if (book_menu_choice_number.strip() == '1'): 
        create_book(mycursor, mydb) # Function to inserts a new book and the details into the database

    elif (book_menu_choice_number.strip() == '2'):
        delete_book(mycursor, mydb) # Function to delete book of a particular book ID from the database

    elif (book_menu_choice_number.strip() == '3'):
        display_all_books(mycursor, mydb) # Function to display all books from database

    elif (book_menu_choice_number.strip() == '4'): 
        return # Does not do anything. Returns to main menu

    else:
        print('Invalid option selected.\n')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see


# This function inserts a new book and the details into the database
def create_book(mycursor, mydb): # The function receives the database cursor parameter

    # Accepts book details from user
    print('Book details\n---------------')
    book_title = input('Enter the book title (100 characters max): ')
    book_author = input('Enter the author (40 characters max): ')
    book_published_year = input('Enter the year the book was published (yyyy): ')

    # Trim all spaces
    book_title, book_author, book_published_year = book_title.strip(), book_author.strip(), book_published_year.strip()

    # Check book data
    book_data = (book_title, book_author, book_published_year) # Pack the book data into a tuple

    if not is_book_data_correct(book_data):
        print('Check the data you\'ve entered.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return
    
    # Inserts details to database
    insert_book_query = "INSERT INTO book (title, author, published_year) VALUES (%s, %s, %s)"
    val = (book_title, book_author, book_published_year)
    mycursor.execute(insert_book_query, val)
    print(mycursor.rowcount, "record inserted.") # mycursor contains the rowcount field which has the count of rows affected

    # Displays the new book ID
    latest_book_id_query = "SELECT MAX(book_id) FROM book;"
    mycursor.execute(latest_book_id_query)
    book_id_result = mycursor.fetchone()
    print('The new book ID is', book_id_result[0])

    mydb.commit() # Saves all changes to database

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see

# Deletes a book which has a book ID specified by user
def delete_book(mycursor, mydb):

    # Accepts book ID from user whose entry needs to be deleted
    book_id_to_delete = input('Enter the ID of book to be deleted: ')

    # Fetches all book IDs for validation
    get_book_ids_query = 'SELECT book_id FROM book WHERE book_id = %s;'
    val = (book_id_to_delete,)
    mycursor.execute(get_book_ids_query, val)
    
    # Query to check if the book with book_id exists. If query returns 0 rows, then we notify the user that that book doesn't exist to delete
    if (mycursor.rowcount == 0 ):
        print('The book with book_id',book_id_to_delete,'does not exist.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return    

    # Validation of the user entered book ID
    if (not book_id_to_delete.isnumeric()):
        print('Please enter a numeric book ID.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Deleting the book with a book ID entered by user
    delete_book_query = 'DELETE FROM book WHERE book_id = ' + book_id_to_delete
    mycursor.execute(delete_book_query)
    print(mycursor.rowcount, "record(s) deleted") # mycursor contains the rowcount field which has the count of rows affected

    mydb.commit() # Saves all changes to database

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see


# Displays all books from database
def display_all_books(mycursor, mydb):

    # Displays all book data
    latest_book_id_query = "SELECT book_id, title, author, published_year FROM book;"
    mycursor.execute(latest_book_id_query)
    all_books = mycursor.fetchall()

    print(display_strings.book_details_header, end='') # Displays a book details heading. We add an end='' since the book_details_header already has a new line

    for book in all_books:
        
        # Extracting book data from tuple
        book_id = book[0]
        book_title = book[1]
        book_author = book[2]
        book_published_year = book[3]

        # Prints row of book detail in an organized row
        print('| %4s | %48s | %34s | %14s |' % (book_id, book_title, book_author, book_published_year))

    print(display_strings.book_details_footer) # Displays a book details footer

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
