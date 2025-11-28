from models.PremiumMembership import PremiumMembership
from models.FamilyMembership import FamilyMembership
from models.PremiumFeature import PremiumFeature
from models.Feature import Feature

membership1 = PremiumMembership(cost=12.50)
membership1 = PremiumFeature(name="Specialized program",
                                  cost=5.50,
                                  wrapee=membership1)
membership1 = PremiumFeature(name="Exclusive access",
                                  cost=8.25,
                                  wrapee=membership1)

membership2 = FamilyMembership(cost=10.50)
membership2 = Feature(name="Personal training sessions",
                                  cost=4.25,
                                  wrapee=membership2)
membership2 = Feature(name="Group classes",
                                  cost=7.15,
                                  wrapee=membership2)



print(f'Membership 1: Premium\n{membership1.getDetails()}\n')

print(f'Membership 2: Family\n{membership2.getDetails()}\n')