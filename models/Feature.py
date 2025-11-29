from models.Membership import Membership


class Feature(Membership):

    def __init__(self, name: str, cost: float, wrapee: Membership, available: bool = True):
        super().__init__(cost, wrapee.group_size, available)
        self.name = name
        self.wrapee = wrapee

    def getBaseCost(self):
        return self.wrapee.getBaseCost()
    
    def getAdditionalCost(self):
        return self.wrapee.getAdditionalCost() + self.cost
    
    def getTotalCost(self):
        return self.wrapee.getTotalCost() + self.cost