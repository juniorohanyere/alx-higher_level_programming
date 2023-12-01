#!/usr/bin/python3
"""takes a GitHub credentials (username and password) and uses the GitHub API
to display the id
"""

import sys
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    request = requests.get(url, auth=requests.auth.HTTPBasicAuth(sys.argv[1],
                                                                 sys.argv[2]))

    print(request.json().get('id'))
