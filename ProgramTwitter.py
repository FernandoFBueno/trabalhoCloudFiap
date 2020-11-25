import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import time

phrase_to_search = 'Bolsonaro'

print(phrase_to_search);

consumer_key = 'IBBIFNKEz3F2mts8YjCzu7w4T'
consumer_secret = 'KfYGUKDmcRp7rvKcSEJ96ILfN2EVz8KWWfCkoFByCocoNz7dvb'
access_token = '344908066-4Fo1A0ecqQHnMlgmVHJr3XO8UjOv0nli2FRKaByo'
access_secret = '1UQyvz8B7ynJysrGsFDYnDY390iHkM8jEZtXvkMf0RVYl'

g = []


class StdOutListener(StreamListener):
    def on_data(self, data):
        # Streaming API. Streaming API fetches live tweets
        print(data)
        g.append(data)
        time.sleep(2)
        return True

    # To print the status if an error happens
    def on_error(self, status):
        print(status)


def call_api(stream, phrase):
    # If the time crosses the amount of time mentioned by t_end, then the tweet scrapping stops
    try:
        print("teste 1")
        stream.filter(track=[phrase])
        print("teste 1")
    except Exception as e:
        print(e)

    # If the stream is already connected, the following will disconnect the stream and reconnect it
    if "Stream object already connected!" in str(e):
        stream.disconnect()
        print("connecting again")
        stream.filter(track=[phrase])


if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, listener)
    call_api(stream, phrase_to_search)



