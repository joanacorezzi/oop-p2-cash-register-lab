#!/usr/bin/env python3

class CashRegister:
      def __init__(self, discount=0):
        # Initialize discount, total, items, and previous_transactions
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

        @property
        def discount(self):
          return self._discount

        @discount.setter
        def discount(self, value):
        # Discount must be int 0–100
            if isinstance(value, int) and 0 <= value <= 100:
              self._discount = value
            else:
             print("Not valid discount")
            self._discount = 0

      def add_item(self, item, price, quantity=1):
        # Increase total by price * quantity
        added_total = price * quantity
        self.total += added_total

        # Add item name for each quantity
        for _ in range(quantity):
            self.items.append(item)

        # Store the amount added as a transaction
        self.previous_transactions.append(added_total)

      def apply_discount(self):
        # No discount?
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate discount percentage
        discount_amount = self.total * (self.discount / 100)
        self.total = self.total - discount_amount

        # Print updated total (tests expect this)
        print(f"After the discount, the total comes to ${self.total:.0f}.")

      def void_last_transaction(self):
        # If no transaction, nothing to void
        if not self.previous_transactions:
            print("No transactions to void.")
            return

        # Remove last transaction from total
        last = self.previous_transactions.pop()
        self.total -= last