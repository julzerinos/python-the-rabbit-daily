import sys

from db_conn_decr import dbconnect
from db_actions import subs_insert_subs, subs_view_subs


if len(sys.argv) < 2:
    raise SystemExit

with dbconnect('databases/subscribers.db') as conn:
    subs_insert_subs(conn, sys.argv[1:])
    print(subs_view_subs(conn))