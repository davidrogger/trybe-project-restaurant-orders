from src.track_orders import TrackOrders


class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    CURRENT_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.track_orders = TrackOrders()

    def check_ingredients_available(self, ingredients: list):
        for ingredient in ingredients:
            quantity = self.CURRENT_INVENTORY[ingredient]
            if quantity == 0:
                raise ValueError("Insufficient quantity")

    def check_stock(self, order):
        ingredients = self.INGREDIENTS[order]

        self.check_ingredients_available(ingredients)

    def add_new_order(self, customer, order, day):
        pass

    def get_quantities_to_buy(self):
        pass
