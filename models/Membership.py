class Membership:

    def __init__(self, name: str, cost: float, benefits: list[str]):
        self.name = name
        self.cost = cost
        self.benefits = benefits

    def getBaseCost(self):
        return self.cost

    def getAdditionalCost(self):
        return 0

    def getTotalCost(self):
        return self.getBaseCost() + self.getAdditionalCost()

    def getDetails(self):
        return f'Benefits: {", ".join(self.benefits)}\nBase cost: ${self.getBaseCost()}'