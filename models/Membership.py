class Membership:

    def __init__(self, cost: float, group_size: int = 1):
        self.cost = cost
        self.group_size = group_size

    def getBaseCost(self):
        return self.cost

    def getAdditionalCost(self):
        return 0
    
    def getTotalCost(self):
        total = self.getBaseCost() + self.getAdditionalCost()
        
        # Apply group discount (10% if 2 or more members)
        if self.group_size >= 2:
            group_discount = total * 0.10
            total -= group_discount
            print(f"*** You are saving ${group_discount:.2f} by signing up {self.group_size} members together! ***")
        
        # Apply special offer discounts
        if total > 400:
            total -= 50
        elif total > 200:
            total -= 20
            
        return total
    
    def getDetails(self):
        return f'Base cost: ${self.getBaseCost()}\nAdditional cost: ${self.getAdditionalCost()}\nTotal cost: ${self.getTotalCost()}'