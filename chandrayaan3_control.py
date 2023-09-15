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

