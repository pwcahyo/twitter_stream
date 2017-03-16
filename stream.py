from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "841593479591473153-9eu1EoRkEo4jtUD4A5ljH6duwXpLFdb"
access_token_secret = "rq0IfvYm45Yev814JNYHNGatvMq88uYdIFgH9vADAiGZa"
consumer_key = "EEPcL9tQoKbBmOYb2CdYdrFiP"
consumer_secret = "76BEv6UZOiILkualRCWLY1kv8bHMaHpGEHl2QD2tEGSH49VevP"

# Defining listener class for getting the streaming
class StdOutListener(StreamListener):
    def on_data(self, data):           
        #Retrieving the details like Id, tweeted text and created at.
        tweet=json.loads(data)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        tweetind=collection.insert_one(obj).inserted_id
        print obj
        return True
        
    def on_error(self, status):
        print status

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming AP
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Below code  is for making connection with mongoDB
    from pymongo import MongoClient   
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.test_database
    collection = db.test_collection 
    #This line filter Twitter Streams to capture data by the keywords: 'India'
    stream.filter(track=['jokowi'])