from elastic_app_search import Client

import constants

client = Client()


def init():
    global client
    client = Client(
        base_endpoint=constants.search_endpoint,
        api_key=constants.search_api_key,
        use_https=False
    )


def search(query):
    a = client.search(constants.search_engine_name, query, {"page": {"size": 5, "current": 1}})
    print(a)
    return a
