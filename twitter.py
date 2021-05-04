import tweepy
import logging
from config import consumer_key, consumer_secret, access_token, access_token_secret
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
#
# class listener(tweepy.StreamListener):
#     # def __init__(self, api):
#     #     self.api = api
#     #     self.me = api.me()
#
#     def on_status(self, tweet):
#         print("on_status")
#         logger.info(f"Processing tweet id {tweet.id}")
#         # if tweet.in_reply_to_status_id is not None or \
#         #     tweet.user.id == self.me.id:
#         #     # This tweet is a reply or I'm its author so, ignore it
#         #     return
#         if not tweet.favorited:
#             # Mark it as Liked, since we have not done it yet
#             try:
#                 tweet.favorite()
#                 print(tweet)
#             except Exception as e:
#                 logger.error("Error on fav", exc_info=True)
#         # if not tweet.retweeted:
#         #     # Retweet, since we have not retweeted it yet
#         #     try:
#         #         tweet.retweet()
#         #     except Exception as e:
#         #         logger.error("Error on fav and retweet", exc_info=True)
#
#     def on_error(self, status):
#         logger.error(status)

def main():
    # api = create_api()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    # print(api.user_timeline(screen_name="iimunofficial"))
    tweets = api.user_timeline(screen_name="iimunofficial", count=200)

    for tweet in tweets:
        if not tweet.favorited:
            try:
                tweet.favorite()
                print("Liked:", tweet, "\n")
            except Exception as e:
                logger.error("Error on tweet", exc_info=True)

    # tweets_listener = listener(api)
    # stream = tweepy.Stream(api.auth, tweets_listener)
    # # stream.filter(track=keywords, languages=["en"])
    # stream.filter(follow=['975728688'])

main()

# if __name__ == "__main__":
#     main(["iimun", "IIMUN"])



