from functools import reduce
from typing import List


def add(a, b):
    return a + b


powers: List[int] = []

data = open("data.txt", "r")

game_index = 0
line = data.readline()
while line:
    game_index = game_index + 1

    # print(f"game_index={game_index}")

    first_split = line.split(":")

    rounds = first_split[1].split(";")
    # print(f"rounds: {rounds}")

    cubes_min = {"red": 0, "blue": 0, "green": 0}

    for r in range(len(rounds)):
        game_round = rounds[r]
        # print(f"\tgame_round: {game_round}")
        cubes_in_round = game_round.split(",")
        # print(f"\tcubes_in_round: {cubes_in_round}")

        for cube in cubes_in_round:
            # print(f"\t\tcube: {cube}")

            number_temp = ""
            color_temp = ""
            for i in range(len(cube)):
                char = cube[i]
                # print(f"\t\t\tnow at char {char}")
                if char.isdigit():
                    number_temp = number_temp + char
                elif char != " " and char != "\n":
                    # print("\t\t\t\tadding ", [char])
                    color_temp = color_temp + char

            # print(
            #     f"\t\t\tnumber_temp={number_temp} color_temp={color_temp} {len(color_temp)}"
            # )

            if int(number_temp) > cubes_min[color_temp]:
                cubes_min[color_temp] = int(number_temp)

    print(f"minimum cubes for {line} =")
    print(f"{cubes_min}")

    power = 1
    for key, value in cubes_min.items():
        power = power * value

    powers.append(power)

    line = data.readline()


final_sum = reduce(add, powers)

print(f"Final sum={final_sum}")

data.close
