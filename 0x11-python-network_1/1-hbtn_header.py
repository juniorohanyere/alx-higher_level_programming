#!/usr/bin/python3
"""akes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""

from urllib.request import urlopen, Request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    request = Request(url)

    with urlopen(request) as response:
        print(dict(response.headers).get('X-Request-Id'))
