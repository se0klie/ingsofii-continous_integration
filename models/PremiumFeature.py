from models.PremiumMembership import PremiumMembership
from models.Feature import Feature


class PremiumFeature(Feature):

    def __init__(self, cost: float, name: str, wrapee: PremiumMembership):
        super().__init__(name, cost, wrapee)
        
    
    def getAdditionalCost(self):
        base_additional = super().getAdditionalCost()
        surcharge = round((self.wrapee.getBaseCost() + base_additional) * 0.15, 2)
        return base_additional + surcharge - self.cost
    
    def getTotalCost(self):
        return self.wrapee.getTotalCost()

    def getSurcharge(self):
        return round(super().getTotalCost() * 0.15, 2)
    

    def getDetails(self):
        return f'Base cost: ${self.getBaseCost()}\nAdditional cost: ${self.getAdditionalCost()}\n15% surcharge: ${self.getSurcharge()}\nTotal cost: ${self.getTotalCost()}'
