import sys

num = int(sys.argv[1])

# low hanging fruit
if num == 1:
    print('1 ist keine primzahl')
    sys.exit(0)

# eigentlicher algorithmus
for divisor_candidate in range(2, num//2 + 1):
    if num % divisor_candidate == 0:
        print(num, 'ist keine primzahl')
        break
else:
    print('ist eine primzahl')
