import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234Abcd",
)

cursor = db_connection.cursor()

cursor.execute("CREATE DATABASE airport")

print("Database 'airport' table created")


cursor.close()
db_connection.close()