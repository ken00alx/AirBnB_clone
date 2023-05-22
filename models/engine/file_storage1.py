import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                from models.base_model import BaseModel
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = eval(class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
