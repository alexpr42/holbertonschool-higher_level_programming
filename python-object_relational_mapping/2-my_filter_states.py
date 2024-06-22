#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

The script takes 4 arguments: mysql username, mysql password, database name,
and state name searched. It connects to a MySQL server running on localhost at
port 3306, retrieves states with the given name, and displays them sorted by
state id in ascending order.
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

    # Execute the SQL query to retrieve states matching the given name
    query = (
        "SELECT id, name FROM states WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(state_name)
    )
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
