from models.Membership import Membership

class Feature(Membership):

    def __init__(self, name: str, cost: float, wrapee: Membership):
        super().__init__(wrapee.name, cost, wrapee.benefits)
        self.wrapee = wrapee

    def getBaseCost(self):
        return self.wrapee.getBaseCost()
    
    def getAdditionalCost(self):
        return self.wrapee.getAdditionalCost() + self.cost
    
    