class Garment:

    def __init__(self, name, brand, type, description, stock_quantity, buying_cost, selling_price, id = None):
        self.name = name
        self.brand = brand
        self.type = type
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.id = id

    def calculate_markup(self):
        markup = float(self.selling_price) - float(self.buying_cost) 
        return markup
        
