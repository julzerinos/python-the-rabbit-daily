import sqlite3
import datetime
import time

conn = sqlite3.connect('rabbits.db')

c = conn.cursor()

c.execute(
    '''CREATE TABLE IF NOT EXISTS rabbits
    (
        rabbit_id INTEGER PRIMARY KEY,
        date_added DATE,
        link VARCHAR(2083) NOT NULL UNIQUE
        )'''
             )

c.execute(
    '''INSERT OR IGNORE INTO rabbits (rabbit_id, date_added, link)
    VALUES (
        1,
        ?,
        'https://www.telegraph.co.uk/content/dam/pets/2016/03/18/bunny_trans_NvBQzQNjv4BqqVzuuqpFlyLIwiB6NTmJwfSVWeZ_vEN7c6bHu2jJnT8.jpg?imwidth=450'
        )''',
        (datetime.datetime.today().strftime('%Y-%m-%d'),)
    )

conn.commit()

c.execute(
    '''SELECT * FROM rabbits'''
             )

print(c.fetchall())

conn.close()