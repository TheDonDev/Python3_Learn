import math
def min(values):
    smallest=None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest
values=[3, 41, 12, 9, 74, 15]
min(values)