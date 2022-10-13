import unittest
from models.type import Type

class TestType(unittest.TestCase):

    def setUp(self):
        self.type = Type("Shirt")

    def test_type_has_type_of_garment(self):
        self.assertEqual("Shirt", self.type.type)