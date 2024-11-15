
from product import (
    AnkleBoots,
    Scarf,
    Shoes,
    Sneakers,
    BowTie,
    Hooligan,
    Jacket,
    Coat,
    Blazer,
    
)

from interface import Accessory, ClothingFactory, Footwear, Outerwear


class SportsFactory(ClothingFactory):
    """Фабрика Спортивного стиля

    Args:
        ClothingFactory (_type_): _description_
    """
    def create_outerwear(self) -> Outerwear:
        return Jacket()

    def create_footwear(self) -> Footwear:
        return Sneakers()
    
    def create_accessory(self) -> Accessory:
        return Hooligan()

class ClassicFactory(ClothingFactory):
    """Фабрика Классики

    Args:
        ClothingFactory (_type_): _description_
    """
    def create_outerwear(self) -> Outerwear:
        return Blazer()

    def create_footwear(self) -> Footwear:
        return Shoes()
    
    def create_accessory(self) -> Accessory:
        return BowTie()
    

class Sherlock(ClothingFactory):
    """ Фабрика "Шерлока"

    Args:
        ClothingFactory (_type_): _description_
    """

    def create_outerwear(self) -> Outerwear:
        return Coat()

    def create_footwear(self) -> Footwear:
        return AnkleBoots()
    
    def create_accessory(self) -> Accessory:
        return Scarf()