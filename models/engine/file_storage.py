#!/usr/bin/python3
""" Importing necessary modules """
import json
from models.base_model import BaseModel
from os import path
<<<<<<< HEAD
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review
=======
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
>>>>>>> 80e25cab0c4758f606430f345365feb16d6e628a

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}

class FileStorage:
    """
    Serializes instances to a JSON files and deserializes
    JSON files to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns __objects dictionary """
        return (FileStorage.__objects)

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """

        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as my_file:
            json.dump(obj_dict, my_file)

    def reload(self):
        """ Deserializes the JSON file if file exists """
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as my_file:
                str_dict = json.load(my_file)
                for element in str_dict.values():
                    class_name = element['__class__']
                    del element['__class__']
                    self.new(eval(class_name)(**element))
        except Exception:
            pass
