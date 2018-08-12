import unittest
from datetime import date, timedelta

from Strategizer.Goal import Habit


class BasicTest(unittest.TestCase):

    def test_can_add_action(self):
        test_habit = Habit("test goal", "test starts")
        test_habit.log_action()

        self.assertTrue(test_habit.actions[0].is_recent)

    def test_can_add_and_find_recent_actions(self):
        test_habit = Habit("test goal", "test starts")
        test_habit.log_action()
        test_habit.log_action(date=(date.today()-timedelta(days=89)))
        test_habit.log_action(date=(date.today() - timedelta(days=91)))

        self.assertAlmostEqual(25.7142857, test_habit.habit_strength_score())
