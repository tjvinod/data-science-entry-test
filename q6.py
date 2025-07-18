def find_first_negative(lst):
    x = 0
    while x < len(lst):
        if lst[x] < 0:
            return lst[x]
        x += 1
    return "No negatives"


# Task 2
scenario1 = find_first_negative([3, 5, -1, 7, -2, 8])
scenario2 = find_first_negative([2, 10, 7, 0])
print(scenario1) 
print(scenario2)
