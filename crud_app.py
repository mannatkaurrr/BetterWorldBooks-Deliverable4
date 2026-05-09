#BetterWorld Books App
import mysql.connector
from decimal import Decimal, InvalidOperation
from datetime import datetime
from getpass import getpass


def requiredinput(prompt, numbers_allowed=True):
    while True:
        value = input(prompt).strip()

        if value.lower() == "exit":
            return None

        if value == "":
            print("Error: This field cannot be blank.")
            continue

        if not numbers_allowed and not any(char.isalpha() for char in value):
            print("Error: Numbers are not allowed for this field.")
            continue

        return value


def integerinput(prompt):
    while True:
        value = input(prompt).strip()

        if value.lower() == "exit":
            return None

        if value == "":
            print("Error: This field cannot be blank.")
            continue

        try:
            return int(value)

        except ValueError:
            print("Error: Please enter a valid whole number.")


def decimalinput(prompt):
    while True:
        value = input(prompt).strip()

        if value.lower() == "exit":
            return None

        if value == "":
            print("Error: This field cannot be blank.")
            continue

        try:
            return Decimal(value)

        except InvalidOperation:
            print("Error: Please enter a valid decimal number.")


def dateinput(prompt):
    while True:
        value = input(prompt).strip()

        if value.lower() == "exit":
            return None

        if value == "":
            print("Error: This field cannot be blank.")
            continue

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value

        except ValueError:
            print("Error: Please enter the date in YYYY-MM-DD format.")

def emailinput(prompt):
    while True:
        email = input(prompt).strip()

        if email.lower() == "exit":
            return None

        if email == "":
            print("Error: Email cannot be blank.")
            continue

        if "@" not in email or "." not in email:
            print("Error: Please enter a valid email address.")
            continue

        return email

def phoneinput(prompt):
    while True:
        phone = input(prompt).strip()

        if phone.lower() == "exit":
            return None

        if phone == "":
            print("Error: Phone number cannot be blank.")
            continue

        cleaned_phone = phone.replace("-", "").replace(" ", "")

        if not cleaned_phone.isdigit():
            print("Error: Phone number must contain numbers only.")
            continue

        return phone

def billingaddressinput(prompt):
    while True:
        address = input(prompt).strip()

        if address.lower() == "exit":
            return None

        if address == "":
            print("Error: Address cannot be blank.")
            continue

        if len(address) > 100:
            print("Error: Address cannot exceed 100 characters.")
            continue

        return address


def confirmation(prompt="Are you sure?", y="y", n="n"):
    while True:
        choice = input(f"{prompt} ({y}/{n}): ").strip().lower()

        if choice == y:
            return True

        elif choice == n:
            return False

        else:
            print(f"Invalid choice. Please enter '{y}' or '{n}'.")


def runbetterworldbooksdatabase():
    print("\nWelcome to the BetterWorld Books Management System")
    print("Type 'exit' at any time to cancel setup.\n")

    use_default = input("Would you like to use default options? (y/n): ").strip().lower()

    if use_default == "exit":
        return None

    if use_default == "y":
        password = getpass("Enter your MySQL password: ")
        return {
            "host": "localhost",
            "user": "root",
            "password": password,
            "database": "BetterWorldBooksDB"
        }

    host = requiredinput("Enter the MySQL host: ")
    user = requiredinput("Enter your MySQL username: ")
    password = getpass("Enter your MySQL password: ")
    database = requiredinput("Enter your database name: ")

    return {
        "host": host,
        "user": user,
        "password": password,
        "database": database
    }


try:
    while True:
        databaselogin = runbetterworldbooksdatabase()
        if databaselogin is None:
            print("Database setup cancelled.")
            exit()


        try:
            connection = mysql.connector.connect(
                host=databaselogin["host"],
                user=databaselogin["user"],
                password=databaselogin["password"],
                database=databaselogin["database"]
            )

            if connection.is_connected():
                print("Connected to the MySQL database successfully")
                break

        except mysql.connector.Error as e:
            print("Error connecting to database:", e)
            print("Please try again.\n")

    cursor = connection.cursor()


    def viewtable(table_name):
        select_query = f"SELECT * FROM {table_name}"
        cursor.execute(select_query)
        records = cursor.fetchall()

        print(f"\nViewing Table: {table_name}\n")

        if not records:
            print("No records found.")
            return

        for record in records:
            if table_name == "Author":
                print(f"Author ID: {record[0]}, First Name: {record[1]}, Last Name: {record[2]}")

            elif table_name == "Book":
                print(f"Book ID: {record[0]}, Title: {record[1]}, Price: ${record[2]}, Condition: {record[3]}, Publication Year: {record[4]}, ISBN: {record[5]}, Author ID: {record[6]}, Genre ID: {record[7]}")

            elif table_name == "Customer":
                print(f"Customer ID: {record[0]}, First Name: {record[1]}, Last Name: {record[2]}, Email: {record[3]}, Phone Number: {record[4]}, Billing Address: {record[5]}")

            elif table_name == "Genre":
                print(f"Genre ID: {record[0]}, Genre Name: {record[1]}")

            elif table_name == "Payment":
                print(f"Payment ID: {record[0]}, Method: {record[1]}, Date: {record[2]}, Amount: ${record[3]}, Transaction Sale ID: {record[4]}")

            elif table_name == "Review":
                print(f"Review ID: {record[0]}, Comment: {record[1]}, Date: {record[2]}, Rating: {record[3]}, Customer ID: {record[4]}, Book ID: {record[5]}")

            elif table_name == "TransactionItem":
                print(f"Transaction Item ID: {record[0]}, Quantity: {record[1]}, Book ID: {record[2]}, Transaction Sale ID: {record[3]}")

            elif table_name == "TransactionSale":
                print(f"Transaction Sale ID: {record[0]}, Date: {record[1]}, Total Amount: ${record[2]}, Status: {record[3]}, Customer ID: {record[4]}")

        print(f"{table_name} record retrieved successfully.")


    def readdata():
        while True:
            print("\nView Tables\n")
            print("Display data from any selected table from BetterWorld Books Database\n")
            print("1. Authors")
            print("2. Books")
            print("3. Customers")
            print("4. Genres")
            print("5. Payments")
            print("6. Reviews")
            print("7. Transaction Items")
            print("8. Transaction Sales")
            print("9. Back to Main Menu\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                viewtable("Author")
            elif choice == "2":
                viewtable("Book")
            elif choice == "3":
                viewtable("Customer")
            elif choice == "4":
                viewtable("Genre")
            elif choice == "5":
                viewtable("Payment")
            elif choice == "6":
                viewtable("Review")
            elif choice == "7":
                viewtable("TransactionItem")
            elif choice == "8":
                viewtable("TransactionSale")
            elif choice == "9":
                break
            else:
                print("Invalid choice. Please select a valid option.")


    def insertauthor():
        print("\nAdd New Author")
        print("Type 'exit' at any time to cancel.\n")
        author_id = integerinput("Enter author ID: ")
        first_name = requiredinput("Enter first name: ", numbers_allowed=False)
        last_name = requiredinput("Enter last name: ", numbers_allowed=False)

        if author_id is None or first_name is None or last_name is None:
            print("Insert cancelled.")
            return

        insert_query = "INSERT INTO Author (author_id, first_name, last_name) VALUES (%s, %s, %s)"

        try:
            cursor.execute(insert_query, (author_id, first_name, last_name))
            connection.commit()
            print("New author record inserted successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error:", e)

    def insertgenre():
        print("\nAdd New Genre")
        print("Type 'exit' at any time to cancel.\n")
        genre_id = integerinput("Enter genre ID: ")
        genre_name = requiredinput("Enter genre name: ", numbers_allowed=False)

        if genre_id is None or genre_name is None:
            print("Insert cancelled.")
            return

        insert_query = "INSERT INTO Genre (genre_id, genre_name) VALUES (%s, %s)"

        try:
            cursor.execute(insert_query, (genre_id, genre_name))
            connection.commit()
            print("New genre record inserted successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error:", e)

    def insertpayment():
        print("\nAdd New Payment")
        print("Type 'exit' at any time to cancel.\n")
        payment_id = integerinput("Enter payment ID: ")
        payment_method = requiredinput("Enter payment method: ")
        payment_date = dateinput("Enter payment date (YYYY-MM-DD): ")
        payment_amount = decimalinput("Enter payment amount: ")
        transaction_sale_id = integerinput("Enter transaction sale ID: ")

        if payment_id is None or payment_method is None or payment_date is None or payment_amount is None or transaction_sale_id is None:
            print("Insert cancelled.")
            return

        insert_query = """
        INSERT INTO Payment
        (payment_id, payment_method, payment_date, payment_amount, transaction_sale_id)
        VALUES (%s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(insert_query, (payment_id, payment_method, payment_date, payment_amount, transaction_sale_id))
            connection.commit()
            print("New payment record inserted successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error:", e)

    def inserttransactionitem():
        print("\nAdd New Transaction Item")
        print("Type 'exit' at any time to cancel.\n")
        transaction_item_id = integerinput("Enter transaction item ID: ")
        quantity = integerinput("Enter quantity: ")
        book_id = integerinput("Enter book ID: ")
        transaction_sale_id = integerinput("Enter transaction sale ID: ")

        if transaction_item_id is None or quantity is None or book_id is None or transaction_sale_id is None:
            print("Insert cancelled.")
            return

        insert_query = "INSERT INTO TransactionItem (transaction_item_id, quantity, book_id, transaction_sale_id) VALUES (%s, %s, %s, %s)"

        try:
            cursor.execute(insert_query, (transaction_item_id, quantity, book_id, transaction_sale_id))
            connection.commit()
            print("New transaction item record inserted successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error:", e)

    def inserttransactionsale():
        print("\nAdd New Transaction Sale")
        print("Type 'exit' at any time to cancel.\n")
        transaction_sale_id = integerinput("Enter transaction sale ID: ")
        transaction_sale_date = dateinput("Enter transaction sale date (YYYY-MM-DD): ")
        total_transaction_sale_amount = decimalinput("Enter total transaction sale amount: ")
        transaction_sale_status = requiredinput("Enter transaction sale status: ")
        customer_id = integerinput("Enter customer ID: ")

        if transaction_sale_id is None or transaction_sale_date is None or total_transaction_sale_amount is None or transaction_sale_status is None or customer_id is None:
            print("Insert cancelled.")
            return

        insert_query = """
        INSERT INTO TransactionSale
        (transaction_sale_id, transaction_sale_date, total_transaction_sale_amount, transaction_sale_status, customer_id)
        VALUES (%s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(insert_query, (transaction_sale_id, transaction_sale_date, total_transaction_sale_amount, transaction_sale_status, customer_id))
            connection.commit()
            print("New transaction sale record inserted successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error:", e)

    def insertbook():
        print("\nAdd New Book")
        print("Type 'exit' at any time to cancel.\n")
        book_id = integerinput("Enter book ID: ")
        title = requiredinput("Enter title: ")
        price = decimalinput("Enter price: ")
        book_condition = requiredinput("Enter book condition: ")
        publication_year = integerinput("Enter publication year: ")
        isbn = requiredinput("Enter ISBN: ")
        author_id = integerinput("Enter author ID: ")
        genre_id = integerinput("Enter genre ID: ")

        if None in (book_id, title, price, book_condition, publication_year, isbn, author_id, genre_id):
            print("Insert cancelled.")
            return

        if price <= 0:
            print("Error: Price must be greater than 0.")
            return

        insert_query = """
        INSERT INTO Book
        (book_id, title, price, book_condition, publication_year, isbn, author_id, genre_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(insert_query, (book_id, title, price, book_condition, publication_year, isbn, author_id, genre_id))
            connection.commit()
            print("New book record inserted successfully.")
        except mysql.connector.IntegrityError as e:
            connection.rollback()

            if "foreign key constraint fails" in str(e).lower():
                print("Error: The author ID or genre ID does not exist.")
                print("Please view the Author and Genre tables first, then enter a valid ID.")
            else:
                print("Database integrity error:", e)

        except mysql.connector.Error as e:
            connection.rollback()
            print("Error:", e)


    def insertcustomer():
        print("\nAdd New Customer")
        print("Type 'exit' at any time to cancel.\n")
        customer_id = integerinput("Enter customer ID: ")
        first_name = requiredinput("Enter first name: ", numbers_allowed=False)
        last_name = requiredinput("Enter last name: ", numbers_allowed=False)
        email = emailinput("Enter email: ")
        phone_number = phoneinput("Enter phone number: ")
        billing_address = billingaddressinput("Enter billing address: ")

        if customer_id is None or first_name is None or last_name is None or email is None:
            print("Insert cancelled.")
            return

        insert_query = """
        INSERT INTO Customer
        (customer_id, first_name, last_name, email, phone_number, billing_address)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(insert_query, (customer_id, first_name, last_name, email, phone_number, billing_address))
            connection.commit()
            print("New customer record inserted successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error:", e)

    def insertreview():
        print("\nAdd New Review")
        print("Type 'exit' at any time to cancel.\n")
        review_id = integerinput("Enter review ID: ")
        comment = requiredinput("Enter comment: ")
        review_date = dateinput("Enter review date (YYYY-MM-DD): ")
        rating = decimalinput("Enter rating: ")
        customer_id = integerinput("Enter customer ID: ")
        book_id = integerinput("Enter book ID: ")

        if review_id is None or comment is None or review_date is None or rating is None or customer_id is None or book_id is None:
            print("Insert cancelled.")
            return

        insert_query = """
        INSERT INTO Review
        (review_id, comment, review_date, rating, customer_id, book_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(insert_query, (review_id, comment, review_date, rating, customer_id, book_id))
            connection.commit()
            print("New review record inserted successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error:", e)


    def writedata():
        while True:
            print("\nTable Inserts")
            print("Add data to any selected table from BetterWorld Books Database\n")
            print("1. Add New Author")
            print("2. Add New Book")
            print("3. Add New Customer")
            print("4. Add New Genre")
            print("5. Add New Payment")
            print("6. Add New Review")
            print("7. Add New Transaction Item")
            print("8. Add New Transaction Sale")
            print("9. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                insertauthor()
            elif choice == "2":
                insertbook()
            elif choice == "3":
                insertcustomer()
            elif choice == "4":
                insertgenre()
            elif choice == "5":
                insertpayment()
            elif choice == "6":
                insertreview()
            elif choice == "7":
                inserttransactionitem()
            elif choice == "8":
                inserttransactionsale()
            elif choice == "9":
                break
            else:
                print("Invalid choice. Please select a valid option.")


    def deleterecord(table_name, primary_key):
        print(f"\nDelete Record from {table_name}")
        print("Type 'exit' at any time to cancel.\n")
        viewtable(table_name)

        record_id = integerinput(f"Enter {primary_key} to delete: ")

        if record_id is None:
            print("Delete cancelled.")
            return

        check_query = f"SELECT * FROM {table_name} WHERE {primary_key} = %s"
        cursor.execute(check_query, (record_id,))
        record = cursor.fetchone()

        if not record:
            print("No matching record found.")
            return

        if not confirmation("Are you sure you want to permanently delete this record?"):
            print("Delete cancelled.")
            return

        delete_query = f"DELETE FROM {table_name} WHERE {primary_key} = %s"

        try:
            cursor.execute(delete_query, (record_id,))
            connection.commit()
            print("Record deleted successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error deleting record:", e)


    def deletedata():
        while True:
            print("\nTable Deletes - Menu\n")
            print("Delete data in any selected table from BetterWorld Books Database\n")
            print("1. Delete Author")
            print("2. Delete Book")
            print("3. Delete Customer")
            print("4. Delete Genre")
            print("5. Delete Payment")
            print("6. Delete Review")
            print("7. Delete Transaction Item")
            print("8. Delete Transaction Sale")
            print("9. Back to Main Menu\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                deleterecord("Author", "author_id")
            elif choice == "2":
                deleterecord("Book", "book_id")
            elif choice == "3":
                deleterecord("Customer", "customer_id")
            elif choice == "4":
                deleterecord("Genre", "genre_id")
            elif choice == "5":
                deleterecord("Payment", "payment_id")
            elif choice == "6":
                deleterecord("Review", "review_id")
            elif choice == "7":
                deleterecord("TransactionItem", "transaction_item_id")
            elif choice == "8":
                deleterecord("TransactionSale", "transaction_sale_id")
            elif choice == "9":
                break
            else:
                print("Invalid choice. Please select a valid option.")


    def updateauthor():
        print("\nUpdate Author")
        print("Type 'exit' at any time to cancel.\n")
        viewtable("Author")

        author_id = integerinput("Enter author ID to update: ")

        if author_id is None:
            print("Update cancelled.")
            return

        print("1. First Name")
        print("2. Last Name")

        choice = input("Enter your choice: ")

        if choice == "1":
            column_name = "first_name"
            new_value = requiredinput("Enter new first name: ")
        elif choice == "2":
            column_name = "last_name"
            new_value = requiredinput("Enter new last name: ")
        else:
            print("Invalid choice.")
            return

        update_query = f"UPDATE Author SET {column_name} = %s WHERE author_id = %s"

        try:
            cursor.execute(update_query, (new_value, author_id))
            connection.commit()

            if cursor.rowcount == 0:
                print("No author found with that ID.")
            else:
                print("Author record updated successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error updating author:", e)


    def updatebook():
        print("\nUpdate Book")
        print("Type 'exit' at any time to cancel.\n")
        viewtable("Book")

        book_id = integerinput("Enter book ID to update: ")

        if book_id is None:
            print("Update cancelled.")
            return

        print("1. Title")
        print("2. Price")
        print("3. Book Condition")

        choice = input("Enter your choice: ")

        if choice == "1":
            column_name = "title"
            new_value = requiredinput("Enter new title: ")
        elif choice == "2":
            column_name = "price"
            new_value = decimalinput("Enter new price: ")
        elif choice == "3":
            column_name = "book_condition"
            new_value = requiredinput("Enter new book condition: ")
        else:
            print("Invalid choice.")
            return

        update_query = f"UPDATE Book SET {column_name} = %s WHERE book_id = %s"

        try:
            cursor.execute(update_query, (new_value, book_id))
            connection.commit()

            if cursor.rowcount == 0:
                print("No book found with that ID.")
            else:
                print("Book record updated successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error updating book:", e)


    def updatecustomer():
        print("\nUpdate Customer")
        print("Type 'exit' at any time to cancel.\n")
        viewtable("Customer")

        customer_id = integerinput("Enter customer ID to update: ")

        if customer_id is None:
            print("Update cancelled.")
            return

        print("1. Email")
        print("2. Phone Number")
        print("3. Billing Address")

        choice = input("Enter your choice: ")

        if choice == "1":
            column_name = "email"
            new_value = requiredinput("Enter new email: ")
        elif choice == "2":
            column_name = "phone_number"
            new_value = requiredinput("Enter new phone number: ")
        elif choice == "3":
            column_name = "billing_address"
            new_value = requiredinput("Enter new billing address: ")
        else:
            print("Invalid choice.")
            return

        update_query = f"UPDATE Customer SET {column_name} = %s WHERE customer_id = %s"

        try:
            cursor.execute(update_query, (new_value, customer_id))
            connection.commit()

            if cursor.rowcount == 0:
                print("No customer found with that ID.")
            else:
                print("Customer record updated successfully.")
        except mysql.connector.Error as e:
            connection.rollback()
            print("Error updating customer:", e)

    updatingcolumnnames = {
        "Author": ["first_name", "last_name"],
        "Genre": ["genre_name"],
        "Customer": ["first_name", "last_name", "email", "phone_number", "billing_address"],
        "Book": ["title", "price", "book_condition", "publication_year", "isbn", "author_id", "genre_id"],
        "TransactionSale": ["transaction_sale_date", "total_transaction_sale_amount", "transaction_sale_status", "customer_id"],
        "TransactionItem": ["quantity", "book_id", "transaction_sale_id"],
        "Payment": ["payment_method", "payment_date", "payment_amount", "transaction_sale_id"],
        "Review": ["comment", "review_date", "rating", "customer_id", "book_id"]}

    def updaterecord(table_name, primary_key):
        print(f"\nUpdate Record in {table_name}")
        print("Type 'exit' at any time to cancel.\n")

        viewtable(table_name)

        record_id = integerinput(f"Enter {primary_key} of the record to update: ")

        if record_id is None:
            print("Update cancelled.")
            return

        columns = updatingcolumnnames.get(table_name)

        if not columns:
            print("No updatable columns found.")
            return

        print("\nWhich field would you like to update?\n")

        for index, column in enumerate(columns, start=1):
            print(f"{index}. {column}")

        choice = integerinput("\nEnter your choice: ")

        if choice is None or choice < 1 or choice > len(columns):
            print("Invalid choice.")
            return

        column_name = columns[choice - 1]

        new_value = requiredinput(f"Enter new value for {column_name}: ")

        if new_value is None:
            print("Update cancelled.")
            return

        update_query = f"UPDATE {table_name} SET {column_name} = %s WHERE {primary_key} = %s"

        try:
            cursor.execute(update_query, (new_value, record_id))
            connection.commit()

            if cursor.rowcount == 0:
                print("No matching record found.")
            else:
                print(f"{table_name} record updated successfully.")

        except mysql.connector.Error as e:
            connection.rollback()
            print("Error updating record:", e)

    def updatedata():
        while True:
            print("\nTable Updates - Menu\n")
            print("Update data in any selected table from BetterWorld Books Database\n")
            print("1. Update Author")
            print("2. Update Book")
            print("3. Update Customer")
            print("4. Update Genre")
            print("5. Update Payment")
            print("6. Update Review")
            print("7. Update Transaction Item")
            print("8. Update Transaction Sale")
            print("9. Back to Main Menu\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                updaterecord("Author", "author_id")

            elif choice == "2":
                updaterecord("Book", "book_id")

            elif choice == "3":
                updaterecord("Customer", "customer_id")

            elif choice == "4":
                updaterecord("Genre", "genre_id")

            elif choice == "5":
                updaterecord("Payment", "payment_id")

            elif choice == "6":
                updaterecord("Review", "review_id")

            elif choice == "7":
                updaterecord("TransactionItem", "transaction_item_id")

            elif choice == "8":
                updaterecord("TransactionSale", "transaction_sale_id")

            elif choice == "9":
                break

            else:
                print("Invalid choice. Please select a valid option.")


    def runquery(query_name, select_query, description=None, params=None):
        print(f"\n{query_name}")

        if description:
            print(description)

        try:
            cursor.execute(select_query, params)
            records = cursor.fetchall()

            if not records:
                print("No results found.")
                return

            for record in records:
                print(record)

            print("Report executed successfully.")

        except mysql.connector.Error as e:
            print("Error running report:", e)


    def choosegenre():
        cursor.execute("SELECT genre_name FROM Genre ORDER BY genre_name")
        genres = cursor.fetchall()

        print("\nChoose benchmark genre:")

        for index, genre in enumerate(genres, start=1):
            print(f"{index}. {genre[0]}")

        choice = integerinput("Enter genre number: ")

        if choice is None or choice < 1 or choice > len(genres):
            print("Invalid genre choice.")
            return None

        return genres[choice - 1][0]


    def complexqueries():
        while True:
            print("\nComplex Queries - Menu\n")
            print("1. View Multi-Book Transactions")
            print("   Shows which transaction has multiple books purchased.")
            print("   Functions Used: Set membership IN, GROUP BY, HAVING, COUNT\n")
            print("2. View Sales by Genre")
            print("   Show which genre of books sell the most at BetterWorld Books")
            print("   Functions Used: aggregate functions using SUM(), GROUP BY\n")
            print("3. Rank Books by Customer Rating")
            print("   Rank all books from highest to lowest rating")
            print("   Functions Used: OLAP/window function using RANK() OVER, subquery, AVG(), GROUP BY\n")
            print("4. View Revenue Rollup by Genre and Payment Method")
            print("   Show transaction sales total amounts by genre & grand totals of all totals for each genre.")
            print("   Functions Used: OLAP query using WITH ROLLUP, SUM(), GROUP BY\n")
            print("5. Smart Value Book Recommendations")
            print("   Shows affordable, used-books compared against a chosen benchmark genre")
            print("   Functions Used: Set comparison using ALL and subqueries\n")
            print("6. View Most Used Payment Methods")
            print("   Shows which payment methods have been used the most in transactions by customers.")
            print("   Functions Used: Set operation using UNION, COUNT(), GROUP BY\n")
            print("7. View Customer Loyalty Ranking")
            print("   Show total spending for each customer & compare it in a list for loyalty program analysis")
            print("   Functions Used: Subquery using WITH clause, OLAP/window function using DENSE_RANK()\n")
            print("8. Back to Main Menu\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                query = """
                SELECT
                    ts.transaction_sale_id,
                    ts.transaction_sale_date,
                    ts.transaction_sale_status,
                    b.title,
                    ti.quantity,
                    ts.total_transaction_sale_amount
                FROM TransactionSale ts
                JOIN TransactionItem ti ON ts.transaction_sale_id = ti.transaction_sale_id
                JOIN Book b ON ti.book_id = b.book_id
                WHERE ts.transaction_sale_id IN (
                    SELECT transaction_sale_id
                    FROM TransactionItem
                    GROUP BY transaction_sale_id
                    HAVING COUNT(book_id) > 1
                )
                ORDER BY ts.transaction_sale_id
                """
                runquery("Multi-Book Transactions", query)

            elif choice == "2":
                query = """
                SELECT
                    genre_name,
                    ROUND(SUM(b.price * ti.quantity), 2) AS total_sales
                FROM Genre g
                JOIN Book b ON g.genre_id = b.genre_id
                JOIN TransactionItem ti ON b.book_id = ti.book_id
                JOIN TransactionSale ts ON ti.transaction_sale_id = ts.transaction_sale_id
                GROUP BY g.genre_name
                ORDER BY total_sales DESC
                """
                runquery("Sales by Genre", query)

            elif choice == "3":
                query = """
                SELECT
                    title,
                    first_name,
                    last_name,
                    genre_name,
                    average_rating,
                    RANK() OVER (ORDER BY average_rating DESC) AS book_rank
                FROM (
                    SELECT
                        b.title,
                        a.first_name,
                        a.last_name,
                        g.genre_name,
                        AVG(r.rating) AS average_rating
                    FROM Book b
                    JOIN Author a ON b.author_id = a.author_id
                    JOIN Genre g ON b.genre_id = g.genre_id
                    JOIN Review r ON b.book_id = r.book_id
                    GROUP BY b.book_id, b.title, a.first_name, a.last_name, g.genre_name
                ) ranked_books
                ORDER BY book_rank ASC
                """
                runquery("Rank Books by Customer Rating", query)

            elif choice == "4":
                query = """
                SELECT
                    genre_name,
                    p.payment_method,
                    SUM(b.price * ti.quantity) AS total_sales
                FROM Genre g
                JOIN Book b ON g.genre_id = b.genre_id
                JOIN TransactionItem ti ON b.book_id = ti.book_id
                JOIN TransactionSale ts ON ti.transaction_sale_id = ts.transaction_sale_id
                JOIN Payment p ON ts.transaction_sale_id = p.transaction_sale_id
                GROUP BY g.genre_name, p.payment_method WITH ROLLUP
                """
                runquery("Revenue Rollup by Genre and Payment Method", query)

            elif choice == "5":
                benchmarkgenre = choosegenre()

                if benchmarkgenre is None:
                    continue

                query = """
                SELECT
                    title,
                    a.first_name,
                    a.last_name,
                    g.genre_name,
                    price,
                    book_condition,
                    AVG(r.rating) AS average_rating
                FROM Book b
                JOIN Author a ON b.author_id = a.author_id
                JOIN Genre g ON b.genre_id = g.genre_id
                JOIN Review r ON b.book_id = r.book_id
                WHERE price BETWEEN 10 AND 15
                AND book_condition LIKE 'Used - Good%'
                GROUP BY
                    b.book_id, title, a.first_name, a.last_name,
                    g.genre_name, price, book_condition
                HAVING price < ALL (
                    SELECT price
                    FROM Book
                    WHERE genre_id = (
                        SELECT genre_id
                        FROM Genre
                        WHERE genre_name = %s
                    )
                )
                ORDER BY average_rating DESC
                """
                runquery("Smart Value Book Recommendations", query, params=(benchmarkgenre,))

            elif choice == "6":
                query = """
                SELECT
                    payment_method AS category,
                    'Payment Method' AS category_type,
                    COUNT(payment_id) AS total_count,
                    SUM(payment_amount) AS total_amount
                FROM Payment
                GROUP BY payment_method

                UNION

                SELECT
                    transaction_sale_status AS category,
                    'Transaction Status' AS category_type,
                    COUNT(transaction_sale_id) AS total_count,
                    SUM(total_transaction_sale_amount) AS total_amount
                FROM TransactionSale
                GROUP BY transaction_sale_status

                ORDER BY total_amount DESC
                """
                runquery("Payment and Transaction Summary", query)

            elif choice == "7":
                query = """
                WITH ranked_customers AS (
                    SELECT
                        c.customer_id,
                        c.first_name,
                        c.last_name,
                        SUM(ts.total_transaction_sale_amount) AS total_spent
                    FROM Customer c
                    JOIN TransactionSale ts ON c.customer_id = ts.customer_id
                    GROUP BY c.customer_id, c.first_name, c.last_name
                )
                SELECT
                    customer_id,
                    first_name,
                    last_name,
                    total_spent,
                    DENSE_RANK() OVER (ORDER BY total_spent DESC) AS customer_rank
                FROM ranked_customers
                ORDER BY customer_rank ASC
                """
                runquery("Customer Loyalty Ranking", query)

            elif choice == "8":
                break
            else:
                print("Invalid choice. Please select a valid option.")


    def main():
        while True:
            print("\nBetterWorld Books Management System - Main Menu\n")
            print("1. View Tables")
            print("   Display data from any selected table from BetterWorld Books Database\n")
            print("2. Table Inserts")
            print("   Add data to any selected table from BetterWorld Books Database\n")
            print("3. Table Deletes")
            print("   Delete data in any selected table from BetterWorld Books Database\n")
            print("4. Table Updates")
            print("   Update data in any selected table from BetterWorld Books Database\n")
            print("5. Complex Queries")
            print("   Run complex SQL queries on data in BetterWorld Books Database for business analysis\n")
            print("6. Exit\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                readdata()
            elif choice == "2":
                writedata()
            elif choice == "3":
                deletedata()
            elif choice == "4":
                updatedata()
            elif choice == "5":
                complexqueries()
            elif choice == "6":
                print("Exiting BetterWorld Books Management System.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


    if __name__ == "__main__":
        main()


except mysql.connector.Error as e:
    print("Error:", e)


finally:
    if 'cursor' in locals():
        cursor.close()

    if 'connection' in locals() and connection.is_connected():
        connection.close()

    print("Connection to MySQL database closed")
