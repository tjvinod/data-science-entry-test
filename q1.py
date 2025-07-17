def swap(x, y):
    if not ((type(x) == int or type(x) == float or type(x) == complex) and (type(y) == int or type(y) == float or type(y) == complex)):
        return -1
    return y, x
    
#Task2    
answer1 = swap("Apple", 10)
answer2 = swap(9,17)
print(answer1)
print(answer2)