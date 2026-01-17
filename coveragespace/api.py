"""API client functions."""

import time

import log
import requests

from . import API
from .cache import Cache

cache = Cache()


def put(slug: str, data):
    url = f"{API}/{slug}"
    log.info("PUT %s: %s", url, data)

    response = cache.get((url, data))
    if response is None:
        for delay in [1, 3, 5]:
            response = requests.put(url, data=data, timeout=30)
            if response.status_code == 500:
                time.sleep(delay)
                continue
            break
        cache.set((url, data), response)

    log.info("Response: %s", response)

    return response


def delete(slug: str):
    url = f"{API}/{slug}"
    log.info("DELETE %s", url)

    for delay in [1, 3, 5]:
        response = requests.delete(url, timeout=30)
        if response.status_code == 500:
            time.sleep(delay)
            continue
        break

    log.info("Response: %s", response)

    cache.clear()

    return response
