def find_and_replace(lst, find_val, replace_val):
    if type(lst) != list:
        return -1
    for x in range(len(lst)):
        if lst[x] == find_val:
            lst[x] = replace_val
    return lst


# Task 2
answer1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
answer2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(answer1)
print(answer2)