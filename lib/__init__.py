# lib/__init__.py
import sqlite3

# Provides a connection to the DB
CONN = sqlite3.connect('company.sqlite')
# Cursor is used to persist data to the DB
CURSOR = CONN.cursor()
