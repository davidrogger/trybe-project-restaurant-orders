from src.track_orders import TrackOrders


INITIAL_INVENTORY = {
    "pao": 50,
    "carne": 50,
    "queijo": 100,
    "molho": 50,
    "presunto": 50,
    "massa": 50,
    "frango": 50,
}


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

    NEED_TO_BUY = {
        "pao": 0,
        "carne": 0,
        "queijo": 0,
        "molho": 0,
        "presunto": 0,
        "massa": 0,
        "frango": 0,
    }

    AVAILABLE_DISHES = {"hamburguer", "pizza", "misto-quente", "coxinha"}

    def __init__(self, inventory=INITIAL_INVENTORY):
        self.track_orders = TrackOrders()
        self.current_inventory = inventory

    def check_ingredients_available(self, ingredients: list):
        for ingredient in ingredients:
            quantity = self.current_inventory[ingredient]
            if quantity == 0:
                raise ValueError("Insufficient quantity")

    def consuming_inventory(self, ingredients):
        for ingredient in ingredients:
            self.current_inventory[ingredient] -= 1
            self.NEED_TO_BUY[ingredient] += 1
            if not self.current_inventory[ingredient]:
                self.update_available_dishes(ingredient)

    def inventory_moviment(self, order):
        ingredients = self.INGREDIENTS[order]

        self.check_ingredients_available(ingredients)
        self.consuming_inventory(ingredients)

    def add_new_order(self, customer, order, day):
        try:
            self.inventory_moviment(order)
            self.track_orders.add_new_order(customer, order, day)
        except ValueError:
            return False

    def get_quantities_to_buy(self):
        return self.NEED_TO_BUY

    def update_available_dishes(self, ingredient):
        dishe_unavailable = set()

        for dishe in self.AVAILABLE_DISHES:
            if ingredient in self.INGREDIENTS[dishe]:
                dishe_unavailable.add(dishe)

        updated_available_dishes = self.AVAILABLE_DISHES.difference(
            dishe_unavailable
        )

        self.AVAILABLE_DISHES = updated_available_dishes

    def get_available_dishes(self):
        return self.AVAILABLE_DISHES
