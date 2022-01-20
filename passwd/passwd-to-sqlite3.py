from passwd import UserDataBase

import sys
import sqlite3    # mysql, postgres


PASSWD_FILENAME = sys.argv[1]
SQLITE3_FILENAME = sys.argv[2]

passwd_db = UserDataBase(PASSWD_FILENAME)
sql_db = sqlite3.connect(SQLITE3_FILENAME)

cursor = sql_db.cursor()
cursor.execute('create table users (uid integer, gid integer, username text, description text, home text, shell text)')

for user in passwd_db.all_users():
    cursor.execute(f'insert into users values ({user.uid}, {user.gid}, "{user.username}", "{user.description}", "{user.home}", "{user.shell}")')

sql_db.commit()

    
