#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response
"""

import sys
import requests


if __name__ == '__main__':
    email = {'email': argv[2]}
    request = requests.post(argv[1], data=email)

    print(request.text)
