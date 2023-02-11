#!/usr/python3

import unittest
import uuid
import datetime
from models import storage
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)
        self.assertEqual(self.base_model.created_at, self.base_model.updated_at)

    def test_str(self):
        self.assertIsInstance(str(self.base_model), str)

    def test_save(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)
        self.assertIn(self.base_model, storage.all().values())

    def test_to_dict(self):
        self.assertIsInstance(self.base_model.to_dict(), dict)
        self.assertEqual(self.base_model.to_dict()['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(self.base_model.to_dict()['updated_at'], self.base_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
