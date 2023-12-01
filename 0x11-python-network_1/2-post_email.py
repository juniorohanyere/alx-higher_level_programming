#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response (decoded in
utf-8)
"""

import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode


if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urlencode(value).encode('ascii')
    request = Request(url, data)

    with urlopen(request) as response:
        print(response.read().decode('utf-8'))
