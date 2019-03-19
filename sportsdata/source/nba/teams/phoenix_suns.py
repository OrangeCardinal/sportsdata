from sportsdata.source.nba.team import NBA_Team


class PhoenixSuns(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Phoenix Suns"
        self.name       = "Suns"
        self.team_id    = None