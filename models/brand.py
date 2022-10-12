class Brand:

    def __init__(self, name, deactive, id = None):
        self.name = name
        self.id = id
        self.deactivate = deactive

    
    def chose_deactivated(self, deactivate):
        self.deactivate = deactivate

    