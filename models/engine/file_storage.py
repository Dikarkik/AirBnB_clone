#!/usr/bin/python3
import json
from datetime import datetime


class FileStorage():
    """ FileStorage.
    Private class attribute:
        __file_path
        __objects
    Public instance methods:
        classes
        all
        new
        save
        reload
    """
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """ Method that return a dict of the classes """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        options = {'BaseModel': BaseModel,
                   'User': User,
                   'State': State,
                   'City': City,
                   'Amenity': Amenity,
                   'Place': Place,
                   'Review': Review}
        return options

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            di = {key: value.to_dict()
                  for key, value in FileStorage.__objects.items()}
            json.dump(di, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dicts = json.load(file)
            for obj_key, obj_dic in obj_dicts.items():
                instance = self.classes()[obj_dic['__class__']](**obj_dic)
        except:
            pass
