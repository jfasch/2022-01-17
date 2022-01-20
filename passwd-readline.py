f = open('/etc/passwd')

while True:
    line = f.readline()
    if line == '':    # EOF (end-of-file)
        break
    else:
        print(line.rstrip())
