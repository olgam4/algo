import unittest
import helpers.func as cut
from unittest.mock import MagicMock, Mock, patch
import settings

TIME_INCREMENT = 100
TRIES = 100

mock_time = MagicMock()
mock_time.side_effect = lambda: mock_time.call_count * TIME_INCREMENT

settings.verbose = False

mock_print = MagicMock()
mock_print.side_effect = None

class TestFuncMethods(unittest.TestCase):


    def test_timing_a_func_should_execute_the_func(self):
        some_func = Mock()

        cut.time_this(some_func)

        some_func.assert_called_once_with()

    def test_timing_a_func_should_extract_its_return_value(self):
        some_func = Mock(return_value=100)

        return_value, _ = cut.time_this(some_func)

        self.assertEqual(return_value, 100)

    @patch('time.time', mock_time)
    def test_timing_a_func_should_calculate_the_time_between_the_start_and_end(self):
        some_func = Mock()

        _, total_time = cut.time_this(some_func)

        self.assertEqual(total_time, TIME_INCREMENT * 1)


    @patch('builtins.print', mock_print)
    def test_testing_a_func_should_execute_as_many_times_as_required(self):
        some_func = Mock()
        some_func.return_value = 0
        setup_expected_value = Mock()
        setup_expected_value.return_value = some_func.return_value
        setup_argument = Mock()

        _ = cut.test_func(some_func, TRIES, setup_expected_value, setup_argument)

        self.assertEqual(some_func.call_count, TRIES)

    @patch('builtins.print', mock_print)
    def test_testing_a_which_does_not_work_as_intended_should_only_run_once(self):
        some_func = Mock()
        some_func.return_value = 0
        setup_expected_value = Mock()
        setup_expected_value.return_value = 10
        setup_argument = Mock()

        _ = cut.test_func(some_func, TRIES, setup_expected_value, setup_argument)

        some_func.assert_called_once()

    @patch('builtins.print', mock_print)
    def test_testing_a_func_should_print_if_verbose_is_turned_on(self):
        self.assertTrue(False)

