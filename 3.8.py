#нагомнокодил: Akinetri
def cats_and_mice(mapping, moves):
    cat_line = 0
    cat_column = 0
    mice_line = 0
    mice_column = 0
    line = 1
    column = 0
    cat_founded = False
    mice_founded = False
    for char in mapping:
        if char != " ":
            if char == "\n":
                line += 1
                column = 0
            else:
                column += 1
            if char == "C":
                cat_line = line
                cat_column = column
                cat_founded = True
            elif char == "m":
                mice_line = line
                mice_column = column
                mice_founded = True
    if not cat_founded or not mice_founded:
        print("We need two animals!")
    else:
        column_distance = abs(cat_column - mice_column)
        line_distance = abs(cat_line - mice_line)
        distance = column_distance + line_distance
        if distance <= moves:
            print("Caught!")
        else:
            print("Run!")


print(cats_and_mice("""\
            ..C......
            .........
            ....m....""", 6)) # должно вернуть Caught!
print(cats_and_mice("""\
            .C.......
            .........
            ......m..""", 6)) # должно вернуть Run!
print(cats_and_mice("""\
            ..C......
            .........
            .........""", 6)) # должно вернуть We need two animals!