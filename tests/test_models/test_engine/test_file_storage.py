#!/usr/bin/python3
"""
storage Test
"""
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
from time import sleep
import unittest


class test_fileStorage(unittest.TestCase):
    """Test_FileStorage Class"""
    def test_instances(self):
        """instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Check docstrings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    if __name__ == '__main__':
        unittest.main()
