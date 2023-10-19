from resources.search import Search
from schemas.schemas import films_schema


class FilmsSearch(Search):
    def __init__(self):
        super().__init__(search_category="films")
        self.exp_schema = films_schema
