from datetime import date, timedelta
import pandas as pd

from Strategizer.Action import Action


class Habit:
    """
    "Habits are learned sequences of acts that have become automatic responses to specific cues"
     (Verplanken & Aarts, 1999)

     -Learned through context-dependent repetition
     -Cue-dependent
     -Automatic

     Therefore, to establish and measure the strength of lasting habits:

     -We store the context or trigger for each habit
     -We measure the strength of the cue
     -We measure the magnitude of autonomy

     Habit classification:
     -Frequency (expressed as number of times daily)

    """

    def __init__(self, name, cue, frequency=7, start_date=None):
        self.name = name
        self.cue = cue
        self.frequency = frequency

        if start_date is None:
            start_date = date.today()
        self.start_date = start_date
        self.initialisation_date = date.today()

        self.actions = []

    def log_action(self, date=date.today(), autonomy_rating=None, cue_strength_rating=None):
        self.actions.append(Action(self.name, date, autonomy_rating, cue_strength_rating))

    def habit_strength_score(self, period=90):
        actions_as_dict = [action.as_dict() for action in self.actions]
        df = pd.DataFrame.from_dict(actions_as_dict)

        start_date = date.today() - timedelta(days=90)
        end_date = date.today()
        recent_actions = df['date'].between(start_date, end_date)

        recent_actions = df.loc[recent_actions]

        # average_autonomy = recent_actions.mean(axis='autonomy_rating')
        score = recent_actions.shape[0] / self.frequency*period

        return score
