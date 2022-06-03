def second_min(*args):
    sorted_list = sorted(args)
    return sorted_list[1]


def second_min2(*args):
    # Find minimum, delete it
    # Find minimum again -> this is second smallest
    numbers_list = list(args)
    minimum = min(numbers_list)
    numbers_list.remove(minimum)
    return min(numbers_list)


def second_min3(*args):
    if args[0] < args[1]:
        minima = [args[0], args[1]]
    else:
        minima = [args[1], args[0]]

    for n in args[2:]:
        if n < minima[0]:
            minima[1] = minima[0]
            minima[0] = n
        elif n < minima[1]:
            minima[1] = n

    return minima[1]


print(second_min(1, 7, 3, 9, 0, 10))
print(second_min2(1, 7, 3, 9, 0, 10))
print(second_min3(1, 7, 3, 9, 0, 10))
