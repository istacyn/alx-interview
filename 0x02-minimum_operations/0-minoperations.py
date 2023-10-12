#!/usr/bin/python3
''' Minimum  number of operations needed
to result in exactly n H characters in the file.
'''


def minOperations(n):
    '''
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    '''
    current_chars = 1
    start = 0
    operations = 0

    while current_chars < n:
        remaining_chars = n - current_chars

        if (remaining_chars % current_chars == 0):
            start = current_chars
            current_chars += start
            operations += 2

        else:
            current_chars += start
            operations += 1

    return operations
