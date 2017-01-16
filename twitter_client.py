
import twitter
from twitter import TwitterError
import urllib2

""" uses http://code.google.com/p/python-twitter/
    easy_install python-twitter
"""

MAX_TWEETS = 300
TWEETS_PER_QUERY = 200
def get_twitter_api():

    api = twitter.Api(
        consumer_key = "qgaK3jSAvX8qz0K5wuYtpv63P",
        consumer_secret = "votqJloq4alvdMHjL49ji8SYQ0ZHSd3OZFTKdUvyKV1vxe1y9h",
        access_token_key = "18426999-SnTsi76bAC1XObm7JxtdAhFQItZycO7FkXgoPGUyM",
        access_token_secret = "ImpgKgSP9OSEbkchOVqiSFH3SRUqNV0Q1Vs2cJQ7ZYyqs")
    return api

def read_tweets(api, user):
    """ reads user's tweets
    """
    max_id = None

    statuses = []

    while True:
        new_statuses = []
        try:
            new_statuses = api.GetUserTimeline(screen_name=user,
                count=TWEETS_PER_QUERY, include_rts=True, max_id=max_id,
                since_id=None)
        except (TwitterError, urllib2.HTTPError) as e:
            print e

        if len(new_statuses) > 0:
            statuses.extend(new_statuses)
            max_id = new_statuses[-1].id - 1
        else:
            break

    print "Fetched", len(statuses), "tweets."

    if statuses > 0:

        if len(statuses) >= 10:
            for status in statuses:
                print status.text + "\n"

    return statuses

def main():
    """
        read tweets
    """
    twitter_api = get_twitter_api()
    twitter_handle = "nyndpv"
    read_tweets(twitter_api, twitter_handle)
if __name__ == '__main__':
    main()
