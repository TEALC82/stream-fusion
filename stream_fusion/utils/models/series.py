from stream_fusion.utils.models.media import Media


class Series(Media):
    def __init__(self, id, titles, season, episode, origin_country, languages):
        super().__init__(id, titles, languages, "series")
        self.season = season
        self.episode = episode
        self.origin_country = origin_country
        self.seasonfile = None
