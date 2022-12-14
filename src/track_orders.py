class TrackOrders:
    def __init__(self) -> None:
        self.customers = dict()
        self.menu = set()
        self.open_days = dict()
        self.busiest_day = None
        self.less_busy_day = None

    def __len__(self):
        return len(self.customers)

    def update_most_ordered_dish(self, customer, order):
        customer_data = self.customers[customer]

        current_most_ordered = self.customers[customer]["most_ordered"]
        current_most_ordered_qt = customer_data["orders"][current_most_ordered]

        new_order_qt = customer_data["orders"][order]

        if new_order_qt > current_most_ordered_qt:
            self.customers[customer]["most_ordered"] = order

    def updated_customer_orders(self, customer, order):
        orders = self.customers[customer]["orders"]

        if order not in orders:
            orders[order] = 1
        else:
            orders[order] += 1

        self.update_most_ordered_dish(customer, order)

    def add_new_order(self, customer: str, order: set, day: int):
        if customer not in self.customers:
            self.customers[customer] = dict()
            self.customers[customer]["orders"] = dict()
            self.customers[customer]["days"] = set()
            self.customers[customer]["most_ordered"] = order

        self.menu.add(order)
        self.update_moviment_day(day)

        self.updated_customer_orders(customer, order)
        self.customers[customer]["days"].add(day)

    def get_most_ordered_dish_per_customer(self, customer):
        return self.customers[customer]["most_ordered"]

    def get_never_ordered_per_customer(self, customer):
        customer_orders = set(self.customers[customer]["orders"])
        return self.menu.difference(customer_orders)

    def update_busiest_day(self, day):
        if self.busiest_day:
            moviment_busiest_day = self.open_days[self.busiest_day]
            moviment_day = self.open_days[day]

            if moviment_day > moviment_busiest_day:
                self.busiest_day = day
        else:
            self.busiest_day = day

    def update_less_busy_day(self, day):
        if self.less_busy_day:
            moviment_less_busy_day = self.open_days[self.less_busy_day]
            moviment_day = self.open_days[day]

            if moviment_day < moviment_less_busy_day:
                self.less_busy_day = day
        else:
            self.less_busy_day = day

    def update_moviment_day(self, day):
        if day not in self.open_days:
            self.open_days[day] = 1
        else:
            self.open_days[day] += 1

        self.update_busiest_day(day)
        self.update_less_busy_day(day)

    def get_days_never_visited_per_customer(self, customer):
        customer_visted_days = self.customers[customer]["days"]
        return self.open_days.difference(customer_visted_days)

    def get_busiest_day(self):
        return self.busiest_day

    def get_least_busy_day(self):
        return self.less_busy_day
