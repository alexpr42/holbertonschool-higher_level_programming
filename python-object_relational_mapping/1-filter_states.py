#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' (upper N)
from the database hbtn_0e_0_usa.

The script takes 3 arguments: mysql username, mysql password, and
database name. It connects to a MySQL server running on localhost
at port 3306, retrieves all states starting with 'N', and displays
them sorted by state id in ascending order.
"""

import MySQLdb
import sys


def main():
    # Retrieve the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute the SQL query to retrieve states starting with 'N'
    query = (
            "SELECT id, name FROM states WHERE BINARY name LIKE 'N%'
            ORDER BY id ASC")
    cursor.execute(query)

    # Fetch all the rows from the executed query
    states = cursor.fetchall()

    # Print the rows
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
