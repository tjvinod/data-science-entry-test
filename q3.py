def update_dictionary(dct, key, value):
    if key in dct:
        print(dct, key, dct[key])
    dct[key] = value
    print(dct, dct[key])
    return dct

# Task 2
answer1 = update_dictionary({}, "name", "Alice")
answer2 = update_dictionary({"age": 25}, "age", 26)
print(answer1)
print(answer2)
