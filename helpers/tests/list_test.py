import helpers.list as cut
import unittest

LENGTH = 10
MAX_VALUE = 10

class TestListMethods(unittest.TestCase):

    def test_creating_a_random_list_with_a_certain_length_should_make_it_that_length(self):
       random_list = cut.create_random_list(LENGTH, MAX_VALUE)

       self.assertEqual(len(random_list), LENGTH)

    def test_creating_a_random_list_with_a_max_value_should_cap_the_values_to_it(self):
        random_list = cut.create_random_list(LENGTH, MAX_VALUE)

        found = False
        for element in random_list:
            if element > MAX_VALUE:
                found = True
                break

        self.assertFalse(found)

    def test_creating_a_random_list_should_cap_the_bottom_values_to_zero(self):
        random_list = cut.create_random_list(LENGTH, MAX_VALUE)

        found = False
        for element in random_list:
            if element < 0:
                found = True
                break

        self.assertFalse(found)

