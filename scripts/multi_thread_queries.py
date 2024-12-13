import pymysql
from concurrent.futures import ThreadPoolExecutor
import time

# Insert Query - Single Record
insert_sql = """
INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity)
VALUES ('San Francisco', '2024-01-03', 15.0, 7.0, 75.0);
"""

# Select Query
select_sql = "SELECT * FROM ClimateData WHERE temperature > 20;"

# Update Query
update_sql = "UPDATE ClimateData SET humidity = 80.0 WHERE location = 'New York';"

def execute_query(query, params=None):
    connection = pymysql.connect(
        host="automated-mysql-server4.mysql.database.azure.com",
        user="root_nav",
        password="Secret55",
        database="project_db",
        ssl={'ssl': True}
    )
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        connection.commit()
    connection.close()

# Concurrent Queries
with ThreadPoolExecutor() as executor:
    executor.submit(execute_query, insert_sql)
    executor.submit(execute_query, select_sql)
    executor.submit(execute_query, update_sql)

# Bulk Insert
print("\nInserting 50,0000 records into ClimateData and measuring execution time...")
connection = pymysql.connect(
    host="automated-mysql-server4.mysql.database.azure.com",
    user="root_nav",
    password="Secret55",
    database="project_db",
    ssl={'ssl': True}
)
cursor = connection.cursor()
start_time = time.time()

bulk_data = [
    (f"Location-{i}", "2024-01-03", i % 50 + 10.0, i % 20 + 5.0, i % 100 + 50.0)
    for i in range(500000)
]
cursor.executemany(
    """
    INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity)
    VALUES (%s, %s, %s, %s, %s);
    """,
    bulk_data
)
connection.commit()
end_time = time.time()
execution_time = end_time - start_time
print(f"Time taken to insert 50,0000 records: {execution_time:.2f} seconds")

cursor.close()
connection.close()
