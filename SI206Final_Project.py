## SI 206 2017
## Final Project
## Alex Shell

import unittest
import itertools
import collections
import facebook
import facebook_info #protects information
import json
import sqlite3
import requests

## Facebook Setup
access_token = facebook_info.access_token

graph = facebook.GraphAPI(access_token=token, version = 2.7)

## Caching Setup
CACHE_FNAME = "facebook_cache.json"

try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}


## Utilizing API
def get_facebook_data(user):
    if user in CACHE_DICTION:
		print('User Previously Searched: Accessing Cache')
    else:
		print('New User Search: Processing API Request')
        facebook_results = graph.get_connections(user, feed, limit=100)
        CACHE_DICTION[user] = facebook_results
        f = open(CACHE_FNAME,'w')
		f.write(json.dumps(CACHE_DICTION, indent=4))
		f.close()
    return CACHE_DICTION[user]


## Database Setup
conn = sqlite3.connect('206_APIsAndDBs.sqlite')
cur = conn.cursor()
