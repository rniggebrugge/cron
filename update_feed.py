import feedparser
import json
import requests
from datetime import datetime
import os

full_name = os.getenv('FULL_NAME')

RSS_FEED_URL = 'https://feeds.megaphone.fm/newheights'
JSON_FILE_PATH = 'rss_data.json' 

def fetch_and_save_feed():
    feed = feedparser.parse(RSS_FEED_URL)
    entries = feed.entries

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data_with_timestamp = {
        'timestamp': timestamp,
        'full_name' : full_name,
        'entries': entries
    }

    with open(JSON_FILE_PATH, 'w') as json_file:
        json.dump(data_with_timestamp, json_file, indent=2)

if __name__ == '__main__':
    fetch_and_save_feed()