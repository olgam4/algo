import helpers.math as cut
import unittest


class TestMathMethods(unittest.TestCase):

    def test_requiring_the_average_should_give_the_right_average(self):
        some_array_with_average_ten = [10, 12, 8, 15, 5]

        average = cut.average(some_array_with_average_ten)

        self.assertEqual(average, 10)

    def test_calculating_the_average_of_an_empty_array_should_equal_zero(self):
        some_empty_array = []

        average = cut.average(some_empty_array)

        self.assertEqual(average, 0)



