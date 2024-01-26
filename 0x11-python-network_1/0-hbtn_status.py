#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        print('Body response:')
        print('\t- type: {}'.format(type(r)))
        print('\t- content: {}'.format(r.read()))
        print('\t- utf8 content: {}'.format(r.read().decode('utf-8')))
