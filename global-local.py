x = 666

def f():
    global x
    x = 42
    print(x)

f()

print(x)
