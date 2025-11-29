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
        return self.wrapee.getTotalCost()
    
    def isAvailable(self):
        """Check if the feature is available. Feature is available only if itself and the wrapped membership are available."""
        return self.available and self.wrapee.isAvailable()
    
    def getName(self):
        """Get the name of the feature."""
        return self.name
    