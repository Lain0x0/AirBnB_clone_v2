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
            return {k: v for k, v in
                    self._objects.items() if isinstance(v, cls)}
        return self._objects.copy()
    # Return a copy to avoid modifying original dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

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
