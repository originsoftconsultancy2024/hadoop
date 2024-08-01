#!/usr/bin/env python3

import sys

# Read data from standard input

transactions = []

for line in sys.stdin:

	transactions.append(line)
    
for record in transactions:

	print (record)
