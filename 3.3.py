def repeat_sum(l):
    repeated_numbers = {}
    for sublist in l:
        unique_numbers = set(sublist)
        for number in unique_numbers:
            repeated_numbers[number] = repeated_numbers.get(number, 0) + 1
    return sum(number for number, count in repeated_numbers.items() if count >= 2)

print(repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])) # --> 10
print(repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]])) # --> 0
print(repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])) # --> 9