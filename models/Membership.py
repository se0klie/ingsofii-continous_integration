class Membership:

    def __init__(self, cost: float):
        self.cost = cost

    def getBaseCost(self):
        return self.cost

    def getAdditionalCost(self):
        return 0
    
    def getTotalCost(self):
        return self.getBaseCost() + self.getAdditionalCost()
    
    def getDetails(self):
        return f'Base cost: ${self.getBaseCost()}\nAdditional cost: ${self.getAdditionalCost()}\nTotal cost: ${self.getTotalCost()}'