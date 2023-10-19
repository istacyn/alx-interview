#!/usr/bin/python3
'''Reads stdin line by line and computes metrics'''

import sys


def print_metrics(dictionary, size):
    '''
    Prints the total file size and the counts
    for each status code in ascending order.
    '''
    print('File size: {:d}'.format(size))
    for i in sorted(dictionary.keys()):
        if dictionary[i] != 0:
            print('{}: {:d}'.format(i, dictionary[i]))

    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}

    count = 0
    size = 0

    try:
        for line in sys.stdin:
            if count != 0 and count % 10 == 0:
                print_metrics(status_codes, size)

            # Split line into components
            parts = line.split()
            count += 1

            try:
                size += int(parts[-1])
            except Exception:
                pass

            try:
                if parts[-2] in status_codes:
                    status_codes[parts[-2]] += 1
            except Exception:
                pass
        print_metrics(status_codes, size)

    except KeyboardInterrupt:
        print_metrics(status_codes, size)
        raise
