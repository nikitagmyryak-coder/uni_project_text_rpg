from entities.base_entity import Entity


class Merchant(Entity):
    def __init__(self):
        self.name = 'Merchant'
        self.description = "an walking merchant you have never met before(you will see him in between every level)"
        goods = []