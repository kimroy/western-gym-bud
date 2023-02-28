import re

import pytz
import tweepy as tw
from snscrape.modules import twitter as sntwitter

from db import Database
from tweet import Tweet
from helper_functions import get_env_var

TWITTER_USER = get_env_var('TWITTER_USER')
SINCE_SEARCH = get_env_var('SINCE_SEARCH')
UNTIL_SEARCH = get_env_var('UNTIL_SEARCH')

def parse_tweet_values(tweet_text: list) -> list:
    values = []
    for line in tweet_text:
        # extract the value from each one
        match = re.search(r"\D*(\d+)", line, re.IGNORECASE)
        if match is not None:
            values.append(int(match.group(1)))
    return values

def set_timezone_to_est(tweet_timestamp):
    est = pytz.timezone('US/Eastern')
    return tweet_timestamp.date.astimezone(est)

def is_tweet_valid(tweet_values: list) -> bool:
    return len(tweet_values) == 3

def main():
    db = Database()
    scraper = sntwitter.TwitterSearchScraper(f'from:{TWITTER_USER} until:{UNTIL_SEARCH} since:{SINCE_SEARCH}')
    db.create_table()
    with db.conn.cursor() as cur:
        for tweet in scraper.get_items():
            print(tweet.date)
            cleaned_tweet = tweet.renderedContent.split('\n')
            values = parse_tweet_values(cleaned_tweet)

            if is_tweet_valid(values):
                dt = set_timezone_to_est(tweet)
                tweet_obj = Tweet(tweet.id, dt.date(), dt.time(), values[0], values[1], values[2])
                db.insert(cur, tweet_obj)

        
if __name__ == "__main__":
    main()
