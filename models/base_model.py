#!/usr/bin/python3
"""
This is a base model class doing wjat ot does
"""
from uuid import uuid4 
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        

    def __str__(self):
        return f'[self.__class__.__name__] (self.id) self.__dict__'
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__
        dict[__class__] = self.__class__.__name__

        for key,value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dict[key] = value.isoformat() 
        return dict
    

    
        