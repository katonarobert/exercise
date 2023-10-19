from resources.search import Search
from schemas.schemas import all_search_schema


class AllSearch(Search):
    def __init__(self):
        super().__init__()
        self.exp_search_schema = all_search_schema

    def verify_search_field_contains_phrase(self, search_phrase: str, response_body: object):
        """
        Verifies that the search field contains the search phrase

        Args:
          self: object instance
          search_phrase: phrase used in /api/{category}/?search={phrase}
          response_body: response body to verify phrases for
        """
        for result in response_body["results"]:
            if "model" in result:
                assert (
                    search_phrase.lower() in result["name"].lower() or search_phrase.lower() in result["model"].lower()
                ), f'Search fields "name", "model" does not contain {search_phrase}'
            else:
                assert (
                    search_phrase.lower() in result["name"].lower()
                ), f'Search field "name" {result["name"]} does not contain {search_phrase}'
