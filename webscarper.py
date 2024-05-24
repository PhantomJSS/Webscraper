from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import regex as re
import http.client
import json
import requests

pd.set_option('display.max_rows', None)
pd.set_option('mode.chained_assignment', None)

conn = http.client.HTTPSConnection('www.zillow.com')
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.zillow.com',
    'priority': 'u=1, i',
    'referer': 'https://www.zillow.com/toronto-on/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}
json_data = {
    'searchQueryState': {
        'pagination': {},
        'isMapVisible': False,
        'mapBounds': {
            'west': -79.77807212207031,
            'east': -78.97469687792969,
            'south': 43.50672472489649,
            'north': 43.90877235887992,
        },
        'regionSelection': [
            {
                'regionId': 792680,
                'regionType': 6,
            },
        ],
        'filterState': {
            'sortSelection': {
                'value': 'globalrelevanceex',
            },
            'isAllHomes': {
                'value': True,
            },
        },
        'isListVisible': True,
        'mapZoom': 11,
    },
    'wants': {
        'cat1': [
            'listResults',
        ],
        'cat2': [
            'total',
        ],
    },
    'requestId': 3,
    'isDebugRequest': False,
}
conn.request(
    'PUT',
    '/async-create-search-page-state',
    json.dumps(json_data),
    # '{"searchQueryState":{"pagination":{},"isMapVisible":false,"mapBounds":{"west":-79.77807212207031,"east":-78.97469687792969,"south":43.50672472489649,"north":43.90877235887992},"regionSelection":[{"regionId":792680,"regionType":6}],"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true,"mapZoom":11},"wants":{"cat1":["listResults"],"cat2":["total"]},"requestId":3,"isDebugRequest":false}',
    headers
)
response = conn.getresponse()