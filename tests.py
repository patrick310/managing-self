import unittest
from datetime import date, timedelta

from Strategizer.Goal import Habit


class BasicTest(unittest.TestCase):

    def test_can_add_and_find_recent_actions(self):
        test_habit = Habit("test goal", "test starts")
        test_habit.log_action()
        test_habit.log_action(date=(date.today()-timedelta(days=89)))
        test_habit.log_action(date=(date.today() - timedelta(days=91)))

        self.assertEqual(test_habit.habit_strength_score(), 2)
