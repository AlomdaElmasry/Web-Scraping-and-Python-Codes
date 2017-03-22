import twitter

c_key = 'DYvKN0FoGBtMbx75ySGyY2daZ'
c_secret = 'AHnVMyqslbfzCtz3PMBAXQ1u6SeHg5vpy95oXwArZb00L4F1n4'
a_key = '2974062416-KAziUgk5jpzmQveUt1rjdNHu1tmu1Lb4b9VLvsX'
a_secret = 'mfiIqHfz1OL6H7dsoucuRDr2Xhxi3SEsOLYkYdsy7FUzA'


def get_tweets(user_id):
    api = twitter.Api(consumer_key=c_key, consumer_secret=c_secret, access_token_key=a_key,
                      access_token_secret=a_secret)

    # print api.VerifyCredentials()

    l = []
    t = api.GetUserTimeline(user_id=user_id, count=25)
    # print t
    tweets = [i.AsDict() for i in t]

    for i in tweets :
        l.append(i['text'])

    print l


ID = raw_input("Enter the user ID : ")
get_tweets(ID)

