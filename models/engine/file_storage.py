#!/usr/bin/python3

import json
from datetime import datetime

class FileStorage():
    __file_path = "file.json"
    __objects = {}

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
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dicts = json.load(file)
            for obj_key, obj_dic in obj_dicts.items():
                if obj_dic['__class__'] == "BaseModel":
                    instance = BaseModel(**obj_dic)
                FileStorage.__objects[obj_key] = instance
        except:
            pass
