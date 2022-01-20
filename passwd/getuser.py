import sys
import passwd


FILENAME = sys.argv[1]
USERS = []
if len(sys.argv) > 2:
    USERS = sys.argv[2:]

userdatabase = passwd.create_db(FILENAME)
for name in USERS:
    record = passwd.search_db(userdatabase, name)

    print(f"""User: {name}
UID: {record['uid']}
GID: {record['gid']}
Home: {record['home']}
Shell: {record['shell']}""")
