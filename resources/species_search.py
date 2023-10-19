from resources.search import Search
from schemas.schemas import species_schema


class SpeciesSearch(Search):
    def __init__(self):
        super().__init__(search_category="species")
        self.exp_schema = species_schema
