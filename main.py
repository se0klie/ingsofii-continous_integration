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
    # 1. Definir y construir los planes de membresía con sus beneficios (features)
    basic_plan = BasicMembership(cost=50)
    basic_plan = Feature(name="Access to gym floor", cost=0, wrapee=basic_plan)
    basic_plan = Feature(name="Standard locker room", cost=0, wrapee=basic_plan)

    premium_plan = PremiumMembership(cost=100)
    premium_plan = Feature(name="All Basic benefits", cost=0, wrapee=premium_plan)
    premium_plan = Feature(name="Access to group classes", cost=0, wrapee=premium_plan)
    premium_plan = Feature(name="Sauna and spa access", cost=0, wrapee=premium_plan)

    family_plan = FamilyMembership(cost=250)
    family_plan = Feature(name="All Premium benefits for up to 4 family members", cost=0, wrapee=family_plan)
    family_plan = Feature(name="Childcare services", cost=0, wrapee=family_plan)

    memberships = {
        "1": ("Basic", basic_plan),
        "2": ("Premium", premium_plan),
        "3": ("Family", family_plan)
    }

    while True:
        print("\nWelcome to the Gym Membership Management System!")
        print("Please select a membership plan:")
        for key, (name, plan) in memberships.items():
            print(f"{key}. {name} Membership - ${plan.getTotalCost()}")
            # Nota: Para mostrar beneficios, necesitaríamos una forma de extraerlos del decorador.
            # Por ahora, nos centramos en la selección y el costo.
        
        choice = input("Enter the number of your choice (or 'q' to quit): ")

        if choice.lower() == 'q':
            print("Exiting application. Goodbye!")
            break

        if choice in memberships:
            name, selected_plan = memberships[choice]
            print(f"\nYou have selected the {name} Membership.")
            print(f"Total Cost: ${selected_plan.getTotalCost()}")
            # The next step will be to customize the membership with additional features.
            break # Exiting after selection for now
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()