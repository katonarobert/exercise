from resources.search import Search
from schemas.schemas import vehicles_search_schema, vehicles_schema


class VehiclesSearch(Search):
    def __init__(self):
        super().__init__(search_category="vehicles")
        self.exp_search_schema = vehicles_search_schema
        self.exp_schema = vehicles_schema

    def verify_search_field_contains_phrase(self, search_phrase: str, response_body: object):
        """
        Verifies that the vehicles search field contains the search phrase

        Args:
          self: object instance
          search_phrase: phrase used in /api/vehicles/?search={phrase}
          response_body: response body to verify phrases for
        """
        for result in response_body["results"]:
            assert (
                search_phrase.lower() in result["name"].lower() or search_phrase.lower() in result["model"].lower()
            ), f'Search fields "name", "model" does not contain {search_phrase}'
