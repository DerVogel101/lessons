class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price == other.price and self.name == other.name

    def __ne__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return not self.price == other.price and other.name == self.name

    def __lt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price < other.price and self.name < other.name

    def __le__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price <= other.price and self.name <= other.name

    def __gt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price > other.price and self.name > other.name

    def __ge__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price >= other.price and self.name >= other.name

    def __repr__(self):
        return f'{self.name}: {self.price}'

if __name__ == "__main__":
    item1 = Item('Apple', 1)
    item2 = Item('Apple', 1)
    item3 = Item('Banana', 2)
    print(item1 == item2)  # Output: True
    print(item1 == item3)  # Output: False
    print(item1 != item2)  # Output: False
    print(item1 != item3)  # Output: True
    print(item1 < item3)  # Output: True
    print(item1 <= item3)  # Output: True
    print(item1 > item3)  # Output: False
    print(item1 >= item3)  # Output: False
    print(item1 >= item2)  # Output: True
    print(item1 <= item2)  # Output: True
    print(item1 > item2)  # Output: False
    print(item1 < item2)  # Output: False

