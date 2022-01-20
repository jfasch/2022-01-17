def uniq(numbers):
    output_list = []
    have = set()
    for num in numbers:
        if not num in have:
            output_list.append(num)
            have.add(num)
    return output_list

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output_list = uniq(input_list)
for element in output_list:
    print(element)
