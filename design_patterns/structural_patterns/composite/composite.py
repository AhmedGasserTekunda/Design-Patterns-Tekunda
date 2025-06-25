class MenuItem:
    def display(self):
        raise NotImplementedError()


class Dish(MenuItem):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Dish: {self.name}")


class Menu(MenuItem):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def display(self):
        print(f"Menu: {self.name}")
        for item in self.items:
            item.display()


if __name__ == "__main__":
    breakfast = Menu("Breakfast Menu")
    breakfast.add(Dish("Pancakes"))
    breakfast.add(Dish("Waffles"))

    drinks = Menu("Drinks Menu")
    drinks.add(Dish("Coffee"))
    drinks.add(Dish("Orange Juice"))

    full_menu = Menu("Full Menu")
    full_menu.add(breakfast)
    full_menu.add(drinks)

    full_menu.display()