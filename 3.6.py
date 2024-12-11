def bracket_pairs(s):
    close = []
    open = []
    result = {}
    i = 0
    while i < len(s):
        if s[i] == '(':
            open.append(i)
        elif s[i] == ')':
            close.append(i)
            if len(open) != 0:
                last_open = open[-1]
                result[last_open] = i
                open = open[:-1]
        i += 1

    sorted_result = {k: result[k] for k in sorted(result)}
    if result == {} and (len(open) != 0 or len(close) != 0):
        return False
    else:
        return sorted_result


print(bracket_pairs("len(list)"))  # --> {3:8}
print(bracket_pairs("string"))  # --> {}
print(bracket_pairs(""))  # --> {}
print(bracket_pairs("def f(x"))  # --> False
print(bracket_pairs(")("))  # --> False
print(bracket_pairs("(a(b)c()d)"))  # --> {0:9,2:4,6:7}
print(bracket_pairs("f(x[0])"))  # --> {1:6}
print(bracket_pairs("lenlist)"))