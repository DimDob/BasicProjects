from project.pet_shop import PetShop
import unittest


class TestPetShop(unittest.TestCase):
    def setUp(self) -> None:
        self.petshop = PetShop('MaxiPet')

    def test_init(self):
        name = 'MaxiPet'
        petshop = PetShop(name)
        self.assertEqual(name, petshop.name)
        self.assertEqual({}, petshop.food)
        self.assertEqual(petshop.pets, [])

    def test_add_food_if_quantity_equal_or_zero_raises(self):
        for quantity in [0,-50]:
            with self.assertRaises(ValueError) as ex:
                self.petshop.add_food('banana', quantity)

            self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_if_food_name_not_in_food(self):
        food_name = 'Banana'
        quantity = 1
        self.assertTrue(food_name not in self.petshop.food)
        result = self.petshop.add_food(food_name, quantity)
        self.assertEqual(self.petshop.food, {'Banana':1})
        self.assertEqual(self.petshop.food[food_name], quantity)
        self.assertEqual(f'Successfully added {quantity:.2f} grams of {food_name}.', result)

    def test_add_pet_if_pet_name_not_in_pets(self):
        pet_name = 'pet1'
        self.assertTrue(pet_name not in self.petshop.pets)
        self.assertEqual(self.petshop.pets, [])
        result = self.petshop.add_pet(pet_name)
        self.assertTrue(pet_name in self.petshop.pets)
        self.assertEqual(result, f"Successfully added {pet_name}." )

    def test_add_pet_if_pet_name_is_in_pets(self):
        self.petshop.pets = ['pet1', 'pet2']
        with self.assertRaises(Exception) as ex:
            self.petshop.add_pet('pet1')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_if_pet_name_not_in_pets_raises(self):
        self.petshop.pets = ['pet1', 'pet2']
        with self.assertRaises(Exception) as ex:
            self.petshop.feed_pet('Banana', 'pet3')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_if_food_name_not_in_food(self):
        food_name = 'Banana'
        self.petshop.pets = ['pet1', 'pet2']
        self.assertTrue(food_name not in self.petshop.food)
        result = self.petshop.feed_pet(food_name, 'pet1')
        self.assertEqual(result, f'You do not have {food_name}')

    def test_feed_pet_if_quantity_of_food_is_less_than_hundred(self):
        self.petshop.food['Banana'] = 50
        self.petshop.pets = ['pet1', 'pet2']
        result = self.petshop.feed_pet('Banana', 'pet1')
        self.assertEqual(1050, self.petshop.food['Banana'])
        self.assertEqual("Adding food...", result)

    def test_feed_pet_if_quantity_of_food_is_higher_than_hundred(self):
        self.petshop.food['Banana'] = 150
        self.petshop.pets = ['pet1', 'pet2']
        result = self.petshop.feed_pet('Banana', 'pet1')
        self.assertEqual(50, self.petshop.food['Banana'])
        self.assertEqual(f"pet1 was successfully fed", result)

    def test_repr(self):
        self.petshop.pets = ['pet1', 'pet2']
        result = repr(self.petshop)
        expected = f'Shop MaxiPet:\n' \
               f'Pets: pet1, pet2'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
