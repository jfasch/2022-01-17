'''Das hier ist der docstring des ganzen moduls.

Hier koennte auch noch was supergscheites stehen, 
aber naja wir haben besseres zu tun.
'''


class UserData:
    def __init__(self, uid, gid, username, description, home, shell):
        self.uid = uid
        self.gid = gid
        self.username = username
        self.description = description
        self.home = home
        self.shell = shell

    def __str__(self):
        return f'''User: {self.username}
UID: {self.uid}
GID: {self.gid}
Description: {self.description}
Home: {self.home}
Shell: {self.shell}
'''

    def commit_suicide(self):
        print('BOOM!')

class UserDataBase:
    def __init__(self, filename):
        '''read passwd file into big fat dictionary, the userdatabase'''
        self.mydict = {}
        
        f = open(filename)
        for line in f:
            line = line.rstrip('\n')
        
            # tuple unpacking
            my_username, my_password, my_uid, my_gid, my_description, my_home, my_shell = line.split(':')
            userrecord = UserData(username=my_username, 
                                  uid=int(my_uid), 
                                  gid=int(my_gid), 
                                  home=my_home, 
                                  shell=my_shell, 
                                  description=my_description)
    
            self.mydict[my_username] = userrecord
    
    def search(self, username):
        '''keine ahnung, was ich hier schreiben soll.
        weil der lehrer hat gesagt, wenn man die funktionen 
        und ihre parameter so nennt, wie das, was sie tut, 
        dann brauch ich nix dokumentieren.
        '''
        return self.mydict[username]

    def all_users(self):
        users = []
        for user in self.mydict.values():
            users.append(user)
        return users
