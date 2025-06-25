# strategy_pattern/strategy.py
class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError()


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))

    def checkout(self, strategy: PaymentStrategy):
        total = sum(price for _, price in self.items)
        strategy.pay(total)


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Book", 10)
    cart.add_item("Pen", 2)

    print("Using Credit Card:")
    cart.checkout(CreditCardPayment())

    print("\nUsing PayPal:")
    cart.checkout(PayPalPayment())