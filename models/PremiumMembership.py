from models.Membership import Membership

class PremiumMembership(Membership):
    
    def __init__(self, cost: float):
        super().__init__(cost)