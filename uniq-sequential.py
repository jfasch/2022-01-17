input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output_list = []


for num in input_list:
    if not num in output_list:
        output_list.append(num)

for num in output_list:
    print(num)
