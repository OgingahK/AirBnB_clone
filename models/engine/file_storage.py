#!/usr/bin/python3

"""FileStorage class module"""
import datetime
import json
import os

class FileStorage:
    """Class that stores and retrieves data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """dictionary __objects are returned"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k:v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Valid classes and their references are returned using dictionary"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
        return classes

    def reload(self):
        """Reloads the storage objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                    for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Valid attributes and their classname types are returned"""
        attributes = {
                "BaseModel":
                            {"id": str,
                                "created_at": datetime.datetime,
                                "updated_at": datetime.datetime},
                "User":
                       {"email": str,
                        "password": str,
                        "first_name": str,
                        "last_name": str},
                
                "State":
                        {"name": str},

                "City":
                       {"state_id": str,
                        "name": str},

                "Amenity":
                          {"name": str},

                "Place":
                        {"city_id": str,
                            "user_id": str,
                            "name": str,
                            "description": str,
                            "number_rooms": int,
                            "number_bathrooms": int,
                            "max_guest": int,
                            "price_by_nigt": int,
                            "latitude": float,
                            "longitude": float,
                            "amenity_ids": list},
               "Review":
                        {"place_id": str,
                            "user_id": str,
                            "text": str}
            }
        return attributes
