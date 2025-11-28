from models.Membership import Membership

class FamilyMembership(Membership):
    
    def __init__(self, cost: float):
        super().__init__(cost)