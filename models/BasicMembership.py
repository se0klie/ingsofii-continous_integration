from models.Membership import Membership

class BasicMembership(Membership):
    
    def __init__(self, cost: float):
        super().__init__(cost)