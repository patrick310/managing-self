class Action:
    """
    Represents a possible move towards completion of a goal
    """

    def __init__(self, goal, date, autonomy_rating=None, cue_strength_rating=None):
        self.goal = goal
        self.date = date

        self.autonomy_rating = autonomy_rating
        self.cue_strength_rating = cue_strength_rating
