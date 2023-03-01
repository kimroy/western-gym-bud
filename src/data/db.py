import psycopg2

from helper_functions import get_env_var

POSTGRES_DB = get_env_var('POSTGRES_DB')
POSTGRES_USER = get_env_var('POSTGRES_USER')
POSTGRES_PASSWORD = get_env_var('POSTGRES_PASSWORD')


class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host='db',
                dbname=POSTGRES_DB,
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD
            )

        except ConnectionError:
            raise Exception(f'Unable to open a connection to {POSTGRES_DB}')

    def insert(self, cur, tweet_obj) -> None:
        print(type(tweet_obj.wr))
        cur.execute("INSERT INTO tweets (id, date, time, wr, cm, spin) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (id) do nothing;", (tweet_obj.id, tweet_obj.date, tweet_obj.time, tweet_obj.wr, tweet_obj.cm, tweet_obj.spin))
        self.conn.commit()

    def create_table(self, cur) -> None:
        cur.execute("CREATE TABLE IF NOT EXISTS tweets \
            (id bigint PRIMARY KEY, \
            date date, \
            time time, \
            wr integer, \
            cm integer, \
            spin integer);")
        self.conn.commit()

    def check_duplicate_entry(self, cur, tweet_id) -> bool:
        cur.execute("""
            SELECT 1 FROM tweets 
            WHERE id = %s;
        """, (tweet_id,))
        return cur.fetchone()