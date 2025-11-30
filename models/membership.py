class Membership:
    def __init__(self, cost: float, group_size: int = 1, available: bool = True):
        self.cost = cost
        self.group_size = group_size
        self.available = available

    def get_base_cost(self):
        return self.cost

    def get_additional_cost(self):
        return 0

    def get_total_before_discount(self):
        return self.get_base_cost() + self.get_additional_cost()

    def get_discount_amount(self):
        total = self.get_total_before_discount()
        discount = 0.0

        if self.group_size >= 2:
            discount += total * 0.10

        temp_total = total - discount
        if temp_total > 400:
            discount += 50
        elif temp_total > 200:
            discount += 20

        return discount

    def get_discount_details(self):
        details = []
        total = self.get_total_before_discount()

        if self.group_size >= 2:
            group_discount = total * 0.10
            details.append(f"Group membership discount ({self.group_size} members): 10% (${group_discount:.2f})")

        temp_total = total - (total * 0.10 if self.group_size >= 2 else 0)
        if temp_total > 400:
            details.append("Special offer discount (>$400): $50.00")
        elif temp_total > 200:
            details.append("Special offer discount (>$200): $20.00")

        return details

    def get_total_cost(self):
        """
        Get total cost after applying all discounts.
        """
        total = self.get_total_before_discount()
        discount = self.get_discount_amount()

        if self.group_size >= 2:
            group_discount = total * 0.10
            print(f"*** You are saving ${group_discount:.2f} by signing up {self.group_size} members together! ***")

        return total - discount

    def is_available(self):
        return self.available

    def set_available(self, available: bool):
        self.available = available

    def get_details(self):
        return f'Base cost: ${self.get_base_cost()}\nAdditional cost: ${self.get_additional_cost()}\nTotal cost: ${self.get_total_cost()}'
