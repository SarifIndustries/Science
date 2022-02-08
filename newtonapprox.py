#!/usr/bin/env python3

#==================================#
#=  NEWTON-RAPHSON APPROXIMATION  =#
#==================================#
#
# 1. Enter function and derivative below.
# 2. Instead of entering derivative, try using calculated derivative.
# 3. Choose approximation steps and what derivative function to use.
# 3. Run program and enter your guess.

def f(x):
	return (
		# Enter function here:
		x * x * x - 100
	)


def defined_df(x):
	return (
		# Enter derivative here:
		3 * x * x
	)


# Use instead of defined derivative.
def calculated_df(x):
	delta = 0.000001
	return (f(x + delta) - f(x)) / delta


APPROXIMATION_STEPS = 8

DERIVATIVE_FUNCTION = calculated_df


#===================== MAIN =====================

def main():
	print("=" * 10 + "  Welcome to Newton Approximation  " + "=" * 10)
	print()
	x = float(input("Please, enter your guess: "))
	print("\nFollowing the winds of root...\n")
	df = DERIVATIVE_FUNCTION 	# Select derivative function.
	# Start approximation steps
	for i in range(APPROXIMATION_STEPS):
		offset = f(x) / df(x) 	# How much far from true root (approximately)
		x -= offset				# Correction
		print(f"Step {i + 1}: {x}")
	# Check answer
	print()
	print(f"Checking found root: f(x1) = {f(x)} ({f(x):2.8f})")

#================================================

if __name__ == "__main__":
	main()
