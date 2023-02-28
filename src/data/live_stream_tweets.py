###
#   Currently not in use, it is much easier to maintain data by manually running the bulk script on a periodic basis versus having a
#   constant open stream listening for tweets.
###
# class Stream(tw.StreamingClient):

#     def __init__(self, bearer_token):
#         super().__init__(bearer_token)
#         self.db = Database()


#     def on_connect(self):
#         print( 'API Connected')


#     def on_tweet(self, tweet):
#         # If the tweet recieved is a direct tweet
#         if tweet.referenced_tweets == None:
#             tweet_id = tweet.data['id']
#             created_at_est = self.convert_dt_to_est(tweet.data['created_at'])
#             values = self.parse_values(tweet.data['text'].split('\n'))
#             self.is_tweet_valid(values)

#             # If everything about the tweet is valid then create the object
#             tweet_obj = Tweet(tweet_id, created_at_est.date(), created_at_est.time(), values[0], values[1], values[2])
            
#             self.db.create_table()
#             self.db.insert(tweet_obj)


#     def parse_values(self, text):
#         values = []
#         for num in text:
#             # extract the value from each one
#             match = re.search(r"\D*(\d+)", num, re.IGNORECASE)
#             if match is not None:
#                 values.append(int(match.group(1)))
#         return values


#     def is_tweet_valid(self, values):
#         if len(values) != 3:
#             raise Exception(f'Not a valid input tweet')


    # def convert_dt_to_est(self, created_at):
    #     return datetime.strptime(created_at ,"%Y-%m-%dT%H:%M:%S.%fZ").astimezone(timezone('US/Eastern'))



# def main():
#     ### For when we want to have a stream of live tweets with open ports
#     # stream = Stream(bearer_token=TWITTER_BEARER_TOKEN)
#     # stream.add_rules(tw.StreamRule(value=f'from:{TWITTER_USER}'))
#     # stream.filter(tweet_fields=["created_at"])
    
    

# if __name__ == "__main__":
#     main()