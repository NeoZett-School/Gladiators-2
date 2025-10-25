from Data import Data, dataclass

items = Data(source="items")

print(items)

@dataclass
class Item(Data, source="items"):
    id: int
    name: str
    price: float

item1 = Item(id=1, name="Sword", price=100.0)
print(item1.config)