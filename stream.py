from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "841593479591473153-9eu1EoRkEo4jtUD4A5ljH6duwXpLFdb"
access_token_secret = "rq0IfvYm45Yev814JNYHNGatvMq88uYdIFgH9vADAiGZa"
consumer_key = "EEPcL9tQoKbBmOYb2CdYdrFiP"
consumer_secret = "76BEv6UZOiILkualRCWLY1kv8bHMaHpGEHl2QD2tEGSH49VevP"

# Definisi class listener untuk pengambilan tweet
class StdOutListener(StreamListener):
    def on_data(self, data):           
        #Tweet diambil berdasarkan Id, teks tweet dan waktu posting
        tweet=json.loads(data) #Convert tweet ke json
        created_at = tweet["created_at"] #ambil waktu posting
        id_str = tweet["id_str"] #ambil id teks tweet
        text = tweet["text"] #ambil teks tweet
        #Membuat dictionary obj
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        #memasukan dictionary obj kedalam mongodb
        tweetind=collection.insert_one(obj).inserted_id
        print obj #menampilkan obj yang telah di masukan ke dalam mongodb
        return True
        
    def on_error(self, status):
        #print error
        print status

if __name__ == '__main__':
    #Buat object StdOutListener untuk penanganan koneksi menuju Twitter Streaming API
    l = StdOutListener() 
    auth = OAuthHandler(consumer_key, consumer_secret) #proses autentikasi
    auth.set_access_token(access_token, access_token_secret) #setting access token
    stream = Stream(auth, l) #create kanal untuk streaming data

    # Below code  is for making connection with mongoDB
    from pymongo import MongoClient  
    client = MongoClient() #definisi object mongoclient
    client = MongoClient('localhost', 27017) #
    db = client.test_database
    collection = db.test_collection 
    
    #This line filter Twitter Streams to capture data by the keywords: 'India'
    stream.filter(track=['jokowi'])