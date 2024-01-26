#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter, and displays the result based on the conditions
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r = r.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get('id'), r.get('name')))
    except ValueError:
        print("Not a valid JSON")
