#!/usr/bin/python3
""" Base Model Module """
import uuid
from datetime import datetime
from models import storage



class BaseModel():

    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic['created_at'] = datetime.isoformat(dic['created_at'])
        dic['updated_at'] = datetime.isoformat(dic['updated_at'])
        dic['__class__'] = self.__class__.__name__
        return dic

