from flask import Flask,render_template,session
from pymongo import MongoClient
from flask_pymongo import pymongo
from bson import json_util
import json


app = Flask(__name__)
cclient = pymongo.MongoClient("mongodb://Sriram725:Sriram007@ac-3dhryti-shard-00-00.vlc2bke.mongodb.net:27017,ac-3dhryti-shard-00-01.vlc2bke.mongodb.net:27017,ac-3dhryti-shard-00-02.vlc2bke.mongodb.net:27017/?ssl=true&replicaSet=atlas-ok5ehc-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cclient['collectionone']
collection = db['collectionone']
@app.route('/')
def getdata():
        all_seeds = list(collection.find({}))
        return json.dumps(all_seeds, default=json_util.default)

if __name__ == "__main__":
    app.run()


