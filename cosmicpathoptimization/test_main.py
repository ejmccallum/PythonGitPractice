import unittest
from main import Main

class TestMain(unittest.TestCase):

    def test_calculate_mean_temperature(self):
        main = Main()

        main.num_readings = 3
        main.temperatures = [300, 310, 280]
        self.assertEqual(main.calculate_mean_temperature(), 296)

        main.num_readings = 4
        main.temperatures = [100, 200, 300, 400]
        self.assertEqual(main.calculate_mean_temperature(), 250)

        main.num_readings = 4
        main.temperatures = [0, 0, 0, 0]
        self.assertEqual(main.calculate_mean_temperature(), 0)

        main.num_readings = 3
        main.temperatures = [37, 37, 37]
        self.assertEqual(main.calculate_mean_temperature(), 37)

        main.num_readings = 5
        main.temperatures = [10, 20, 30, 40, 50]
        self.assertEqual(main.calculate_mean_temperature(), 30)

        main.num_readings = 2
        main.temperatures = [100, 200]
        self.assertEqual(main.calculate_mean_temperature(), 150)

if __name__ == '__main__':
    unittest.main()
