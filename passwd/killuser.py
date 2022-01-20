import sys
import passwd


FILENAME = sys.argv[1]
USER = sys.argv[2]

db = passwd.UserDataBase(FILENAME)
user = db.search(USER)

user.commit_suicide()
