# BetterWorld Books Inc. Database Application

Mannat Kaur


## Description
BetterWorld Books is an online bookstore that sells new and used books. Customers can browse the website to find their desired books by title, author, genre/categories. They can also look at more detailed information about those books and eventually place an order. To place an order, customers can add payment details and check out. Lastly, the website allows customers to leave reviews for their orders. 

For deliverable #5, I will be extending deliverable #4 into a fully interactive Python-based command-line application and performing CRUD (Create, Read, Update, Delete) operations on all tables in the BetterWorld Books database. This database application is a user-friendly command-line interface that supports advanced SQL functionalities & queries, dynamic user interaction and improved error handling.

## Features of the BetterWorld Books database application:

Users can Full CRUD (Create, Read, Update, Delete) operations on the following tables:
- Author
- Book
- Customer
- Genre
- Payment
- Review
- TransactionItem
- TransactionSale

Advanced SQL Queries
There are 7 complex queries 


## Languages, libraries and platforms used for the BetterWorld Books database application:

### Programming Languages:
1. Python
2. SQL
### Python Libraries:
1. mysql.connector
2. datetime
3. decimal
4. getpass
### Platforms:
1. MySQL Server
2. Terminal / Command-Line Interface

## Requirements:
Before running this application, please ensure you have Python 3 installled on your terminal. You must also be connected to MYSQL Server and it should be installed & running.

## How to run database application:
1. You must ensure that MySQL Server is running and connected properly before executing the application.

To install mysql.connector, run:

```python
pip install mysql-connector-python
```
2. Download the python file listed in this GitHub named "BetterWorldBooksApp.py". Save on desktop.
2. Once connected to MySQL, open Terminal and run the Python file using this:

```python
python3 .py
```
4. Use the menu options to perform CRUD operations (1,2,3,4,5,6)
5. Press 6 from the Menu to exit & close the MYSQL connection.

## Specifics of database application:
This database applicaiton includes error handling using try/except/finally and is a command-line application, easier for all users. 
Currently the sample values for insert, update and delete are hardcoded for this demonstrating this deliverable 4.
