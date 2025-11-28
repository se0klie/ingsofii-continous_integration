from models.Membership import Membership

class FamilyMembership(Membership):
    
    def __init__(self, cost: float = 250.0):
        benefits = ["All Premium benefits for up to 4 family members", "Childcare services"]
        super().__init__("Family", cost, benefits)