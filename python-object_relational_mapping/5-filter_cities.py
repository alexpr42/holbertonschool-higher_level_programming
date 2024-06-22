#!/usr/bin/python3
"""
This script lists all cities of a given state from the database
hbtn_0e_4_usa.

The script takes 4 arguments: mysql username, mysql password, database
name, and state name. It connects to a MySQL server running on
localhost at port 3306, retrieves all cities of the given state,
and displays them sorted by city id in ascending order.
"""

import MySQLdb
import sys


def main():
    # Retrieve the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities of the given state
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows from the executed query
    cities = cursor.fetchall()

    # Print the cities, separated by commas
    print(", ".join([city[0] for city in cities]))

    # Close the cursor and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
