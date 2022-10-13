import unittest
from models.brand import Brand

class TestBrand(unittest.TestCase):
    
    def setUp(self):
        self.brand = Brand("Maria B", False)

    def test_brand_has_name(self):
        self.assertEqual("Maria B", self.brand.name)

    def test_brand_has_deactivate_status(self):
        self.assertEqual(False, self.brand.deactivate)