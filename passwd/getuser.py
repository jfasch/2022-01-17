import sys
import passwd


FILENAME = sys.argv[1]
USERS = []
if len(sys.argv) > 2:
    USERS = sys.argv[2:]

db = passwd.UserDataBase(FILENAME)
for name in USERS:
    record = db.search(name)
    print(record)
