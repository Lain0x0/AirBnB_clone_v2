#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a list of objects of a specific class type"""
        if (cls is not None):
            cls = eval(cls)
            return {k: v for k, v in
                    self._objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.to_dict()['__class__']}.{obj.id}"
        self._objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {key: val.to_dict() for key, val in self._objects.items()}
        with open(self._file_path, 'w') as f:
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(self._file_path, 'r') as f:
                temp = json.load(f)
            for key, val in temp.items():
                if HBNBCommand:
                    class_ = HBNBCommand.classes.get(val['__class__'])
                    if class_:  # Check if class exists before instantiation
                        self._objects[key] = class_(**val)
                else:
                    # Handle case where HBNBCommand is not provided
                    pass  # Or raise an exception
        except FileNotFoundError:
            pass
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }

    def delete(self, obj=None):
        """ Deletes an object from storage """
        if obj is None:
            return  # No object provided, nothing to delete

        try:
            key = f"{type(obj).__name__}.{obj.id}"
            del self._objects[key]
            obj.delete()  # Assuming models have a delete method
            print(f"Deleted {key}")
        except (AttributeError, KeyError):
            pass  # Handle missing object or delete method

    def close(self):
        """Saves objects to file and closes session (optional)"""
        self.save()
