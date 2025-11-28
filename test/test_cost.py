from models import FamilyMembership, Feature, PremiumFeature
from models.Membership import Membership
from models.PremiumMembership import PremiumMembership

def test_base_cost():
    m = Membership(cost=10.0)
    assert m.getBaseCost() == 10.0

def test_total_cost():
    membership = FamilyMembership(cost=10.50)
    membership = Feature(name="Personal training sessions",
                                    cost=4.25,
                                    wrapee=membership)
    membership = Feature(name="Group classes",
                                    cost=7.15,
                                    wrapee=membership)
    assert membership.getTotalCost() == 21.9


def test_total_cost_with_premium_features():
    membership = PremiumMembership(cost=12.50)
    membership = PremiumFeature(name="Specialized program",
                                    cost=5.50,
                                    wrapee=membership)
    membership = PremiumFeature(name="Exclusive access",
                                    cost=8.25,
                                    wrapee=membership)
    assert membership.getTotalCost() == 30.19