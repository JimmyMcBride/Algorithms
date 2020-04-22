#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    rps = [["rock", "paper", "scissors"]] * n
    game_choice = []
    grand_daddy_array = [game_choice]
    for choice in rps:
        grand_daddy_array = [x + [y] for x in grand_daddy_array for y in choice]
    return grand_daddy_array


print(rock_paper_scissors(2))
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print("Usage: rps.py [num_plays]")
