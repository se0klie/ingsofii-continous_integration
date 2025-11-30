from models.PremiumMembership import PremiumMembership
from models.Feature import Feature


class PremiumFeature(Feature):

    def __init__(self, cost: float, name: str, wrapee: PremiumMembership, available: bool = True):
        super().__init__(name, cost, wrapee, available)
        
    
    def getAdditionalCost(self):
        return self.wrapee.getAdditionalCost() + self.cost
    
    def getTotalCost(self):
        raw_cost = self.getBaseCost() + self.getAdditionalCost()
        return round(raw_cost * 1.15, 2)

    def getSurcharge(self):
        raw_cost = self.getBaseCost() + self.getAdditionalCost()
        return round(super().getTotalCost() * 0.15, 2)
    

    def getDetails(self):
        return f'Base cost: ${self.getBaseCost()}\nAdditional cost: ${self.getAdditionalCost()}\n15% surcharge: ${self.getSurcharge()}\nTotal cost: ${self.getTotalCost()}'
    