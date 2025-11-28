from models.PremiumMembership import PremiumMembership
from models.Feature import Feature

class PremiumFeature(Feature):

    def __init__(self, cost: float, name: str, wrapee: PremiumMembership):
        super().__init__(name, cost, wrapee)
        
    
    def getTotalCost(self):
        return super().getTotalCost() + self.getSurcharge()
    

    def getSurcharge(self):
        return round(super().getTotalCost() * 0.15, 2)
    

    def getDetails(self):
        return f'Base cost: ${self.getBaseCost()}\nAdditional cost: ${self.getAdditionalCost()}\n15% surcharge: ${self.getSurcharge()}\nTotal cost: ${self.getTotalCost()}'
    