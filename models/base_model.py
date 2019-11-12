#!/usr/bin/python3
""" Importing necessary modules """
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """ SuperClass from which the rest of the classes will inherit """
    def __init__(self, *args, **kwargs):
        """ Constructor method """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns the string representation of class name, id and dict """
        class_name = str("[" + self.__class__.__name__ + "]")
        instance_id = str("(" + self.id + ")")
        instance_dict = str(self.__dict__)
        return (class_name + " " + instance_id + " " + instance_dict)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key/values of instance """
        dict_str = self.__dict__.copy()
        dict_str['__class__'] = self.__class__.__name__
        dict_str['created_at'] = self.created_at.isoformat()
        dict_str['updated_at'] = self.updated_at.isoformat()

        return (dict_str)
