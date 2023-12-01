#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    url = 'http://0.0.0.0:5000/search_user'
    request = requests.post(url, data={'q': letter})

    try:
        req = request.json()
        if len(req) == 0 or 'id' not in req or 'name' not in req:
            print("No result")
        else:
            id = req.get('id')
            name = req.get('name')

            print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
