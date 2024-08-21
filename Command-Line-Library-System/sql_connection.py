import mysql.connector # Library to connect Python to MySQL

# Database connection to the MySQL "school" database
mydb = mysql.connector.connect(host="localhost", user="root", passwd="173-Balenp%%5690", auth_plugin='mysql_native_password', database='school')
mycursor = mydb.cursor(buffered=True) # buffered=True to avoid error that occurs when we fetch data but don't use it
