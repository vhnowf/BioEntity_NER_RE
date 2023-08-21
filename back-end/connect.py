import mysql.connector

# Connection parameters
host = 'localhost'
user = 'root'
password = 'abcd@1234'
database = 'bio_db'

# Establish the connection
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Create a cursor
cursor = conn.cursor()

# Execute queries, fetch data, etc.
# For example:
cursor.execute("SELECT * FROM articles")
rows = cursor.fetchall()
for row in rows:
    print(row)

