#!/usr/bin/env python3

title="""
#================================#
#=           SAIL FORCE         =#
#================================#
"""

import math
from math import sin

WIND_SPEED = 10
SAIL_AREA = 20
AIR_DENSITY = 1
GRANULARITY = 30

def force_forward(sail_angle: float, course: float) -> float:
	return (
		WIND_SPEED * WIND_SPEED * SAIL_AREA * AIR_DENSITY *
		sin(sail_angle) * sin(sail_angle) * sin(course - sail_angle)
	)

#===================== MAIN =====================

def main():
	print(title)
	course = float(input("Enter course to wind: "))
	for i in range(1, GRANULARITY + 1):
		sail_angle = (math.pi / 2 / GRANULARITY) * i
		force = force_forward(sail_angle, course)
		print(f"Sail angle [ {int(math.degrees(sail_angle))} ] --- Force: [ {force:.2f} ]")
	f = force_forward(0.2, course)
	print(f)

#================================================

if __name__ == "__main__":
	main()
