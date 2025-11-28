from models.Membership import Membership

class PremiumMembership(Membership):
    
    def __init__(self, cost: float = 100.0):
        benefits = ["All Basic benefits", "Access to group classes", "Sauna and spa access"]
        super().__init__("Premium", cost, benefits)