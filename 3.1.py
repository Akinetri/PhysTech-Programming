def floyd_line(n):
    i = 1 # конечный член строки
    p = 1 # разница между конечными членами строк
    z = 1 # номер строки
    while n > i:
        p = p + 1
        i = i + p
        z = z + 1
    print(z)
print(floyd_line(26))