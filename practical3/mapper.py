#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    line = line.strip().lower()
    line = re.sub(r'[^a-z0-9\s]', ' ', line)

    words = line.split()

    for word in words:
        print(f"{word}\t1")