from db_conn_decr import dbconnect
from db_actions import subs_insert_subs, subs_view_subs


with dbconnect('databases/subscribers.db') as conn:
    subs_insert_subs(conn, ['kornel1902@gmail.com',])
    print(subs_view_subs(conn))