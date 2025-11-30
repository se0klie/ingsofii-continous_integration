class Membership:
    def __init__(self, cost: float, group_size: int = 1, available: bool = True):
        self.cost = cost
        self.group_size = group_size
        self.available = available

    def getBaseCost(self):
        return self.cost

    def getAdditionalCost(self):
        return 0

    def getTotalBeforeDiscount(self):
        return self.getBaseCost() + self.getAdditionalCost()

    def getDiscountAmount(self):
        total = self.getTotalBeforeDiscount()
        discount = 0.0

        if self.group_size >= 2:
            discount += total * 0.10

        temp_total = total - discount
        if temp_total > 400:
            discount += 50
        elif temp_total > 200:
            discount += 20

        return discount

    def getDiscountDetails(self):
        details = []
        total = self.getTotalBeforeDiscount()

        if self.group_size >= 2:
            group_discount = total * 0.10
            details.append(f"Group membership discount ({self.group_size} members): 10% (${group_discount:.2f})")

        temp_total = total - (total * 0.10 if self.group_size >= 2 else 0)
        if temp_total > 400:
            details.append("Special offer discount (>$400): $50.00")
        elif temp_total > 200:
            details.append("Special offer discount (>$200): $20.00")

        return details

    def getTotalCost(self):
        """
        Get total cost after applying all discounts.
        """
        total = self.getTotalBeforeDiscount()
        discount = self.getDiscountAmount()

        if self.group_size >= 2:
            group_discount = total * 0.10
            print(f"*** You are saving ${group_discount:.2f} by signing up {self.group_size} members together! ***")

        return total - discount

    def isAvailable(self):
        return self.available

    def setAvailable(self, available: bool):
        self.available = available

    def getDetails(self):
        return f'Base cost: ${self.getBaseCost()}\nAdditional cost: ${self.getAdditionalCost()}\nTotal cost: ${self.getTotalCost()}'