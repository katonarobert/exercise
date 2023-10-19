from resources.search import Search
from schemas.schemas import people_search_schema, people_schema


class PeopleSearch(Search):
    def __init__(self):
        super().__init__(search_category="people")
        self.exp_search_schema = people_search_schema
        self.exp_schema = people_schema

    def verify_search_field_contains_phrase(self, search_phrase: str, response_body: object):
        """
        Verifies that the people search field contains the search phrase

        Args:
          self: object instance
          search_phrase: phrase used in /api/people/?search={phrase}
          response_body: response body to verify phrases for
        """
        for result in response_body["results"]:
            search_field = result["name"]
            assert (
                search_phrase.lower() in search_field.lower()
            ), f'Search field "name" {search_field} does not contain {search_phrase}'
