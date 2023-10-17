#!/usr/bin/python3
"""Write a Python function that changes all topics of a school

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """return that will update the topics"""
    return mongo_collection.update_many({"name": "name"},
                                        {"$set": {"topics": topics}})
