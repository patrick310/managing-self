import datetime


class Action:
    """
    Represents a possible move towards completion of a goal
    """

    def __init__(self, goal, date, autonomy_rating=None, cue_strength_rating=None):
        self.goal = goal
        self.date = date

        self.autonomy_rating = autonomy_rating
        self.cue_strength_rating = cue_strength_rating

    def as_dict(self):
        return {'date': self.date,
                'autonomy_rating': self.autonomy_rating,
                'cue_strength_rating': self.cue_strength_rating}

    @property
    def is_recent(self):
        return True if ((datetime.date.today() - self.date).days <= 90) else False
