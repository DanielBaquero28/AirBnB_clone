#!/usr/bin/python3
""" Importing necessary modules """
import json
from models.base_model import BaseModel
from os import path
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


<<<<<<< HEAD
=======
classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


>>>>>>> 2c4626de3bdb00eaf6e1f208ca258bb8b3f38a16
class FileStorage:
    """
    Serializes instances to a JSON files and deserializes
    JSON files to instances
    """
    __file_path = 'file.json'
    __objects = {}
<<<<<<< HEAD
    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review}

    def all(self):
        """ Returns __objects dictionary """
        return (FileStorage.__objects)
=======

    def all(self):
        """ Returns __objects dictionary """
        return (self.__objects)
>>>>>>> 2c4626de3bdb00eaf6e1f208ca258bb8b3f38a16

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """

        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        obj_dict = {}
<<<<<<< HEAD
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as my_file:
=======
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as my_file:
>>>>>>> 2c4626de3bdb00eaf6e1f208ca258bb8b3f38a16
            json.dump(obj_dict, my_file)

    def reload(self):
        """ Deserializes the JSON file if file exists """
<<<<<<< HEAD
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as my_file:
                str_dict = json.load(my_file)
                for element in str_dict.values():
                    class_name = element['__class__']
                    del element['__class__']
                    self.new(eval(class_name)(**element))
        except Exception:
            pass

    def delete(self, classes, Id):
        """ Delete object """
        obj = "{}.{}".format(classes, Id)
        FileStorage.__objects.pop(obj)
        self.save()
=======
        if path.exists(self.__file_path) is True:
            with open(self.__file_path, encoding='utf-8') as my_file:
                tmp_objs = json.load(my_file)
                for key, value in tmp_objs.items():
                    self.new(classes[value['__class__']](**value))
>>>>>>> 2c4626de3bdb00eaf6e1f208ca258bb8b3f38a16
