from interface import Outerwear,Footwear,Accessory

class Jacket(Outerwear):
    """Куртка

    Args:
        Outerwear (_type_): _description_
    """
    def view(self) -> str:
        return "Куртка"
    
class Blazer(Outerwear):
    """Пиджак

    Args:
        Outerwear (_type_): _description_
    """
    def view(self) -> str:
        return "Пиджак"
    

class Coat(Outerwear):
    """Пальто

    Args:
        Outerwear (_type_): _description_
    """
    def view(self) -> str:
        return "Пальто"
    

class Sneakers(Footwear):
    """Кроссовки

    Args:
        Footwear (_type_): _description_
    """
    def view(self) -> str:
        return "Кроссовки"
    

class Shoes(Footwear):
    """Туфли

    Args:
        Footwear (_type_): _description_
    """
    def view(self) -> str:
        return "Туфли"
    

class AnkleBoots(Footwear):
    """Берцы

    Args:
        Footwear (_type_): _description_
    """

    def view(self) -> str:
        return "Берцы"

class Hooligan(Accessory):
    """Хулиганка

    Args:
        Accessory (_type_): _description_
    """
    def view(self) -> str:
        return "Хулиганка"


class Scarf(Accessory):
    """Шарф

    Args:
        Accessory (_type_): _description_
    """
    def view(self) -> str:
        return "Шарф"
    

class BowTie(Accessory):
    """Галстук бабочка

    Args:
        Accessory (_type_): _description_
    """
    def view(self) -> str:
        return "Галстук"
    