import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self) -> None:
        self.train = Train('Train1', 2)

    def test_init(self):
        train = Train('Train1', 5)
        self.assertEqual('Train1', train.name)
        self.assertEqual(5, train.capacity)
        self.assertEqual(train.passengers, [])


    def test_add_method_if_len_passengers_eq_capacity(self):
        self.train.passengers = ['Kaloyan', 'Asen']
        self.assertEqual(self.train.TRAIN_FULL, "Train is full")

        with self.assertRaises(ValueError) as ex:
            self.train.add('Ivan')

        self.assertEqual("Train is full", str(ex.exception))
        self.assertEqual(True, 'Ivan' not in self.train.passengers)


    def test_add_method_if_passenger_name_is_in_passengers(self):
        self.train.passengers = ['Ivan']

        with self.assertRaises(ValueError) as ex:
            self.train.add('Ivan')
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual(True, 'Ivan' in self.train.passengers)
        self.assertEqual("Passenger Ivan Exists", str(ex.exception))

    def test_add_method_if_everything_is_properly_working(self):
        self.train.passengers = ['Ivan']
        result = self.train.add('Asen')
        self.assertEqual(True, 'Asen' in self.train.passengers)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Added passenger Asen", result)

    def test_remove_if_passenger_name_is_not_in_passengers(self):
        self.train.passengers = ['Ivan']

        with self.assertRaises(ValueError) as ex:
            self.train.remove('Asen')
        self.assertEqual(True, 'Asen' not in self.train.passengers)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_is_passenger_is_on_board(self):
        self.train.passengers = ['Ivan', 'Asen']
        self.assertEqual(True, 'Ivan' in self.train.passengers)
        result = self.train.remove('Ivan')
        self.assertEqual(True, 'Ivan' not in self.train.passengers)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual('Removed Ivan', result)