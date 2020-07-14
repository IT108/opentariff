from elastic_app_search import Client

import constants

client = Client()
pagesize = 10


def init():
    global client
    client = Client(
        base_endpoint=constants.search_endpoint,
        api_key=constants.search_api_key,
        use_https=False
    )


def search(query):
    a = client.search(constants.search_engine_name, query, {"page": {"size": pagesize, "current": 1}})
    return a
