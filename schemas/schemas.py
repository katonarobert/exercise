from pytest_schema import Regex, Or, schema

INTEGER_PATTERN = "[0-9]+"
FLOAT_PATTERN = "[0-9]+(.[0-9]+)?"
DATE_PATTERN = "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(.[0-9]{6})?Z"


people_schema = {
    "name": str,
    "height": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "mass": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "hair_color": str,
    "skin_color": str,
    "eye_color": str,
    "birth_year": str,
    "gender": Or("male", "female", "n/a", "hermaphrodite"),
    "homeworld": Or(Regex(f"https://swapi.dev/api/planets/{INTEGER_PATTERN}/"), None),
    "films": [Regex(f"https://swapi.dev/api/films/{INTEGER_PATTERN}/")],
    "species": [Regex(f"https://swapi.dev/api/species/{INTEGER_PATTERN}/")],
    "vehicles": [Regex(f"https://swapi.dev/api/vehicles/{INTEGER_PATTERN}/")],
    "starships": [Regex(f"https://swapi.dev/api/starships/{INTEGER_PATTERN}/")],
    "created": Regex(DATE_PATTERN),
    "edited": Regex(DATE_PATTERN),
    "url": Regex(f"https://swapi.dev/api/people/{INTEGER_PATTERN}/"),
}

people_search_schema = {
    "count": int,
    "next": Or(None, str),
    "previous": Or(None, str),
    "results": [people_schema],
}

vehicles_schema = {
    "name": str,
    "model": str,
    "manufacturer": str,
    "cost_in_credits": str,
    "length": Or(Regex(FLOAT_PATTERN), "n/a", "unknown"),
    "max_atmosphering_speed": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "crew": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "passengers": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "cargo_capacity": Or(Regex(INTEGER_PATTERN), "n/a", "unknown", "none"),
    "consumables": str,
    "vehicle_class": str,
    "pilots": [Regex(f"https://swapi.dev/api/people/{INTEGER_PATTERN}/")],
    "films": [Regex(f"https://swapi.dev/api/films/{INTEGER_PATTERN}/")],
    "created": Regex(DATE_PATTERN),
    "edited": Regex(DATE_PATTERN),
    "url": Regex(f"https://swapi.dev/api/vehicles/{INTEGER_PATTERN}/"),
}

vehicles_search_schema = {
    "count": int,
    "next": Or(None, str),
    "previous": Or(None, str),
    "results": [vehicles_schema],
}

starships_schema = {
    "name": str,
    "model": str,
    "manufacturer": str,
    "cost_in_credits": str,
    "length": Or(Regex(FLOAT_PATTERN), "n/a", "unknown"),
    "max_atmosphering_speed": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "crew": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "passengers": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "cargo_capacity": Or(Regex(INTEGER_PATTERN), "n/a", "unknown", "none"),
    "consumables": str,
    "hyperdrive_rating": Or(Regex(FLOAT_PATTERN), "n/a", "unknown"),
    "MGLT": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "starship_class": str,
    "pilots": [Regex(f"https://swapi.dev/api/people/{INTEGER_PATTERN}/")],
    "films": [Regex(f"https://swapi.dev/api/films/{INTEGER_PATTERN}/")],
    "created": Regex(DATE_PATTERN),
    "edited": Regex(DATE_PATTERN),
    "url": Regex(f"https://swapi.dev/api/starships/{INTEGER_PATTERN}/"),
}

starships_search_schema = {
    "count": int,
    "next": Or(None, str),
    "previous": Or(None, str),
    "results": [starships_schema],
}

films_schema = {
    "title": str,
    "episode_id": int,
    "opening_crawl": str,
    "director": Or("George Lucas", "Irvin Kershner", "Richard Marquand"),
    "producer": str,
    "release_date": Regex("[0-9]{4}-[0-9]{2}-[0-9]{2}"),
    "characters": [Regex(f"https://swapi.dev/api/people/{INTEGER_PATTERN}/")],
    "planets": [Regex(f"https://swapi.dev/api/planets/{INTEGER_PATTERN}/")],
    "starships": [Regex(f"https://swapi.dev/api/starships/{INTEGER_PATTERN}/")],
    "vehicles": [Regex(f"https://swapi.dev/api/vehicles/{INTEGER_PATTERN}/")],
    "species": [Regex(f"https://swapi.dev/api/species/{INTEGER_PATTERN}/")],
    "created": Regex(DATE_PATTERN),
    "edited": Regex(DATE_PATTERN),
    "url": Regex(f"https://swapi.dev/api/films/{INTEGER_PATTERN}/"),
}

species_schema = {
    "name": str,
    "classification": str,
    "designation": str,
    "average_height": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "skin_colors": str,
    "hair_colors": str,
    "eye_colors": str,
    "average_lifespan": Or(Regex(INTEGER_PATTERN), "n/a", "unknown", "indefinite"),
    "homeworld": Or(Regex(f"https://swapi.dev/api/planets/{INTEGER_PATTERN}/"), None),
    "language": str,
    "people": [Regex(f"https://swapi.dev/api/people/{INTEGER_PATTERN}/")],
    "films": [Regex(f"https://swapi.dev/api/films/{INTEGER_PATTERN}/")],
    "created": Regex(DATE_PATTERN),
    "edited": Regex(DATE_PATTERN),
    "url": Regex(f"https://swapi.dev/api/species/{INTEGER_PATTERN}/"),
}

planets_schema = {
    "name": str,
    "rotation_period": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "orbital_period": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "diameter": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "climate": str,
    "gravity": str,
    "terrain": str,
    "surface_water": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "population": Or(Regex(INTEGER_PATTERN), "n/a", "unknown"),
    "residents": [Regex(f"https://swapi.dev/api/people/{INTEGER_PATTERN}/")],
    "films": [Regex(f"https://swapi.dev/api/films/{INTEGER_PATTERN}/")],
    "created": Regex(DATE_PATTERN),
    "edited": Regex(DATE_PATTERN),
    "url": Regex(f"https://swapi.dev/api/planets/{INTEGER_PATTERN}/"),
}

planets_search_schema = {
    "count": int,
    "next": Or(None, str),
    "previous": Or(None, str),
    "results": [planets_schema],
}

all_search_schema = {
    "count": int,
    "next": Or(None, str),
    "previous": Or(None, str),
    "results": [people_schema, planets_schema, starships_schema, vehicles_schema],
}
