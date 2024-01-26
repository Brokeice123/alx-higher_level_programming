#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])

    if 'X-Request-Id' in r.headers:
        print(r.headers['X-Request-Id'])
