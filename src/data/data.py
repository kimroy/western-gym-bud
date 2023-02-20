import tweepy as tw
import re
import os
import psycopg2

def get_env_var(var):
    try:
        return os.environ.get(var)
    except ValueError:
        raise Exception(f'environment variable {var} isn\'t set properly')

POSTGRES_DB = get_env_var('POSTGRES_DB')
POSTGRES_USER = get_env_var('POSTGRES_USER')
POSTGRES_PASSWORD = get_env_var('POSTGRES_PASSWORD')
TWITTER_BEARER_TOKEN = get_env_var('TWITTER_BEARER_TOKEN')
TWITTER_USER = get_env_var('TWITTER_USER')

conn = psycopg2.connect(
    host = 'db',
    dbname = POSTGRES_DB,
    user = POSTGRES_USER,
    password = POSTGRES_PASSWORD
)
cur = conn.cursor()

class Stream(tw.StreamingClient):
    def on_connect(self):
        print("Connected to the Twitter API")


    def on_tweet(self, tweet):

        if tweet.referenced_tweets == None:
            tweet_content = tweet.text.split('\n')
            print(tweet_content)

            values = []

            for observed_num in tweet_content:
                # extract the value from each one
                match = re.search(r"\D*(\d+)", observed_num, re.IGNORECASE)
                if match is not None:
                    values.append(int(match.group(1)))

            if len(values) != 3:
                raise Exception(f'Not a valid input tweet from')
            
            
            cur.execute("CREATE TABLE IF NOT EXISTS tweets (tweet_id VARCHAR(50) PRIMARY KEY, wr integer, cm integer, spin integer);")
            cur.execute("INSERT INTO tweets (tweet_id, wr, cm, spin) VALUES (%s, %s, %s, %s);", (tweet.id, values[0], values[1], values[2]))
            conn.commit()

            cur.execute("SELECT * FROM tweets;")
            print(cur.fetchall())



def main():
    stream = Stream(bearer_token=TWITTER_BEARER_TOKEN)
    stream.add_rules(tw.StreamRule(value=f'from:{TWITTER_USER}'))
    stream.filter()

if __name__ == "__main__":
    main()