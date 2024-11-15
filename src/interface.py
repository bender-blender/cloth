from abc import ABC, abstractmethod

class Outerwear(ABC):
    """ Интерфейс Верхней одежды

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def view(self) -> str:
        raise NotImplementedError()
    

class Footwear(ABC):
    """Интерфейс обуви

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def view(self) -> str:
        raise NotImplementedError()

class Accessory(ABC):
    """Интерфейс Аксессуара

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def view(self) -> str:
        raise NotImplementedError()
    

class ClothingFactory(ABC):
    """Интерфейс Фабрики Одежды

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def create_outerwear(self) -> Outerwear:
        raise NotImplementedError()
    
    @abstractmethod
    def create_footwear(self) -> Footwear:
        raise NotImplementedError()
    
    @abstractmethod
    def create_accessory(self) -> Accessory:
        raise NotImplementedError()