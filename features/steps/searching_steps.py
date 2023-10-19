from behave import *
from resources.people_search import PeopleSearch
from resources.planets_search import PlanetsSearch
from resources.starships_search import StarshipsSearch
from resources.vehicles_search import VehiclesSearch
from resources.films_search import FilmsSearch
from resources.species_search import SpeciesSearch
from resources.all_search import AllSearch


@given('The user wants to search for "{search_category}"')
def step_impl(context, search_category):
    if search_category == "people":
        context.search = PeopleSearch()
    elif search_category == "planets":
        context.search = PlanetsSearch()
    elif search_category == "starships":
        context.search = StarshipsSearch()
    elif search_category == "vehicles":
        context.search = VehiclesSearch()
    elif search_category == "films":
        context.search = FilmsSearch()
    elif search_category == "species":
        context.search = SpeciesSearch()
    elif search_category == "all":
        context.search = AllSearch()


@when('The user searches for phrase: "{search_phrase}"')
def step_impl(context, search_phrase):
    context.response_body, context.resp_status_code = context.search.search_for_phrase(search_phrase=search_phrase)


@then('Verify that the response code is "{exp_status_code}"')
def step_impl(context, exp_status_code):
    context.search.verify_that_status_code_is_correct(
        exp_status_code=int(exp_status_code), resp_status_code=context.resp_status_code
    )


@then("Verify that the response body matches schema")
def step_impl(context):
    exp_schema = context.search.exp_search_schema
    context.search.verify_that_response_body_matches_schema(exp_schema=exp_schema, response_body=context.response_body)


@then('Verify result endpoints for "{endpoint_name}"')
def step_impl(context, endpoint_name):
    if endpoint_name == "residents" or endpoint_name == "pilots":
        result_endpoint_search = PeopleSearch()
    elif endpoint_name == "planets":
        result_endpoint_search = PlanetsSearch()
    elif endpoint_name == "starships":
        result_endpoint_search = StarshipsSearch()
    elif endpoint_name == "vehicles":
        result_endpoint_search = VehiclesSearch()
    elif endpoint_name == "films":
        result_endpoint_search = FilmsSearch()
    elif endpoint_name == "species":
        result_endpoint_search = SpeciesSearch()

    result_endpoint_search.verify_result_endpoints(endpoint_name=endpoint_name, response_body=context.response_body)


@then('Verify that search field contains search phrase: "{search_phrase}"')
def step_impl(context, search_phrase):
    context.search.verify_search_field_contains_phrase(
        search_phrase=search_phrase, response_body=context.response_body
    )


@then("Verify that the detailed entry is correct")
def step_impl(context):
    context.search.verify_detailed_entry(response_body=context.response_body)
