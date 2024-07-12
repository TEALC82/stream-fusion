import requests

from stream_fusion.utils.metdata.metadata_provider_base import MetadataProvider
from stream_fusion.utils.models.movie import Movie
from stream_fusion.utils.models.series import Series
from stream_fusion.settings import settings

class TMDB(MetadataProvider):
    def get_metadata(self, id, type):
        self.logger.info("Getting metadata for " + type + " with id " + id)

        full_id = id.split(":")

        result = None

        for lang in self.config['languages']:
            url = f"https://api.themoviedb.org/3/find/{full_id[0]}?api_key={settings.tmdb_api_key}&external_source=imdb_id&language={lang}"
            response = requests.get(url)
            data = response.json()

            if lang == self.config['languages'][0]:
                if type == "movie":
                    result = Movie(
                        id=id,
                        titles=[self.replace_weird_characters(data["movie_results"][0]["title"])],
                        year=data["movie_results"][0]["release_date"][:4],
                        languages=self.config['languages']
                    )
                else:
                    if data["tv_results"][0]["origin_country"] = "JP":
                        atitles = [self.replace_weird_characters(data["tv_results"][0]["name"])]
                        parts = atitles.split(':', 1)
                        update_titles = parts[0].strip()
                    else:
                        update_titles = [self.replace_weird_characters(data["tv_results"][0]["name"])]

                    result = Series(
                        id=id,
                        titles=update_titles,
                        season="S{:02d}".format(int(full_id[1])),
                        episode="E{:02d}".format(int(full_id[2])),
                        languages=self.config['languages']
                    )
            else:
                if type == "movie":
                    result.titles.append(self.replace_weird_characters(data["movie_results"][0]["title"]))
                else:
                    if data["tv_results"][0]["origin_country"] = "JP":
                        atitles = [self.replace_weird_characters(data["tv_results"][0]["name"])]
                        parts = atitles.split(':', 1)
                        update_titles = parts[0].strip()
                        result.titles.append(self.replace_weird_characters(update_titles))
                    else:
                        result.titles.append(self.replace_weird_characters(data["tv_results"][0]["name"]))

        self.logger.info("Got metadata for " + type + " with id " + id)
        return result
