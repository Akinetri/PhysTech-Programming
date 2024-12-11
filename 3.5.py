def count_salutes(s):
    count_rights = 0
    total_salutes = 0

    for char in s:
        if char == '>':
            count_rights += 1
        elif char == '<':
            total_salutes += 2 * count_rights

    return total_salutes

print(count_salutes('>-<->-<'))