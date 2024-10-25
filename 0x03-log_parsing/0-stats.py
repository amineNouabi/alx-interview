#!/usr/bin/python3

"""

Log Parsing Script

"""

import sys

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0

try:
    for i, line in enumerate(sys.stdin, 1):
        tokens = line.split(" ")
        if len(tokens) < 2:
            continue
        status_code = tokens[-2]
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += int(tokens[-1])
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, value in status_codes.items():
                if value != 0:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, value in status_codes.items():
        if value != 0:
            print("{}: {}".format(key, value))
