import unittest
from chandrayaan3_control import Chandrayaan3


class TestChandrayaan3(unittest.TestCase):

    # testing initialized variables (constructors)
    def test_initial_position_and_direction(self):
        obj = Chandrayaan3()
        self.assertEqual(obj.get_position(), (0, 0, 0))
        self.assertEqual(obj.get_direction(), 'N')

    # def test_move_forward(self):
    #     obj = Chandrayaan3()
    #     obj.move_forward()
    #     self.assertEqual(obj.get_position(), (0, 1, 0))
