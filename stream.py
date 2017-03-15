from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "3988970534-R3WB1SyJapm9W0whxhLdrHPeei26rWxa8TySngh"
access_token_secret = "27IvlcKP1pbg9AptfR8qjOiZkvzbulG04Na4HSEEq3CGL"
consumer_key = "XAxTRxIJ9xCCIYUWBzctxJWLB"
consumer_secret = "fuLWO2L4tpP63vo5vOxdUXJhndKJzs7LpdqX88dUw9KjxZf7MH"

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