from factories import (
    SportsFactory,
    ClassicFactory,
    Sherlock,
    ClothingFactory
    )

from interface import ClothingFactory
from icecream import ic
def client_code(factory:ClothingFactory):
    
    outerwear = factory.create_outerwear()
    footwear = factory.create_footwear()
    create_accessory = factory.create_accessory()
    ic(outerwear.view())
    ic(footwear.view())
    ic(create_accessory.view())
    print()

client_code(SportsFactory())
client_code(ClassicFactory())
client_code(Sherlock())