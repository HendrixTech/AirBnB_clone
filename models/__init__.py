#!/usr/bin/python3

"""create a unique FileStorage instance for the application"""
from AirBnB_clone.models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
