numbers = [1, 2, 3, 999, -1]
empty = []


print(min(numbers))

print(min(empty, default=0))

# print(min(1, 2, 3, 999, -1))


def addition(*args, key=""):
    result = 0
    for n in args:
        result += n
    return result


addition(1, 2, 3, 99, key="Test")
