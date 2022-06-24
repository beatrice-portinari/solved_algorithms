'''
Iterative and recursive version of binary search algorithm
Best-case performance: O(1)
Worst-case performance: O(log n)

The recursive version of Binary Search has a space complexity of O(log N),
but the iterative version has a space complexity of O(log N) (1).
The recursive version is simple to build, the iterative form is more efficient.
'''


import random
# Generating random list of integers
random_list = random.sample(range(0, 10), 10)


def iterative_binary_search(lst, x):
    # Sorting is necessary for the correct operation of the algorithm
    lst.sort()
    start = 0
    end = len(lst) - 1
    while start <= end:
        # Finding a middle element
        middle = (start + end) // 2
        # If element is bigger than middle,
        # than it can only be presented in right sublist
        if lst[middle] < x:
            start = middle + 1
        # If element is smaller than middle,
        # it can only be presented in left sublist
        elif lst[middle] > x:
            end = middle - 1
        else:
            # Return this if middle element equals target element
            return f'Element {x} was found. Middle element is {middle}'
    # Return this if element is not present in list
    return f'Element {x} not found.'

print(random_list)
print(iterative_binary_search(random_list, 7))


# The same method using recursion
# Less efficient version of binary search
def recursive_binary_search(lst, start, end, x):
    lst.sort()
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] < x:
            recursive_binary_search(lst, middle + 1, end, x)
        if lst[middle] > x:
            recursive_binary_search(lst, start, middle - 1, x)
        else:
            return f'Element {x} was found. Middle element is {middle}'
    return f'Element {x} not found.'

print(random_list)
print(recursive_binary_search(random_list, 0, len(random_list) - 1, 7))
