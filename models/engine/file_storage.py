import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Handles storage of objects in a JSON file."""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns all objects, or objects filtered by class."""
        if cls is None:
            return FileStorage.__objects
        else:
            # Filter and return objects of the given class
            filtered_objects = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    filtered_objects[key] = value
            return filtered_objects

    def new(self, obj):
        """Adds new object to __objects."""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves all objects to a JSON file."""
        with open(FileStorage.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()},
                      file, indent=4)

    def delete(self, obj=None):
        """Deletes an object from __objects."""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def reload(self):
        """Loads objects from the JSON file."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objs_dict = json.load(file)
                for key, obj_data in objs_dict.items():
                    class_name = obj_data['__class__']
                    cls = globals()[class_name]
                    obj = cls(**obj_data)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

