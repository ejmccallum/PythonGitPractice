__author__ = "Ethan McCallum"
__course__ = "CSCI 310"
__date__ = "October 22th, 2023"

"""
Cosmic Optimization Kattis Problem Solution
"""

from typing import List


class Main:
    def __init__(self) -> None:
        self.num_readings: int = 0
        self.temperatures: List[int] = []

    def get_input(self) -> None:
        """
        Gets the input from stdin
        """
        self.num_readings = int(input())
        self.temperatures = list(map(int, input().split()))

    def calculate_mean_temperature(self) -> int:
        return sum(self.temperatures) // self.num_readings

    @staticmethod
    def main() -> None:
        main = Main()
        main.get_input()
        print(main.calculate_mean_temperature())


if __name__ == "__main__":
    Main.main()
