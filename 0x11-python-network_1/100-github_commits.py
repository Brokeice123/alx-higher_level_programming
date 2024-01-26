#!/usr/bin/python3
"""
Lists 10 most recent commits from a given GitHub repository
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    commits = r.json()
    for commit in commits[:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
