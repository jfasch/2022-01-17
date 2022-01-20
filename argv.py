import sys

print(sys.argv)

if len(sys.argv) > 2:
    users = sys.argv[2:]

print(users)

# print('argv:', sys.argv)
# print('len:', len(sys.argv))
# print('argv[0]:', sys.argv[0])
# print('argv[1]:', sys.argv[1])
