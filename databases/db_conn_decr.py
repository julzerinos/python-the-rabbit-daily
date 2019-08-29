import contextlib
import sqlite3
from sqlite3 import Error


@contextlib.contextmanager
def dbconnect(database):
    
    conn = sqlite3.connect(database)

    yield conn
    
    conn.close()