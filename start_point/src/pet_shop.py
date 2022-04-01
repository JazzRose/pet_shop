# WRITE YOUR FUNCTIONS HERE
# def test_pet_shop_name(self):
#         name = get_pet_shop_name(self.cc_pet_shop)
#         self.assertEqual("Camelot of Pets", name)

from io import BufferedIOBase


def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]


def add_or_remove_cash(new_amount,cash):
    new_amount["admin"]["total_cash"] += cash
   
    return new_amount

def get_pets_sold(sold):
    return sold ["admin"]["pets_sold"]


def increase_pets_sold(new_amount,pets):
    new_amount["admin"]["pets_sold"] += pets
   
    return new_amount

def get_stock_count(pet):
    return len(pet["pets"])

def get_pets_by_breed(pet_shop,breed):
    list_of_pets = []
    pets = pet_shop["pets"]

    for pet in pets:
        if pet ["breed"] == breed:
            list_of_pets.append(pet)
# add item that is being looped
    return list_of_pets

def find_pet_by_name(pet_shop,name):
    pets = pet_shop["pets"]

    for pet in pets:
        if pet["name"] == name:
            return pet
#     list_of_pets_names = []
#     pets = pet_shop["pets"]

#     for pet in pets:
#         if pet ["name"] == name:
#             list_of_pets_names.append(pet)
# # add item that is being looped
#     return list_of_pets_names

