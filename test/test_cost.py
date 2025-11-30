from models.familiy_membership import FamilyMembership
from models.feature import Feature
from models.premium_feature import PremiumFeature
from models.membership import Membership
from models.premium_membership import PremiumMembership

def test_base_cost():
    m = Membership(cost=10.0)
    assert m.get_base_cost() == 10.0

def test_total_cost():
    membership = FamilyMembership(cost=10.50)
    membership = Feature(name="Personal training sessions",
                                    cost=4.25,
                                    wrapee=membership)
    membership = Feature(name="Group classes",
                                    cost=7.15,
                                    wrapee=membership)
    assert membership.get_total_cost() == 21.9

def test_total_cost_with_premium_features():
    membership = PremiumMembership(cost=12.50)
    membership = PremiumFeature(name="Specialized program",
                                    cost=5.50,
                                    wrapee=membership)
    membership = PremiumFeature(name="Exclusive access",
                                    cost=8.25,
                                    wrapee=membership)
    assert membership.get_total_cost() == 30.19
