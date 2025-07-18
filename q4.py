def string_reverse(s):
    if not isinstance(s, str):
        return "Input must be a string"
    return s[::-1]

# Task 2
scenario1 = string_reverse("Hello World")
scenario2 = string_reverse("Python")
print(scenario1)
print(scenario2)