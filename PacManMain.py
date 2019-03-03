import re
import PacManSim

# Entry point of program. This file is where user input functionality is provided

command = ''
pacman = PacManSim.PacManSimulator()
is_placed = False
regex = re.compile(r'^PLACE\s[0-4][,][0-4][,](NORTH|SOUTH|EAST|WEST)')  # uses regex to enforce valid PLACE input

while True:
    command = input("Enter an instruction for PacMan to execute: ")
    if command == 'QUIT':
        break
    if not is_placed:
        if regex.match(command):
            is_placed = True
            coords = re.findall('\d+', command)
            start_direction = command.rsplit(',', 1)[1]
            pacman.place(int(coords[0]), int(coords[1]), start_direction)
        else:
            print("Invalid input. Use the place command to place PacMan"
                  " with the format 'PLACE X,X,DIRECTION' where X is between 0 and 4 inclusive and DIRECTION is one of "
                  "NORTH/SOUTH/EAST/WEST")
            continue
    else:
        if regex.match(command):
            coords = re.findall('\d+', command)
            start_direction = command.rsplit(',', 1)[1]
            pacman.place(int(coords[0]), int(coords[1]), start_direction)
        elif command == 'MOVE':
            pacman.move()
        elif command == 'LEFT':
            pacman.rotate('LEFT')
        elif command == 'RIGHT':
            pacman.rotate('RIGHT')
        elif command == 'REPORT':
            print(pacman.report())
        else:
            print("Invalid command. Valid commands are: PLACE X,X,DIRECTION (X between 0-4 inclusive, DIRECTION is "
                  " one of NORTH/SOUTH/EAST/WEST), MOVE, LEFT, RIGHT, REPORT")
