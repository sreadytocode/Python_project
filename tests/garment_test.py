import unittest
from models.garment import Garment

class TestGarment(unittest.TestCase):

    def setUp(self):
        self.garment = Garment("Mint and gold dress", 2, 3, "Celestial mint and gold dress with embroidered chiffon and silk.", 15, 100.00, 165.00)

    def test_garment_has_name(self):
        self.assertEqual("Mint and gold dress", self.garment.name)

    def test_garment_has_allocated_brand(self):
        self.assertEqual(2, self.garment.brand)

    def test_garment_has_allocated_type(self):
        self.assertEqual(3, self.garment.type)

    def test_garment_has_description(self):
        self.assertEqual("Celestial mint and gold dress with embroidered chiffon and silk.", self.garment.description)

    def test_garment_has_stock_quantity(self):
        self.assertEqual(15, self.garment.stock_quantity)

    def test_garment_has_buying_cost(self):
        self.assertEqual(100.00, self.garment.buying_cost)

    def test_garment_has_selling_price(self):
        self.assertEqual(165.00, self.garment.selling_price)

    def test_garment_can_calculate_markup(self):
        result = self.garment.calculate_markup()
        self.assertEqual(65.00, result)