import sys

filename = sys.argv[1]

f = open(filename)
for line in f:
    output_line = line.rstrip('\n')

    comment_pos = line.find('#')
    if comment_pos >= 0:
        line = line[:comment_pos]
    line = line.strip()
    if len(line) > 0:
        print(output_line)
