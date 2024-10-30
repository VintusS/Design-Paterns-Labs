from .MenuItem import MenuItem


class Menu:
    _instance = None

    def __init__(self):
        if Menu._instance is not None:
            raise Exception("This is a Singleton class.")
        self._menu_items: list[MenuItem] = []
        Menu._instance = self

    @staticmethod
    def get_instance():
        if Menu._instance is None:
            Menu._instance = Menu()
        return Menu._instance

    def add_menu_item(self, item: MenuItem = None):
        if item is None:
            raise Exception("Passed a NONE item.")
        else:
            self._menu_items.append(item)

    def get_menu_item(self, menu_item_name: str = None):
        for item in self._menu_items:
            if item.name == menu_item_name:
                return item
        print(f"Item {menu_item_name} not found in the menu.")
        return None

    def get_menu_items(self):
        return self._menu_items

    def __repr__(self) -> str:
        menu_string = "[MENU HAS THE FOLLOWING ITEMS]\n"
        for i, item in enumerate(self._menu_items):
            menu_string += f"{i+1}. {item}\n"
        return menu_string
