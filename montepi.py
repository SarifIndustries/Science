#!/usr/bin/env python3

title="""
#==========================================#
#=  VALUE OF PI USING MONTE-CARLO METHOD  =#
#==========================================#
"""

# Amount of points to drop.
TOTAL_POINTS = 10000000

from random import Random
from math import sqrt

def did_point_land_inside_circle_segment(x: float, y: float) -> bool:
	return x * x + y * y <= 1

#===================== MAIN =====================

def main():
	print(title)
	r = Random()
	total_points = TOTAL_POINTS
	inner_points = 0
	# Throwing points into area
	print("Start dropping points...")
	for i in range(total_points):
		x, y = r.random(), r.random()
		if did_point_land_inside_circle_segment(x, y):
			inner_points += 1
	# Total points
	print(f"Points inside circle segment: \t{inner_points}")
	print(f"Total points dropped:         \t{total_points}")
	# Calculate Pi using area difference
	pi = 4 * inner_points / total_points
	print(f"Pi value = \t[ {pi} ]")

#================================================

if __name__ == "__main__":
	main()
