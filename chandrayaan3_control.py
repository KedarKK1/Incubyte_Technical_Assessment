import sys


class Chandrayaan3:
    def __init__(self):
        self.position = (0, 0, 0)
        self.direction = 'N'

    # Implementing getters & setters
    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction

    def set_position(self, x: int, y: int, z: int):
        self.position = (x, y, z)

    def set_direction(self, dir: str):
        self.direction = dir
    # getters and setters completed

    def takeUserInput(self):

        # initializing variable
        ch = ''

        # while user-input is not 'c' or 'C', take user input
        while ch != "c" and ch != "C":
            print("Enter input (g - get position, d - get direction, x - set x position, y - set y position) or end input (c/C): ")
            ch = str(input())

            if(ch == "g"):
                print(self.get_position())
            elif(ch == "d"):
                print(self.get_direction())
            elif(ch == "x"):
                print("Enter Position corordinate X Y Z: ")
                x, y, z = map(int, sys.stdin.readline().split())
                print(self.set_position(x, y, z))
                print("Position is set to", self.get_position())
            elif(ch == "y"):
                print("Enter Directions(E/W/S/N): ")
                k = str(input())
                if(k == "E" or k == "W" or k == "S" or k == "N"):
                    print(self.set_direction(k))
                    print("Direction is set to", self.get_direction())
                else:
                    print("Invalid directions! ")
            elif(ch == "c" or ch == "C"):
                continue
            else:
                print("Error! Enter a valid input(f/b/l/r/u/d/c/C)")


# Creating obj for Chandrayaan3, for calling takeUserInput function, for taking user input
obj = Chandrayaan3()
obj.takeUserInput()
