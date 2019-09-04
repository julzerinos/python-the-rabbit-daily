from flask import render_template, request

from trdflask import trdflask

from databases.db_actions import subs_insert_subs
from databases.db_conn_decr import dbconnect

import config

@trdflask.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        with dbconnect(config.DB_PATH) as conn:
            subs_insert_subs(conn, [email,])
    return render_template('insert.html')