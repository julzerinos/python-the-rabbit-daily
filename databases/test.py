from db_conn_decr import dbconnect
from db_actions import subs_insert_subs, subs_view_subs


with dbconnect('databases/subscribers.db') as conn:
    subs_insert_subs(conn, ['a.jablonska96@gmail.com', 'j.pawelec87@gmail.com', 'nibre0809@gmail.com'])
    print(subs_view_subs(conn))
