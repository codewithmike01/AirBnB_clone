#!/usr/bin/python3
"""
This is a base model class doing wjat ot does
"""
from uuid import uuid4 


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
      