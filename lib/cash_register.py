class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        """Add an item to the cash register with optional quantity."""
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.last_transaction = transaction_amount
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        """Apply discount to total if discount exists and print success message."""
        if self.discount:
            discount_amount = (self.discount * self.total) / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
            return self.total
        else:
            print("There is no discount to apply.")
            return None

    def get_items(self):
        """Return the list of items."""
        return self.items

    def void_last_transaction(self):
        """Remove the last transaction from the total."""
        self.total -= self.last_transaction
        if self.items:
            self.items.pop()
        self.last_transaction = 0