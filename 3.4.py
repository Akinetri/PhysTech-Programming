def new_list(lst):
    while len(lst) > 1:
        edge_sum = lst[0] + lst[-1]
        middle_sum = sum(lst[1:-1])
        if edge_sum == middle_sum:
            return lst
        else:
            lst = lst[1:-1]
    if len(lst) == 0:
        return []
    else:
        lst

print(new_list([1,2,3,4,5])) # должно вернуть []
print(new_list([1,-1])) # должно вернуть [1,-1]
print(new_list([100,0,-100])) # должно вернуть [100,0,-100]
