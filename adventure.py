# Project Description @ https://www.dumas.io/teaching/2021/fall/mcs260/nbview/projects/project2.html

# MCS 260 Fall 2021 Project 2
# Umar Chaudhry
# I attest that the work done in this project is my own and I followed the rules of the project description and syllabus.
"Building a game engine for an adventure game! Date: 10/09/21"

import sys
import json

# gather json file and extract its data under the variable "map_info"
json_filename = sys.argv[1] 
json_openFile = open(json_filename,"r",encoding="UTF-8")
map_info = json.load(json_openFile)
json_openFile.close()

# a stack used to test whether the player has reached all the must visit areas
must_visit = []

# for loop adds as many must visit places from the json file to the stack
for key in map_info:
    if map_info[key]["mustvisit"] == True:
        must_visit.append("True")

# a list used to input the right key or position into the while loop
positions_list = ["start"]

# while loop continues until game over

while True:
     # print out the position of the player based off the matching key in the json file's dictionary
    print(map_info[positions_list[-1]]["description"])
    
    # the variable "direction" is used to choose the players next location and if that choice is allowed
    direction = input("> ")

    # if statement checks if the user's choice of "direction" is allowed and then adds that position to the postions_list
    if direction in map_info[positions_list[-1]]["exits"]:
        position = map_info[positions_list[-1]]["exits"][direction]
        positions_list.append(position)
        
    # if statement handles a invalid choice of next position
    elif direction not in map_info[positions_list[-1]]["exits"]:
        print("You can't go that way.")
        print()
        print(map_info[positions_list[-1]]["description"])
        direction = input("> ")
        
        position = map_info[positions_list[-1]]["exits"][direction]
        positions_list.append(position)

    # if statement handles a player attempting to enter a room not yet allowed for them
    if map_info[positions_list[-1]]["roomtype"] == "win" and len(must_visit) != 0:
        print("You aren't ready to go there yet.")
        print()
        print(map_info[positions_list[-2]]["description"])
        direction = input("> ")
        position = map_info[positions_list[-1]]["exits"][direction]
        positions_list.append(position)

    # if statement removing values from the stack to test if the player has reached all must visit positions
    if map_info[positions_list[-1]]["mustvisit"] == True and len(must_visit) != 0:
        must_visit.pop()

    # last two if statements handle game over scenarios
    if map_info[positions_list[-1]]["roomtype"] == "win":
        print(map_info[positions_list[-1]]["description"])
        exit()
    
    elif map_info[positions_list[-1]]["roomtype"] == "lose":
        print(map_info[positions_list[-1]]["description"])
        exit()