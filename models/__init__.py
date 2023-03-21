#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from .engine.file_storage import FileStorage
from .engine.db_storage import DBStorage
from .engine.db_storage import HBNB_TYPE_STORAGE

if HBNB_TYPE_STORAGE == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
