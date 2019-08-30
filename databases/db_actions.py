import datetime
import time

try:
    from databases.db_conn_decr import dbconnect
except ModuleNotFoundError:
    from db_conn_decr import dbconnect

def subs_insert_subs(conn, emails, stype=1):
    c = conn.cursor()
    for email in emails:
        c.execute(
            '''INSERT OR IGNORE INTO subscribers (date_added, email, subs_type)
            VALUES (
                ?,
                ?,
                ?
                )''',
                (datetime.datetime.today().strftime('%Y-%m-%d'),email,stype),
            )
    conn.commit()


def subs_view_subs(conn, stype=0, test=False):
    c = conn.cursor()
    if test:
        c.execute(
            '''SELECT * FROM subscribers
            WHERE subs_id = 1 OR subs_id = 4
            '''
            )
    
    if stype == 0:
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
