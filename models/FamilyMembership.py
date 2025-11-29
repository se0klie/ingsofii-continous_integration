from models.Membership import Membership


class FamilyMembership(Membership):
    
    def __init__(self, cost: float, group_size: int = 1):
        super().__init__(cost, group_size)
