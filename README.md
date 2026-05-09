# BetterWorld Books Inc. Database Application
Mannat Kaur

## Description
BetterWorld Books is an online bookstore that sells new and used books. Customers can browse the website to find their desired books by title, author, genre/categories. They can also look at more detailed information about those books and eventually place an order. To place an order, customers can add payment details and check out. Lastly, the website allows customers to leave reviews for their orders. 

For deliverable #5, I will be extending deliverable #4 into a fully interactive Python-based command-line application and performing CRUD (Create, Read, Update, Delete) operations on all tables in the BetterWorld Books database. This database application is a user-friendly command-line interface that supports advanced SQL functionalities & queries, dynamic user interaction and improved error handling.

## Features of the BetterWorld Books database application:

Users can execute Full CRUD (Create, Read, Update, Delete) operations on the following tables in the BetterWorld Books database application:

- Author
- Book
- Customer
- Genre
- Payment
- Review
- TransactionItem
- TransactionSale

## Dynamic Interactive Features of the BetterWorld Books database application
- Dynamic and user-friendly menu navigation using 
- User can dynamically choose CRUD operations 

## Advanced SQL Queries
There are 7 complex queries that users can choose from to execute. Thes queries help conduct a deeper analysis on the data in the database and provide meaningful business insights/analysis. Here is information on what each query does & why it is important:

### Query 1 - View Multi-Book Transactions
Statement: Shows which transaction has multiple books purchased.

Why this is Helpful: The database can show many transaction items in 1 single transaction sale. This query is useful for                administration that would like to see all books that belong to 1 single transaction.

Functions Used: Set membership IN, GROUP BY, HAVING, COUNT

Description of SQL Statement: To do so, we will combine 3 tables: TransactionSale, TransactionItem and Book. We will retrieve           all transaction_sale_id under the Transaction Item table and group them by their ids. This will help group items that belong            to the same transaction sale. Next, using: HAVING COUNT(book_id) > 1. This will help in filtering transactions_sale_id that               have more than 1 book purchased. Lastly, sort the rows by transaction_sale_id.
        
### Query 2 - View Sales by Genre
Statement: Show which genre of books sell the most at BetterWorld Books

Why this is Helpful: This would be extremely helpful for admin to understand which genre is generating the most revenue. 

Functions Used: aggregate functions using SUM(), GROUP BY

Description of SQL Statement: For this query, we will join tables: Book, Genre, TransactionItem, TransactionSale. We would              retrieve all genres in the catalog. Using the cost of price for each book_id and multiplying it with the quantity sold under            quantity for those corresponding sold books under transaction items to create a new column called total_sales. This will                reflect total amount sold using this line: ROUND(SUM(b.price * ti.quantity), 2) AS total_sales. Then, we will sort by genre             and order the genre by the highest to lowest sales using ORDER BY total_sales DESC;
          
### Query 3 - Rank Books by Customer Rating
Statement: Rank all books from highest to lowest rating.

Why this is Helpful: Admin would like to see the lowest & high rated books quickly, this can help make short-term decisions             with sales within administration to run more marketing or adjust pricing for those specific books. Specifically for this one,           it is helpful to see the ranking system for books rather than a sorted result, which is easier for comparing products. RANK()           can help with this because it is easier to scroll for the lowest and highest ranking instead of sorting through the lowest              and highest rating.

Functions Used: OLAP/window function using RANK() OVER, subquery, AVG(), GROUP BY

Description of SQL Statement: For this query, we will join tables: Book, Author, Genre and Review. We will calculate the                average rating for each book using: AVG(r.rating) AS average_rating. This will be helpful since each book has multiple                  ratings, so we want to see the overall rating. Then we will use OLAP/window function: RANK() to assign a ranking for each book          based on their average rating that we calculated from above.
          
### Query 4 - View Revenue Rollup by Genre and Payment Method
Statement: Show transaction sales total amounts by genre & grand totals of all totals for each genre.

Why this is Helpful: This is helpful because we can see how much each genre makes in revenue. Admin/upper management can               take a look at this and understand out of all genres, which is the top performing genre and how are customers paying for it.

Functions Used: OLAP query using WITH ROLLUP, SUM(), GROUP BY

Description of SQL Statement: For this query, we will join 5 tables: Book, Genre, TransactionItem, Transactionsale and                  Payment. Firstly, we select the name of all genres, payment methods and calculate the total sales using: SUM(b.price *                  ti.quantity) AS total_salesNext, we will group them by genre and payment method, adding WITH ROLLUP; This will summarize               each genre & give an extra line for the grand total for all total sales from all payment methods used. 
          
### Query 5 - Smart Value Book Recommendations
Statement: Shows affordable, used-books compared against a chosen benchmark genre 

Why this is Helpful: This query is useful in narrowing down book options that fall within the customer’s budget but still be            able to have high reviews before making a transaction sale. This is a dynamic query where the user can enter in a benchmark             genre of their choice from the list of genres & it will compare affordable books against it to identify a better-value recommendations.

Functions Used: Set comparison using ALL and subqueries

Description of SQL Statement: For this specific query, we combine information from 4 tables in the database: Book, Author,              Genre and Review. We will calculate the average rating for each book using: AVG(r.rating) AS average_rating. This will be               helpful since each book has multiple ratings, so we want to see the overall rating. We will also filter to only show books              priced from $10 to $15 using: WHERE price BETWEEN 10 AND 15 and book condition “Used-Good” using this: AND book_condition               LIKE 'Used - Good’ Next, this query uses a set comparison with ALL compare book prices against a user-selected benchmark                genre that will return books that are lower priced than all the books in the chosen benchmark genre.

### Query 6 - View Most Used Payment Methods
Statement: Shows which payment methods have been used the most in transactions by customers.

Why this is Helpful: Instead of displaying the full transaction history of the chosen customer. We will display payment                 methods of all customers & which ones are used most frequently.  This is helpful for the admin to see transaction patterns to           decipher any financial decisions to be taken related to payment.

Functions Used: Set operation using UNION, COUNT(), GROUP BY

Description of SQL Statement: This query only used the Payment table to retrieve information on payment methods according to            the id. We use COUNT() to add up how many times different payment methods are used & SUM() to add up how much was spent for             each payment method. Next, we group by Payment method and order the list by highest to lowest spent on those methods using              DESC;

### Query 7 - View Customer Loyalty Ranking
Statement: Show total spending for each customer & compare it in a list for loyalty program analysis.

Why this is Helpful: This is helpful for administration to understand customer loyalty especially if they are implementing a            customer reward program & need business analysis to support that. It is useful because it will show that using DENSE_RANK()             can be an effective ranking comparison method. 

Functions Used: Subquery using WITH clause, OLAP/window function using DENSE_RANK()

Description of SQL Statement: This query joins 2 tables together: Customer and TransactionSale. First, the WITH clause creates a temporary result called ranked_customers. We select what we want to see in ranked_customer which is customer_id, name of customer, total_spent. Then we use DENSE_RANK() OVER (ORDER BY total_spent DESC) AS customer_rank to rank the customers based on total_spent. The highest rank is given to the customer who spent the most at BetterWorld Books. If 2 customers spent the same amount, they are given the same rank. Next, we also select the total transaction sale amount & sum up the total based on customer id & create a new column called total_spent using: SUM(ts.total_transaction_sale_amount) AS total_spent. Then we group by customer_id and order the list from highest rank to lowest rank. This allows BetterWorld Books administration to compare customer spending patterns more effectively for loyalty and rewards analysis.
          
## Languages, libraries and platforms used for the BetterWorld Books database application:

### Languages and Libraries:
- Python
- SQL
- mysql.connector (installed from Python Library)
- datetime (installed from Python library)
- decimal (installed from Python library)
- getpass (installed from Python library)
- tabulate 
  
### Platforms:
- MySQL Server
- Terminal

## Requirements:
You must ensure the following are installed and properly running before executing the application:
- Python3
- MySQL Server
- mysql.connector (From Python library)
- tabulate

To install mysql.connector & tabulate use:

```python
pip3 install mysql-connector-python
pip3 install tabulate
```

## How to Download and Run the Database Application
1) Download the BetterWorld Books application files from this GitHub.
2) Open the project folder in Terminal. To do so, right-click the downloaded folder & click "New Terminal at Folder"
3) In your terminal, enter the following code to run the database application
   
```python
python3 betterworldbooksapp.py
```

4) The application will prompt the user to either: "Use default database settings" or "Enter custom MySQL credentials" by entering yes (y) or no (n).
5) Enter your MySQL login credentials to connect.
6) Once connected successfully, navigate through the interactive menu system to perform CRUD operations (1,2,3,4,5,6)

8) When you are ready to log off, select "Exit" from the Main Menu to safely close the database connection and terminate the application.

## Specifics of database application:

# Error-Handling & Security
This database application contains many error-handling, validation features for better usability. It also contains database security functionalities to help secure and private connections:

- Date, email, phone number input validation
- Decimal + integer number & blank input validation
- Foreign key constraints
- User-friendly cancellation using "exit" inputs
- Exception handling using try, except and finally.
- Entering password using getpass() & making sure it is hidden
- Username and password invalidation using error-handling messages
