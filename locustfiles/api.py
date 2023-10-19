import random, string
from locust import task, between, HttpUser
from resources.people_search import PeopleSearch
from resources.planets_search import PlanetsSearch
from resources.starships_search import StarshipsSearch
from resources.vehicles_search import VehiclesSearch


class LocustUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def search_for_people_and_verify_results(self):
        self.perform_search_verify_response(search_category="people")

    @task
    def search_for_planets_and_verify_results(self):
        self.perform_search_verify_response(search_category="planets")

    @task
    def search_for_starships_and_verify_results(self):
        self.perform_search_verify_response(search_category="starships")

    @task
    def search_for_vehicles_and_verify_results(self):
        self.perform_search_verify_response(search_category="vehicles")

    def perform_search_verify_response(self, search_category: str):
        """
        Performs a search and verifies results

        Args:
          self: object instance
          search_category: it can be either 'people', 'planets', 'starships', 'vehicles' or 'all'
        """
        if search_category == "people":
            search = PeopleSearch()
        elif search_category == "planets":
            search = PlanetsSearch()
        elif search_category == "starships":
            search = StarshipsSearch()
        elif search_category == "vehicles":
            search = VehiclesSearch()

        response_body, resp_status_code = self.search_for_phrase_with_locust(
            search_phrase=self.generate_random_string(), search=search
        )
        search.verify_that_status_code_is_correct(exp_status_code=200, resp_status_code=resp_status_code)
        search.verify_that_response_body_matches_schema(
            exp_schema=search.exp_search_schema, response_body=response_body
        )

    def generate_random_string(self):
        """
        Generates a random 2 letter string

        Returns:
          The generated string
        """
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for _ in range(2))

    def search_for_phrase_with_locust(self, search_phrase, search):
        """
        Using HttpUser, query the search endpoint

        Args:
          self: object instance
          search_phrase: the randomly generated string to search for
          search: the Search object (to determine search category)

        Returns:
          The response body and the response code
        """
        url = f"https://swapi.dev/api/{search.category}/?search={search_phrase}"
        resp = self.client.get(url)
        resp_body = resp.json()
        resp_status_code = resp.status_code
        return resp_body, resp_status_code
