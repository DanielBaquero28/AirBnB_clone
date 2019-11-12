#!/usr/bin/python3
""" Imports """
import json
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Class BaseModel """
    def __init__(self, *args, **kwargs):
        """ Instance Attribute """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key is 'created_at' or key is 'updated_at':
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

    def __str__(self):
        """ Instances methods
        Returns:
            class name
            id
            dictionary
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """" Save: save time update of date created an id """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ to_dict: contein whole intances of class
        Returns:
            dict_to
        """
        dict_to = dict(self.__dict__.items())
        dict_to.update({'__class__': self.__class__.__name__})
        dict_to.update({'created_at': self.created_at.isoformat()})
        dict_to.update({'updated_at': self.updated_at.isoformat()})
        return dict_to

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json string """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        objs = []
        if list_objs:
            for obj in list_objs:
                objs.append(obj.to_dict())
            with open(cls.__name__ + ".json", "w+") as f:
                f.write(
                    cls.to_json_string(objs))
            f.close()
        else:
            with open(cls.__name__ + ".json", "w+") as f:
                f.write(
                    cls.to_json_string(objs))
                f.close()