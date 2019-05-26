#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#pip3 install pymongo 


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fix"]
myCollectionPartner = mydb["partner"]
myCollectionClient = mydb["client"]

mydict = { "name": "Jose", "address": "Germany", "creditcard": "0000" }

x = myCollectionPartner.insert_one(mydict)

mydict = { "name": "MarMar", "address": "USA", "creditcard": "FFFF" }

x = myCollectionClient.insert_one(mydict)

