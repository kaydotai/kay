# All functions to call external APIs (Embed store, OpenAI)

import os
from kay.helpers.exceptions import APIKeyError, ServerError


def get_kay_apikey():
    kay_api_key = os.getenv("KAY_API_KEY")
    if kay_api_key is not None:
        return kay_api_key
    else:
        raise APIKeyError("Couldn't find KAY_API_KEY in env")


def call_kay(prompt, dataset_config=None, retrieval_config=None):
    import requests

    kay_api_key = get_kay_apikey()
    url = "https://api.kay.ai/retrieve"
    headers = {"API-Key": kay_api_key}

    payload = {
        "query": prompt,
        "dataset_config": dataset_config,
        "retrieval_config": retrieval_config,
    }

    response = requests.post(url, headers=headers, json=payload)

    # Parsing the response and handling errors
    if response.status_code == 200:
        response_json = response.json()
        if response_json["success"] in {True, "true"}:
            response_json["success"] = True
            return response_json
        else:
            raise ServerError(
                f'Server error : {response_json["error"]}. If this persists, please create an issue here - '
                f"https://github.com/kaydotai/kay/issues "
            )
    elif response.status_code == 400:
        raise ServerError(f"Server error 400 for -- {url}")
    elif response.status_code == 401:
        raise APIKeyError(f"Invalid API Key, please contact us at hello@kay.ai")
    else:
        raise ServerError(f"Server error : {response.status_code}")
