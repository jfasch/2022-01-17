from passwd import UserDataBase
import sys


db = UserDataBase('/etc/passwd')
jfasch = db.search('jfasch')

# --- UID is int
if type(jfasch.uid) != int:
    print('FAILED: uid not int', file=sys.stderr)
    sys.exit(1)

# --- userrecord has attributes
jfasch.uid
jfasch.gid
jfasch.home
jfasch.shell

sys.exit(0)

