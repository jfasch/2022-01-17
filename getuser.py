import sys
import pprint


# --- commandline parsing
FILENAME = sys.argv[1]
USERS = []
if len(sys.argv) > 2:
    USERS = sys.argv[2:]

# --- read passwd file into big fat dictionary, the userdatabase
userdatabase = {}

f = open(FILENAME)    # jjj with
for line in f:
    line = line.rstrip('\n')

    # tuple unpacking
    username, password, uid, gid, description, home, shell = line.split(':')

    userrecord = {
        'uid': uid,
        'gid': gid,
        'home': home,
        'shell': shell,
    }
    userdatabase[username] = userrecord

# --- search names in USERS
for name in USERS:
    record = userdatabase[name]

    print(f"""User: {name}
UID: {record['uid']}
GID: {record['gid']}
Home: {record['home']}
Shell: {record['shell']}""")
