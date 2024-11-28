from menu.MenuItem import MenuItem


class Order(MenuItem):
    def __init__(self, items: list[MenuItem] = []) -> None:
        self.items = items
        if len(items) == 0:
            super().__init__("Order", 0)
        else:
            super().__init__(self.get_name(), self.get_price())

    def get_name(self):
        return ', '.join(item.get_name() for item in self.items)

    def add(self, item: MenuItem):
        self.items.append(item)

    def get_price(self) -> float:
        return sum(item.get_price() for item in self.items)

    def get_items(self):
        return self.items

    def show(self) -> str:
        return "\n".join(item.show() for item in self.items)

    def __str__(self) -> str:
        return f"Order: {self.get_name()} - {self.get_price()}"
