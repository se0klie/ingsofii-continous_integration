from models.Membership import Membership

class PremiumMembership(Membership):
    
    def __init__(self, cost: float, group_size: int = 1, available: bool = True):
        super().__init__(cost, group_size, available)
