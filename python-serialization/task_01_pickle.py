#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize object and save it to file.

        Parameters:
        filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred while serializing the object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize object from file.

        Parameters:
        filename (str): The name of the file to load serialized object from.

        Returns:
        CustomObject: The deserialized object or None if an error occurred.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"An error occurred while deserializing the object: {e}")
            return None
