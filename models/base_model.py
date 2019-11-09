#!/usr/bin/python3
""" Imports """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Class BaseModel """
    def __init__(self):
        """ Instance Attribute """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """ Instances methods
        Returns:
            class name
            id
            dictionary
        """
        return "[{}] ({}) {}".format(str(self.__class__.__name__),
                                     self.id, self.__dict__)

    def save(self):
        """" Save: sve time update of date created an id """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ to_dict: contein whole intances of class
        Returns:
            dict_to
        """
        dict_to = dict(self.__dict__.items())
        dict_to.update({'__class__': self.__class__.__name__})
        dict_to['created_at'] = self.created_at.isoformat()
        dict_to['updated_at'] = self.updated_at.isoformat()
        return dict_to
