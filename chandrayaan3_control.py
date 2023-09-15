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

    def move_forward(self):
        # Implement forward movement
        x, y, z = self.position
        if self.get_direction() == 'N':
            self.set_position(x, y + 1, z)
        elif self.get_direction() == 'S':
            self.set_position(x, y - 1, z)
        elif self.get_direction() == 'E':
            self.set_position(x + 1, y, z)
        elif self.get_direction() == 'W':
            self.set_position(x - 1, y, z)
        elif self.get_direction() == 'U':
            self.set_position(x, y, z + 1)
        elif self.get_direction() == 'D':
            self.set_position(x, y, z - 1)

    def move_backward(self):
        # Implement backward movement
        x, y, z = self.position
        if self.get_direction() == 'N':
            self.set_position(x, y - 1, z)
        elif self.get_direction() == 'S':
            self.set_position(x, y + 1, z)
        elif self.get_direction() == 'E':
            self.set_position(x - 1, y, z)
        elif self.get_direction() == 'W':
            self.set_position(x + 1, y, z)
        elif self.get_direction() == 'U':
            self.set_position(x, y, z - 1)
        elif self.get_direction() == 'D':
            self.set_position(x, y, z + 1)

    def turn_left(self):
        # Implement left turn
        if self.get_direction() == 'N':
            self.set_direction('W')
        elif self.get_direction() == 'S':
            self.set_direction('E')
        elif self.get_direction() == 'E':
            self.set_direction('N')
        elif self.get_direction() == 'W':
            self.set_direction('S')
        elif self.get_direction() == 'U':
            self.set_direction('N')
        elif self.get_direction() == 'D':
            self.set_direction('S')

    def turn_right(self):
        # Implement right turn
        if self.get_direction() == 'N':
            self.set_direction('E')
        elif self.get_direction() == 'S':
            self.set_direction('W')
        elif self.get_direction() == 'E':
            self.set_direction('S')
        elif self.get_direction() == 'W':
            self.set_direction('N')
        elif self.get_direction() == 'U':
            self.set_direction('S')
        elif self.get_direction() == 'D':
            self.set_direction('N')

    def turn_up(self):
        # Implement up turn
        self.set_direction('U')

    def turn_down(self):
        # Implement down turn
        self.set_direction('D')

    def takeUserInput(self):

        # initializing variables
        ch, inputList = '', list()

        # while user-input is not 'cc or 'C', take user input
        while ch != "c" and ch != "C":
            print("Enter input (f, b, l, r, u, d) or end input (c/C): ")
            ch = str(input())

            # checking if user input is is valid or not
            # if invalid, then we do not append it to the inputList
            # if input is 'c' or 'C', then we do not append it to the inputList
            if(ch == "f" or ch == "b" or ch == "l" or ch == "r" or ch == "u" or ch == "d"):
                inputList.append(ch)
            elif(ch == "c" or ch == "C"):
                continue
            else:
                print("Error! Enter a valid input(f/b/l/r/u/d/c/C)")

        # iterating inputList elements via element variable, one by one
        for element in inputList:
            if(element == "f"):
                self.move_forward()
            elif(element == "b"):
                self.move_backward()
            elif(element == "l"):
                self.turn_left()
            elif(element == "r"):
                self.turn_right()
            elif(element == "u"):
                self.turn_up()
            elif(element == "d"):
                self.turn_down()
            else:
                print("Unknown element in inputList: %s" % element)

        # printing final output
        print("Final Position: ", self.get_position())
        print("Final Direction: ", self.get_direction())


# Creating obj for Chandrayaan3, for calling takeUserInput function, for taking user input
# obj = Chandrayaan3()
# obj.takeUserInput()
