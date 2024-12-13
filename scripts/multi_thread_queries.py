import pymysql
from concurrent.futures import ThreadPoolExecutor
import time

# Database connection to Azure MySQL
db_connection = pymysql.connect(
    host="automated-mysql-server4.mysql.database.azure.com",
    user="root_nav",
    password="Secret55",
    database="project_db",
    ssl={'ssl': True}
)

# Creating the cursor for database operations
cursor = db_connection.cursor()

# Insert Query - Single Record
insert_sql = """
INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity)
VALUES ('San Francisco', '2024-01-03', 15.0, 7.0, 75.0);
"""
cursor.execute(insert_sql)
db_connection.commit()

# Select Query - Filter Data
select_sql = "SELECT * FROM ClimateData WHERE temperature > 20;"
cursor.execute(select_sql)
select_result = cursor.fetchall()
for row in select_result:
    print(row)

# Update Query
update_sql = "UPDATE ClimateData SET humidity = 80.0 WHERE location = 'New York';"
cursor.execute(update_sql)
db_connection.commit()

# Run concurrent queries using ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    executor.submit(cursor.execute, insert_sql)
    executor.submit(cursor.execute, select_sql)
    executor.submit(cursor.execute, update_sql)

# Close the cursor and connection
cursor.close()
db_connection.close()
