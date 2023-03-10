"""Here we connect to Mongodb"""

from pymongo import MongoClient
class Mongodb:
    isnstance = None
    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.isnstance is None:
            cls.isnstance = super().__new__(*args, **kwargs)
        return cls.isnstance

    def __init__(self):
        self.client = MongoClient()
