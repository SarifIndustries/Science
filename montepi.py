#!/usr/bin/env python3

title="""
#==========================================#
#=  VALUE OF PI USING MONTE-CARLO METHOD  =#
#==========================================#
"""

from random import Random
from math import sqrt

def is_point_in_circle_segment(x: float, y: float) -> bool:
	return x * x + y * y < 1

#===================== MAIN =====================

def main():
	print(title)
	r = Random()
	points_in, points_out = 0, 0
	for i in range(1000000):
		x = r.random()
		y = r.random()
		if is_point_in_circle_segment(x, y):
			points_in += 1
		else:
			points_out += 1
	print(f"Points inside circle segment: \t{points_in}")
	print(f"Points outside circle segment: \t{points_out}")
	# Calculate Area difference
	pi = sqrt(4 * points_in / points_out)
	print(f"Pi value = {pi}") # TODO: check why this is incorrect.

#================================================

if __name__ == "__main__":
	main()
