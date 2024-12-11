def fruit_and_animals(s):
    all_fruits = 0
    transferred = 0
    words = s.split()

    for i, word in enumerate(words):
        if word.isdigit():
            number = int(word)
            if i > 0 and words[i - 1] in {"has", "had"}:
                all_fruits += number
            elif i > 0 and words[i - 1] in {"gave", "took"}:
                if words[i - 1] == "gave":
                    transferred += number
                elif words[i - 1] == "took":
                    transferred -= number
    return all_fruits - transferred

print(fruit_and_animals('The monkey has 10 apples and gave 3')) # должно вернуть 7
print(fruit_and_animals('The cat has 13 oranges and took 6')) # должно вернуть 19
print(fruit_and_animals('Kangaroo had 254 bananas and gave 1 banana')) # должно вернуть 253
