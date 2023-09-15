import unittest
from chandrayaan3_control import Chandrayaan3
class TestChandrayaan3(unittest.TestCase):

    # testing initialized variables (constructors)
    def test_initial_position_and_direction(self):
        obj = Chandrayaan3()
        self.assertEqual(obj.get_position(), (0, 0, 0))
        self.assertEqual(obj.get_direction(), 'N')

    # testing move_forward, move_forward
    def test_move_forward(self):
        obj = Chandrayaan3()
        obj.move_forward()
        self.assertEqual(obj.get_position(), (0, 1, 0))

    def test_move_backward(self):
        obj = Chandrayaan3()
        obj.move_backward()
        self.assertEqual(obj.get_position(), (0, -1, 0))

    # testing turn_left, turn_right, turn_up, turn_down
    def test_turn_left(self):
        obj = Chandrayaan3()
        obj.turn_left()
        self.assertEqual(obj.get_direction(), 'W')

    def test_turn_right(self):
        obj = Chandrayaan3()
        obj.turn_right()
        self.assertEqual(obj.get_direction(), 'E')

    def test_turn_up(self):
        obj = Chandrayaan3()
        obj.turn_up()
        self.assertEqual(obj.get_direction(), 'U')

    def test_turn_down(self):
        obj = Chandrayaan3()
        obj.turn_down()
        self.assertEqual(obj.get_direction(), 'D')