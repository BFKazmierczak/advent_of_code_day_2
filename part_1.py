from functools import reduce
from typing import List


def add(a, b):
    return a + b


cubes = {"red": 12, "green": 13, "blue": 14}

data = open("data.txt", "r")

possible_games: List[int] = []

game_index = 0
line = data.readline()
while line:
    game_index = game_index + 1

    print(f"game_index={game_index}")

    first_split = line.split(":")

    rounds = first_split[1].split(";")
    print(f"rounds: {rounds}")

    is_possible = True

    for r in range(len(rounds)):
        game_round = rounds[r]
        print(f"\tgame_round: {game_round}")
        cubes_in_round = game_round.split(",")
        print(f"\tcubes_in_round: {cubes_in_round}")

        for cube in cubes_in_round:
            print(f"\t\tcube: {cube}")
            # color_number: Dict[str, int] = {}
            number_temp = ""
            color_temp = ""
            for i in range(len(cube)):
                char = cube[i]
                print(f"\t\t\tnow at char {char}")
                if char.isdigit():
                    number_temp = number_temp + char
                elif char != " " and char != "\n":
                    print("\t\t\t\tadding ", [char])
                    color_temp = color_temp + char

            print(
                f"\t\t\tnumber_temp={number_temp} color_temp={color_temp} {len(color_temp)}"
            )
            if int(number_temp) > cubes[color_temp]:
                is_possible = False

                print(
                    f"Game {game_index} is NOT possible, because {color_temp} amount is {cubes[color_temp]} which is smaller than {number_temp}"
                )
                break

    if is_possible:
        possible_games.append(game_index)

    line = data.readline()

print(f"Possible games: {possible_games}")

final_sum = reduce(add, possible_games)

print(f"Final sum={final_sum}")

data.close
