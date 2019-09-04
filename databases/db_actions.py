import datetime
import time
import re

try:
    from databases.db_conn_decr import dbconnect
except ModuleNotFoundError:
    from db_conn_decr import dbconnect

def subs_insert_subs(conn, emails, stype=1):
    c = conn.cursor()
    valid_rows = [
        (datetime.datetime.today().strftime('%Y-%m-%d'), email, stype)
        for email in emails if re.fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
    ]
    c.executemany(
        '''INSERT OR IGNORE INTO subscribers (date_added, email, subs_type)
        VALUES (
            ?,
            ?,
            ?
            )''',
            valid_rows,
        )
    if len(valid_rows) != len(emails):
        print(
            f"The following emails in invalid format were not added: {set(emails) - set(row[1] for row in valid_rows)}"
            )

    conn.commit()
    return len(valid_rows)


def subs_view_subs(conn, stype=0, test=False):
    c = conn.cursor()
    if test:
        c.execute(
            '''SELECT * FROM subscribers
            WHERE subs_id = 1
            '''
            )
    
    elif stype == 0:
        c.execute(
            '''SELECT * FROM subscribers
            '''
            )
    else:
        c.execute(
            '''SELECT * FROM subscribers
            WHERE subs_type = ?
            ''',
            (stype,)
            )

    return c.fetchall()


def subs_update_subs(conn, sid):
    c = conn.cursor()

    c.execute(
        '''UPDATE subscribers
        SET rabbits_recv = rabbits_recv + 1
        WHERE subs_id = ?
        ''',
        (sid,)
        )

    conn.commit()
