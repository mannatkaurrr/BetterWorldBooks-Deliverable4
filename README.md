# BetterWorld Books Inc. Database Application

Mannat Kaur


## Description
BetterWorld Books is an online bookstore that sells new and used books. Customers can browse the website to find their desired books by title, author, genre/categories. They can also look at more detailed information about those books and eventually place an order. To place an order, customers can add payment details and check out. Lastly, the website allows customers to leave reviews for their orders. 

For deliverable #4, I will be creating a Python-based command-line application and performing CRUD (Create, Read, Update, Delete) operations on the “Book” table in the BetterWorld Books database. This will allow any user to manage the book inventory with operations such as view, insert, update and delete.


## Menu of operations available to perform on the database application:
1. Read all books in BetterWorld Books Inventory
2. Add a book in the BetterWorld Books Inventory
3. Update a book record in BetterWorld Books Inventory
4. Delete a book record from BetterWorld Books Inventory
5. Calculate average price of all books in BetterWorld Books Inventory

## Languages & platforms used for the database application:
1. Python
2. mysql.connector
3. Terminal

## Requirements:
Before running this application, please ensure you have Python 3 installled on your terminal. You must also be connected to MYSQL Server and it should be installed & running.

## How to run database application:
1. Open crud_app.py
2. Locate the following section below & update it with your own MYSQL credentials. Note: "youruser" must be your MYSQL credential & "yourpassword" must be your MYSQL password. Hit save.
   
```python
connection = mysql.connector.connect(
  host="localhost",
  user="youruser",
  password="yourpassword",
  database="BetterWorldBooksDB")
```
3. Once connected to MySQL database, open Terminal and run the Python file using this:

```python
python3 crud_app.py
```
4. Use the menu options to perform CRUD operations (1,2,3,4,5,6)
5. Press 6 from the Menu to exit & close the MYSQL connection.

## Specifics of database application:
This database applicaiton includes error handling using try/except/finally and is a command-line application, easier for all users. 
Currently the sample values for insert, update and delete are hardcoded for this demonstrating this deliverable 4.
