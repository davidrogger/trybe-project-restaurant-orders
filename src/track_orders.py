class TrackOrders:
    def __init__(self) -> None:
        self.customers = dict()

    def __len__(self):
        return len(self.customers)

    def updated_customer_orders(self, customer, order):
        orders = self.customers[customer]["orders"]

        if order not in orders:
            orders[order] = 1
        else:
            orders[order] += 1

    def add_new_order(self, customer: str, order: set, day: int):
        if customer not in self.customers:
            self.customers[customer] = dict()
            self.customers[customer]['orders'] = dict()
            self.customers[customer]['days'] = set()

        self.updated_customer_orders(customer, order)
        self.customers[customer]['days'].add(day)

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
