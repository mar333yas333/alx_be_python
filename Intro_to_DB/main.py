import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iammarwan",
    database="alx_book_store"
)

# Create a cursor
cursor = mydb.cursor()

# Example: Retrieve all books with their authors
query = """
SELECT b.title, a.author_name, b.price, b.publication_date
FROM BOOKS b
JOIN AUTHORS a ON b.author_id = a.author_id;
"""

cursor.execute(query)
rows = cursor.fetchall()

# Print formatted output
print(f"{'Title':<40} | {'Author':<20} | {'Price':<6} | {'Date'}")
print("-" * 80)
for row in rows:
    print(f"{row[0]:<40} | {row[1]:<20} | {row[2]:<6} | {row[3]}")

cursor.close()
mydb.close()
