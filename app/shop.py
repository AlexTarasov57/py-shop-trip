import math

from datetime import datetime
from dataclasses import dataclass
from app.customer import Customer


@dataclass
class Shops:
    name: str
    location: list[int]
    products: dict

    def calculate_trip_distance(self, customer: Customer) -> int | float:
        return math.dist(self.location, customer.location)

    def shopping_cost(self, customer: Customer) -> int | float:
        total = 0
        for keys, value in customer.product_cart.items():
            total += self.products.get(keys) * value
        return total

    def print_check(self, customer: Customer) -> None:
        datatime_now = datetime(2021, 1, 4, 12, 33, 41)
        print(f"\nDate: {datatime_now.strftime("%d/%m/%Y %H:%M:%S")}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:"
              )
        for keys, value in customer.product_cart.items():
            amount = self.products[keys] * value
            print(f"{value} {keys}s for "
                  f"{int(amount) if float(amount) == int(amount) else amount} "
                  f"dollars")
        print(
            f"Total cost is {self.shopping_cost(customer)} dollars\n"
            f"See you again!"
        )
