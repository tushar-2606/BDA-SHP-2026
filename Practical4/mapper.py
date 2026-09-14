#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    fields = line.split()

    if len(fields) >= 3:
        date = fields[1]
        temperature = fields[2]

        year = date[:4]

        try:
            temperature = int(temperature)
            print(f"{year}\t{temperature}")
        except ValueError:
            continue