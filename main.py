from models.PremiumFeature import PremiumFeature
from models.Feature import Feature
from models.BasicMembership import BasicMembership
from models.PremiumMembership import PremiumMembership
from models.FamilyMembership import FamilyMembership

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



def main():
    """
    Main function to run the Gym Membership Management System CLI.
    """
    memberships = {
        "1": BasicMembership(),
        "2": PremiumMembership(),
        "3": FamilyMembership()
    }

    while True:
        print("\nWelcome to the Gym Membership Management System!")
        print("Please select a membership plan:")
        for key, membership in memberships.items():
            print(f"{key}. {membership.name} Membership - ${membership.getBaseCost()}")
            print(f"   Benefits: {', '.join(membership.benefits)}")
        
        choice = input("Enter the number of your choice (or 'q' to quit): ")

        if choice.lower() == 'q':
            print("Exiting application. Goodbye!")
            break
        
        if choice in memberships:
            selected_membership = memberships[choice]
            print(f"\nYou have selected the {selected_membership.name} Membership.")
            print(selected_membership.getDetails())
            # The next step will be to customize the membership with additional features.
            break # Exiting after selection for now
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()