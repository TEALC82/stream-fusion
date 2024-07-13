from stream_fusion.utils.models.media import Media


class Series(Media):
    def __init__(self, id, titles, season, episode, origin, languages):
        super().__init__(id, titles, languages, "series")
        self.season = season
        self.episode = episode
        self.origin = origin
        self.seasonfile = None
