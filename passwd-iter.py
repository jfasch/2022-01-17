f = open('/etc/passwd')

for line in f:
    print(line.rstrip())
