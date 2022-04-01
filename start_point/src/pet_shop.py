# WRITE YOUR FUNCTIONS HERE
# def test_pet_shop_name(self):
#         name = get_pet_shop_name(self.cc_pet_shop)
#         self.assertEqual("Camelot of Pets", name)

from io import BufferedIOBase


def get_pet_shop_name(shop):
    return shop["name"]

# def test_total_cash(self):
#     sum = get_total_cash(self.cc_pet_shop)
#     self.assertEqual(1000, sum)

def get_total_cash(cash):
    return cash["admin"]["total_cash"]

# def test_add_or_remove_cash__add(self):
#         add_or_remove_cash(self.cc_pet_shop,10)
#         cash = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(1010, cash)

def add_or_remove_cash(new_amount,cash):
    new_amount["admin"]["total_cash"] += cash
   
    return new_amount

#  def test_pets_sold(self):
#         sold = get_pets_sold(self.cc_pet_shop)
#         self.assertEqual(0, sold)

def get_pets_sold(sold):
    return sold ["admin"]["pets_sold"]


def increase_pets_sold(new_amount,pets):
    new_amount["admin"]["pets_sold"] += pets
   
    return new_amount

def get_stock_count(pet):
    return len(pet["pets"])

def pets_by_breed(breed,amount):

    list_of_breeds = []

        for breed in breeds: