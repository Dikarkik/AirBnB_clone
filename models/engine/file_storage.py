#!/usr/bin/python3
import json
from datetime import datetime


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        from models.base_model import BaseModel
        from models.user import User

        options = {'BaseModel': BaseModel, 'User': User}
        return options

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        di = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(di, file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dicts = json.load(file)
            for obj_key, obj_dic in obj_dicts.items():
                instance = self.classes()[obj_dic['__class__']](**obj_dic)
        except:
            pass
