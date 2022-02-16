#!/usr/bin/env python3

#======================================#
#=       MARKOV CHAIN EQUILIBRIUM     =#
#======================================#
# Represented by directed cyclic graph with 3 nodes.

from random import Random


nodes = ("star", "tower", "light")

screen_text_walk = """
Phase 1. Random walk distribution:
step {} / {}
star  [ {:.6f} ]
tower [ {:.6f} ]
light [ {:.6f} ]
"""

screen_text_transition = """
Phase 2. Vector transition:
[ {:.6f}, {:.6f}, {:.6f} ]
"""

# Adjacency Matrix
A = [
    [ 0.2 , 0.6 , 0.2 ] ,
    [ 0.3 , 0.0 , 0.7 ] ,
    [ 0.5 , 0.0 , 0.5 ] ,
]

rnd = Random()

RANDOM_WALK_STEPS = 1_000_000

VECTOR_TRANSITION_STEPS = 10_000

def walk(node: str) -> str:
    i = nodes.index(node) # Row index
    r = rnd.random()
    if r < A[i][0]:
        result_index = 0
    elif r < A[i][0] + A[i][1]:
        result_index = 1
    else:
        result_index = 2
    return nodes[result_index]

def transition(vec: list) -> list:
    # Row vector multiply to the matrix
    return [
        vec[0] * A[0][0] + vec[1] * A[1][0] + vec[2] * A[2][0],
        vec[0] * A[0][1] + vec[1] * A[1][1] + vec[2] * A[2][1],
        vec[0] * A[0][2] + vec[1] * A[1][2] + vec[2] * A[2][2],
    ]

#===================== MAIN =====================

def main():
    print("=" * 10 + " Walking " + "=" * 10)

    # 1. Random walk
    stats = { "star":0, "tower":0, "light":0 }
    node = "tower" # Starting node
    for i in range(1, RANDOM_WALK_STEPS + 1):
        node = walk(node)
        stats[node] = stats[node] + 1
        # Distribution
        dst = {
            "star" : stats["star"] / i,
            "tower": stats["tower"] / i,
            "light": stats["light"] / i,
        }
        print(screen_text_walk.format(
            i, RANDOM_WALK_STEPS, dst["star"], dst["tower"], dst["light"]
        ))
        print("\033[8A") # Return cursor
    print(screen_text_walk.format(
        i, RANDOM_WALK_STEPS, dst["star"], dst["tower"], dst["light"]
    ))

    # 2. Vector transition
    vec = [0, 1, 0] # Starting row-vector
    for i in range(VECTOR_TRANSITION_STEPS):
        vec = transition(vec)
        print(screen_text_transition.format(*vec))
        print("\033[5A") # Return cursor
    print(screen_text_transition.format(*vec))

#================================================

if __name__ == "__main__":
    main()
