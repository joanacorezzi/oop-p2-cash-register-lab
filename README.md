
# Cash Register project
## Overview
This project creates a simple `CashRegister` class to practice Object Oriented Programming in Python.  
The class allows you to add items, apply a discount, and void the last transaction.

## Features
- `total` starts at 0  
- `items` is a list of all items added  
- `previous_transactions` stores the dollar amount of each add  
- Supports optional discount (0–100%)

## Methods
### add_item(item, price, quantity=1)
Adds the item(s) to the register, updates the total, and records the transaction amount.

### apply_discount()
Applies the percentage discount to the total.  
Prints the updated total or a message if no discount is set.

### void_last_transaction()
Removes the most recent transaction amount from the total.

## Example
```python
register = CashRegister(20)
register.add_item("apple", 1.00, 3)
register.apply_discount()
register.void_last_transaction()
