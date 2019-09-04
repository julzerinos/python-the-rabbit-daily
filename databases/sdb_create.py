import sqlite3
import datetime
import time

from db_conn_decr import dbconnect


with dbconnect('databases/subscribers.db') as conn:

    c = conn.cursor()

    # INTEGER PRIMARY KEY auto-increments under sqlite
    c.execute(
        '''CREATE TABLE IF NOT EXISTS subscribers
        (
            subs_id INTEGER PRIMARY KEY,
            email VARCHAR(2083) NOT NULL UNIQUE,
            date_added DATE,
            subs_type INTEGER,
            rabbits_recv INTEGER DEFAULT 0
            )'''
                 )

    c.execute(
        '''INSERT OR IGNORE INTO subscribers (date_added, email, subs_type)
        VALUES (
            ?,
            "therabbitdaily@gmail.com",
            1
            )''',
            (datetime.datetime.today().strftime('%Y-%m-%d'),),
        )

    c.execute(
        '''CREATE VIEW IF NOT EXISTS vw_users_daily
        AS
        SELECT * FROM subscribers where subs_type = 1
        '''
    )

    c.execute(
        '''CREATE VIEW IF NOT EXISTS vw_users_weekly
        AS
        SELECT * FROM subscribers where subs_type = 2
        '''
    )

    conn.commit()
