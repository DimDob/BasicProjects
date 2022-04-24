from tests.pet_shop import PetShop

import unittest


class TestPetShop(unittest.TestCase):
    obj = PetShop('MaxiPet')

    def test_init(self):
        name = 'Doggy'
        self.assertEqual(name, 'Doggy')
        self.obj.food = {}
        self.assertEqual(self.obj.food, {})
        self.obj.pets = []
        self.assertEqual([], self.obj.pets)

    def test_if_add_food_works_properly(self):
        for quantity in [0,-5]:
            with self.assertRaises(Exception) as ex:
                self.obj.add_food(self.obj.name, quantity)
            self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_if_name_not_in_food(self):
        name = 'Beef'
        boolean = name not in self.obj.food
        self.assertFalse(boolean)

        self.obj.food[name] = 0
        self.assertEqual(self.obj.food[name], 0)

    def test_if_name_in_food(self):
        name = 'Beef' # of food
        quantity = 1
        self.obj.food = {'Beef':0}
        self.obj.food[name] += quantity
        self.assertEqual(self.obj.food[name], 1)

        expected = f"Successfully added {quantity:.2f} grams of {name}."
        self.assertEqual(expected, f"Successfully added {1:.2f} grams of Beef.")

    def test_if_add_pet_name_not_in_pets(self):
        pet_name = 'Doggy'
        self.obj.pets = []
        boolean = pet_name not in self.obj.pets
        self.assertTrue(boolean)

        self.obj.pets.append(pet_name)
        self.assertEqual(self.obj.pets, ['Doggy'])
        expected = f"Successfully added {pet_name}."
        self.assertEqual(expected, f"Successfully added Doggy.")


    def test_if_add_pet_name_in_pets(self):
        pet_name = 'Doggy'
        self.obj.pets.append(pet_name)

        self.assertEqual(True, pet_name in self.obj.pets)
        with self.assertRaises(Exception) as ex:
            self.obj.add_pet(pet_name)
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))


    def test_feed_pet_if_invalid_food(self):
        pet_name = 'Doggy'
        self.obj.pets = []
        with self.assertRaises(Exception) as ex:
            self.obj.feed_pet('Banana', pet_name)
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_if_food_not_in_foods(self):

        food = "Banana"
        self.obj.food = []

        self.assertTrue(food, self.obj.food)
        expected = 'You do not have Banana'
        self.assertEqual(expected, f"You do not have {food}")



    def test_feed_pet_if_food_quantity_less_than_100(self):
        self.obj.food = {}
        self.obj.food['Carrot'] = 10
        expected = f'Successfully added 1000.00 grams of Carrot.'
        result = self.obj.add_food('Carrot', 1000.00)

        self.assertEqual(expected,result)

    def test_prop_minus_100(self):
        self.obj.pets = ['Doggy']
        self.obj.food = {'Banana': 110}
        pet_name = 'Doggy'
        self.obj.feed_pet('Banana', pet_name)
        self.assertEqual(f'{pet_name} was successfully fed', 'Doggy was successfully fed')
        self.assertEqual(10, self.obj.food['Banana'])



    def test_if_repr_prop(self):
        self.obj.pets = ['Doggy', 'Catty']
        expected = f'Shop {self.obj.name}:\n' \
               f'Pets: {", ".join(self.obj.pets)}'

        result =  f'Shop MaxiPet:\n' \
               f'Pets: Doggy, Catty'

        self.assertEqual(expected,result)





if __name__ == '__main__':
    unittest.main()
