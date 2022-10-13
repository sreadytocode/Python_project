import unittest
from models.image import Image

class TestImage(unittest.TestCase):

    def setUp(self):
        self.image = Image("random-image", 5)

    def test_image_has_name(self):
        self.assertEqual("random-image", self.image.name)

    def test_image_has_garment(self):
        self.assertEqual(5, self.image.garment)