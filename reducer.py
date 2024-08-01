#!/usr/bin/env python3

import sys

count = 0
summation = 0.0

for line in sys.stdin:

	try:
		words = line.split(':')
		final_list = words[2].split(',')
		price = final_list[0]
		price = ''.join(l for l in price if l != '"')
		price = float(price)
		summation += price
		count += 1
	except:
		continue

avg = summation/count

print(f"Average price of bitcoin is {avg}")
	



