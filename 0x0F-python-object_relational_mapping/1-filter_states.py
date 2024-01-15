#!/usr/bin/python3
"""  lists all states that start with N"""
import MySQLdb
import sys


if __name__ == "__main__":
  db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
  cursor = db.cursor()
  cursor.execute("SELECT * FROM states WHERE name like "N%" ")
  result = cursor.fetchall()
  for i in result:
    print(i)
  cursor.close()
  db.close()
