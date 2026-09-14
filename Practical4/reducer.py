#!/usr/bin/env python3

import sys

current_year = None
max_temperature = None

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    year, temperature = line.split("\t")

    try:
        temperature = int(temperature)
    except ValueError:
        continue

    if current_year == year:
        if temperature > max_temperature:
            max_temperature = temperature
    else:
        if current_year is not None:
            print(f"{current_year}\t{max_temperature}")

        current_year = year
        max_temperature = temperature

if current_year is not None:
    print(f"{current_year}\t{max_temperature}")