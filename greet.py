import sys


name = input('Name: ')
sex = input('Sex (m,f): ')   # 'f', 'F', 'm', 'M'
sex = sex.upper()
hour_of_day = int(input('Hour of day (0-23): '))

msg = ''

if 0 <= hour_of_day < 10:
    msg += 'Good morning, '
elif 10 <= hour_of_day < 18:
    msg += 'Good day, '
elif 18 <= hour_of_day < 24:
    msg += 'Good evening, '
else:
    print('Invalid hour of day:', hour_of_day, file=sys.stderr)
    sys.exit(1)

if sex == 'M':
    msg += 'Mr. '
elif sex == 'F':
    msg += 'Mrs. '
else:
    print('Invalid sex:', sex, file=sys.stderr)
    sys.exit(1)

msg += name    

print(msg)

