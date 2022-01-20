'''Das hier ist der docstring des ganzen moduls.
Hier koennte auch noch was supergscheites stehen, 
aber naja wir haben besseres zu tun.
'''


def create_db(filename):
    '''read passwd file into big fat dictionary, the userdatabase'''
    db = {}
    
    f = open(filename)    # jjj with
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
        db[username] = userrecord

    return db

def search_db(db, username):
    '''keine ahnung, was ich hier schreiben soll.
    weil der lehrer hat gesagt, wenn man die funktionen 
    und ihre parameter so nennt, wie das, was sie tut, 
    dann brauch ich nix dokumentieren.
    '''
    return db[username]
