class TrackOrders:
    def __init__(self):
        self.orders = []
        self._orders_count = 0
        self.customer_dishes = dict()
        self.customer_days = dict()
        self.day_counts = dict()
        self.dish_counts = dict()

    def __len__(self):
        self._orders_count = len(self.orders)
        return self._orders_count

    def add_new_order(self, customer, order, day):
        self.add_order(order)
        self.update_customer_dishes(customer, order)
        self.update_customer_days(customer, day)
        self.update_day_counts(day)
        self.update_dish_counts(order)

    def add_order(self, order):
        self.orders.append(order)

    def update_customer_dishes(self, customer, dish):
        if customer not in self.customer_dishes:
            self.customer_dishes[customer] = dict()
        if dish not in self.customer_dishes[customer]:
            self.customer_dishes[customer][dish] = 0
        self.customer_dishes[customer][dish] += 1

    def update_customer_days(self, customer, day):
        if customer not in self.customer_days:
            self.customer_days[customer] = dict()
        if day not in self.customer_days[customer]:
            self.customer_days[customer][day] = 0
        self.customer_days[customer][day] += 1

    def update_day_counts(self, day):
        if day not in self.day_counts:
            self.day_counts[day] = 0
        self.day_counts[day] += 1

    def update_dish_counts(self, dish):
        if dish not in self.dish_counts:
            self.dish_counts[dish] = 0
        self.dish_counts[dish] += 1

    def get_most_ordered_dish_per_customer(self, customer):
        if customer not in self.customer_dishes:
            return None
        dishes = self.customer_dishes[customer]
        return max(dishes, key=dishes.get)

    def get_never_ordered_per_customer(self, customer):
        if customer not in self.customer_dishes:
            return set(self.dish_counts.keys())
        customer_dishes = set(self.customer_dishes[customer].keys())
        all_dishes = set(self.dish_counts.keys())
        return all_dishes - customer_dishes

    def get_days_never_visited_per_customer(self, customer):
        if customer not in self.customer_days:
            return set(self.day_counts.keys())
        customer_days = set(self.customer_days[customer].keys())
        all_days = set(self.day_counts.keys())
        return all_days - customer_days

    def get_busiest_day(self):
        return max(self.day_counts, key=self.day_counts.get)

    def get_least_busy_day(self):
        return min(self.day_counts, key=self.day_counts.get)
