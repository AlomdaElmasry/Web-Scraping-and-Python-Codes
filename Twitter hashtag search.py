import tweepy

c_key = 'DYvKN0FoGBtMbx75ySGyY2daZ'
c_secret = 'AHnVMyqslbfzCtz3PMBAXQ1u6SeHg5vpy95oXwArZb00L4F1n4'
a_key = '2974062416-KAziUgk5jpzmQveUt1rjdNHu1tmu1Lb4b9VLvsX'
a_secret = 'mfiIqHfz1OL6H7dsoucuRDr2Xhxi3SEsOLYkYdsy7FUzA'


def get_tweets(text):
    OAUTH_KEYS = {'consumer_key': c_key, 'consumer_secret': c_secret,
                  'access_token_key': a_key, 'access_token_secret': a_secret}
    auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
    api = tweepy.API(auth)

    t = tweepy.Cursor(api.search, q=text).items(25)
    l = []

    for i in t:
        l.append(i.text)

    print l


t = raw_input("Enter the text : ")
get_tweets(t)