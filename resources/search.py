import requests
from pytest_schema import schema


class Search:
    def __init__(self, search_category="all"):
        self.category = search_category
        self.all_categories = ["people", "planets", "starships", "vehicles"]
        self.s = requests.Session()

    def search_for_phrase(self, search_phrase: str):
        """
        Search for a phrase

        Args:
          self: object instance
          search_phrase: search phrase to get matching results for

        Returns:
          The response body and status code of the get request
        """
        if self.category == "all":
            resp_body = self.build_response_body_for_all_search(search_phrase)
            resp_status_code = 200
        else:
            url = f"https://swapi.dev/api/{self.category}/?search={search_phrase}"
            resp = self.s.get(url)
            resp_body = resp.json()
            resp_status_code = resp.status_code
        return resp_body, resp_status_code

    def build_response_body_for_all_search(self, search_phrase):
        """
        Searches for all 4 categories and appends the results together

        Args:
          self: object instance
          search_phrase: search phrase to get matching results for

        Returns:
          The built response body
        """
        resp_body = {"count": 0, "next": None, "previous": None, "results": []}
        for category in self.all_categories:
            url = f"https://swapi.dev/api/{category}/?search={search_phrase}"
            resp = self.s.get(url)
            resp_json = resp.json()
            resp_results = resp_json["results"]
            resp_body["results"].extend(resp_results)
            resp_body["count"] += resp_json["count"]
        return resp_body

    def verify_that_status_code_is_correct(self, exp_status_code: int, resp_status_code: int):
        """
        Verifies that the status code is correct

        Args:
          self: object instance
          exp_status_code: expected status code
          resp_status_code: actual response status code
        """
        assert resp_status_code == exp_status_code, f"Status code is not {exp_status_code}, got: {resp_status_code}"

    def verify_that_response_body_matches_schema(self, exp_schema, response_body: object):
        """
        Verifies that the response body matches the expected schema

        Args:
          self: object instance
          exp_schema: expected schema
          response_body: response body to validate schema for
        """
        assert schema(exp_schema) == response_body, "Schema does not match"

    def get_result_endpoint(self, url: str):
        """
        Gets a given url and returns the response object

        Args:
          self: object instance
          url: url to query

        Returns:
          The response of the get request
        """
        if url.startswith("http://"):
            url = url.replace("http://", "https://")
        resp = self.s.get(url)
        return resp

    def verify_result_endpoints(self, endpoint_name: str, response_body: object):
        """
        Verifies that the endpoints in the response are correct

        Args:
          self: object instance
          endpoint_name: key of result to test (e.g. people, starships, films, etc.)
          response_body: response body that contains the result endpoints
        """
        for result in response_body["results"]:
            if endpoint_name in result:
                if len(result[endpoint_name]) == 0:
                    continue

                for url in result[endpoint_name]:
                    resp = self.get_result_endpoint(url=url)
                    resp_json = resp.json()
                    self.verify_that_status_code_is_correct(200, resp.status_code)
                    self.verify_that_response_body_matches_schema(exp_schema=self.exp_schema, response_body=resp_json)

    def verify_detailed_entry(self, response_body: object):
        """
        Verifies that the detailed entry contains correct information

        Args:
          self: object instance
          response_body: response body that contains the detailed entry endpoint
        """
        for result in response_body["results"]:
            url = result["url"]
            resp = self.get_result_endpoint(url=url)
            resp_json = resp.json()
            self.verify_that_status_code_is_correct(200, resp.status_code)
            self.verify_that_response_body_matches_schema(exp_schema=self.exp_schema, response_body=resp_json)
