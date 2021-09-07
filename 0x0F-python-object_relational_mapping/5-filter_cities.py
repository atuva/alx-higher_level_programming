#!/usr/bin/python3
'''
Contains a MySQLdb script that performs read operations on a database
It lists all states with a name starting with "N"
'''


import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db_location = 'localhost'
    port = 3306

    state = argv[4]
    db = MySQLdb.connect(host=db_location,
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=port)

    cursor = db.cursor()
    sql = """SELECT cities.name FROM states
            INNER JOIN cities ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id ASC"""

    cursor.execute(sql, (state,))
    data = cursor.fetchall()

    # Instead of using for loop with a lot of conditions
    # Create a list of items and then join them with ", "
    print(", ".join([city[0] for city in data]))
    db.close()
