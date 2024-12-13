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

# Insert 50,000 Records and Measure Execution Time
print("\nInserting 50,000 records into ClimateData and measuring execution time...")
start_time = time.time()
for i in range(50000):
    cursor.execute(
        """
        INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity)
        VALUES (%s, %s, %s, %s, %s);
        """,
        (f"Location-{i}", "2024-01-03", i % 50 + 10.0, i % 20 + 5.0, i % 100 + 50.0)
    )
db_connection.commit()
end_time = time.time()
execution_time = end_time - start_time
print(f"Time taken to insert 50,000 records: {execution_time:.2f} seconds")

# Measure Execution Time for Multiple Queries
print("\nMeasuring Execution Time for Multiple Queries on ClimateData Table")
queries = [
    "SELECT * FROM ClimateData WHERE temperature > 30 LIMIT 10;",
    "SELECT COUNT(*) FROM ClimateData;",
    "SELECT * FROM ClimateData WHERE location = 'Location-10';",
    "SELECT * FROM ClimateData WHERE record_date = '2024-01-03' AND humidity > 70;"
]
for query in queries:
    start = time.time()
    cursor.execute(query)
    end = time.time()
    execution_time_ms = (end - start) * 1000  # Convert to milliseconds
    print(f"Query: {query} | Execution Time: {execution_time_ms:.2f} ms")

# Close the cursor and connection
cursor.close()
db_connection.close()
