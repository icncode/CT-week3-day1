from whiteboard import solution
from unittest import TestCase


class TestWhiteboard(TestCase):

    def test_1(self):
        expected_output = "odd"
        self.assertEqual(solution([0, 1, 4]), expected_output)

    def test_2(self):
        expected_output = "even"
        self.assertEqual(solution([0, -1, -5]), expected_output)

    def test_3(self):
        expected_output = "even"
        self.assertEqual(solution([0, 1, 1]), expected_output)

    def test_4(self):
        expected_output = "even"
        self.assertEqual(solution([0]), expected_output)


