def even_numbers(max):
    for num in range(max):
        if num % 2 == 0:
            yield num

for num in even_numbers(100):
    print(num)
