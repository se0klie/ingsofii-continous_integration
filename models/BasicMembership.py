from models.Membership import Membership

class BasicMembership(Membership):
    
    def __init__(self, cost: float = 50.0):
        benefits = ["Access to gym floor", "Standard locker room"]
        super().__init__("Basic", cost, benefits)