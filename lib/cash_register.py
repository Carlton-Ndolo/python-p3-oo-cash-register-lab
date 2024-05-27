#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return "There is no discount to apply."

        discount_amount = self.total * self.discount / 100
        self.total -= discount_amount
        self.total = round(self.total)
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.get_total_without_last_item()
            self.total = last_item_price
            self.items.pop()
        else:
            print("No items to void.")

    def get_total_without_last_item(self):
        if self.items:
            last_item_price = self.items[-1]
            return self.total - last_item_price
        return 0

    def reset_register_totals(self):
        self.total = 0
        self.items = []

