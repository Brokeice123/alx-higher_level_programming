#!/usr/bin/python3
"""
A Scrript that takes in the name of a state as an argument and lists all
cities of that state,
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = '{}'".format(argv[4]))
    print(", ".join([row[1] for row in cur.fetchall()]))
    cur.close()
    db.close()
