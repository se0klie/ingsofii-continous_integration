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



def get_base_membership(membership):
    """
    Get the base membership object from the chain.
    """
    current = membership
    while hasattr(current, 'wrapee'):
        current = current.wrapee
    return current

def extract_feature_names(membership):
    """
    Extract all feature names from a membership chain.
    """
    features = []
    current = membership
    while hasattr(current, 'wrapee'):
        if hasattr(current, 'getName'):
            features.append(current.getName())
        current = current.wrapee
    return features

def display_confirmation(membership, membership_name, additional_features):
    """
    Display confirmation screen with all membership details.
    """
    print("\n" + "="*60)
    print("MEMBERSHIP CONFIRMATION")
    print("="*60)
    
    print(f"\nSelected Membership: {membership_name} Membership")
    print(f"Base Cost: ${membership.getBaseCost():.2f}")
    
    # Get built-in features
    all_features = extract_feature_names(membership)
    built_in_features = [f for f in all_features if f not in additional_features]
    
    if built_in_features:
        print(f"\nBuilt-in Features (included):")
        for feature in built_in_features:
            print(f"  - {feature}")
    
    if additional_features:
        print(f"\nAdditional Features:")
        additional_cost = 0.0
        for feature in additional_features:
            print(f"  - {feature.name}")
            additional_cost += feature.cost
        if additional_cost > 0:
            print(f"Additional Features Cost: ${additional_cost:.2f}")
    
    # Check for premium feature surcharge
    surcharge = 0.0
    if isinstance(membership, PremiumFeature):
        surcharge = membership.getSurcharge()
        if surcharge > 0:
            print(f"\nPremium Feature Surcharge (15%): ${surcharge:.2f}")
    
    base_membership = get_base_membership(membership)
    discount_details = base_membership.getDiscountDetails()
    discount_amount = base_membership.getDiscountAmount()
    
    if discount_amount > 0:
        print(f"\nApplied Discounts:")
        for desc in discount_details:
            print(f"  - {desc}")
        print(f"Total Discount: ${discount_amount:.2f}")
    
    final_total = membership.getTotalCost() - discount_amount
    print(f"\n{'='*60}")
    print(f"FINAL TOTAL COST: ${final_total:.2f}")
    print("="*60)
    
    return final_total

def main():
    """
    Main function to run the Gym Membership Management System CLI.
    """
    # 1. Definir y construir los planes de membresía con sus beneficios (features)
    basic_plan_base = BasicMembership(cost=50, available=True)
    basic_plan = Feature(name="Access to gym floor", cost=0, wrapee=basic_plan_base, available=True)
    basic_plan = Feature(name="Standard locker room", cost=0, wrapee=basic_plan, available=True)

    premium_plan_base = PremiumMembership(cost=100, available=True)
    premium_plan = Feature(name="All Basic benefits", cost=0, wrapee=premium_plan_base, available=True)
    premium_plan = Feature(name="Access to group classes", cost=0, wrapee=premium_plan, available=True)
    premium_plan = Feature(name="Sauna and spa access", cost=0, wrapee=premium_plan, available=True)

    family_plan_base = FamilyMembership(cost=250, available=True)
    family_plan = Feature(name="All Premium benefits for up to 4 family members", cost=0, wrapee=family_plan_base, available=True)
    family_plan = Feature(name="Childcare services", cost=0, wrapee=family_plan, available=True)

    memberships = {
        "1": ("Basic", basic_plan, basic_plan_base),
        "2": ("Premium", premium_plan, premium_plan_base),
        "3": ("Family", family_plan, family_plan_base)
    }

    # Additional features available for selection

    additional_features_catalog = {
        "1": Feature(name="Personal training sessions", cost=25.00, wrapee=basic_plan_base, available=True),
        "2": Feature(name="Nutrition consultation", cost=35.00, wrapee=basic_plan_base, available=True),
        "3": Feature(name="Massage therapy", cost=45.00, wrapee=basic_plan_base, available=False),
        "4": PremiumFeature(cost=30.00, name="Specialized program", wrapee=premium_plan_base, available=True),  # Premium feature
        "5": PremiumFeature(cost=40.00, name="Exclusive access", wrapee=premium_plan_base, available=True)  # Premium feature
    }

    selected_membership = None
    selected_membership_name = None
    selected_membership_base = None
    selected_additional_features = []

    # Step 1: Select membership plan with availability validation
    while True:
        print("\n" + "="*60)
        print("Welcome to the Gym Membership Management System!")
        print("="*60)
        print("\nPlease select a membership plan:")
        for key, (name, plan, base) in memberships.items():
            availability_status = "Available" if base.available else "Unavailable"
            print(f"{key}. {name} Membership - ${plan.getTotalCost():.2f} [{availability_status}]")
        
        choice = input("\nEnter the number of your choice (or 'q' to quit): ")

        if choice.lower() == 'q':
            print("Exiting application. Goodbye!")
            return -1

        if choice in memberships:
            name, plan, base = memberships[choice]
            
            #Validate membership availability
            if not base.available:
                print(f"\nERROR: The {name} Membership is currently unavailable.")
                print("Please select an available membership plan from the options below.\n")
                continue
            
            selected_membership = plan
            selected_membership_name = name
            selected_membership_base = base
            print(f"\nYou have selected the {name} Membership.")
            break
        else:
            print("\nInvalid choice, please try again.")

    # Step 2: Select additional features with availability validation
    print("\n" + "="*60)
    print("ADDITIONAL FEATURES")
    print("="*60)
    print("\nWould you like to add additional features?")
    
    # Filter premium features for Premium memberships only
    available_features = {}
    for key, feature_obj in additional_features_catalog.items():
        if isinstance(feature_obj, PremiumFeature):
            # Premium features only for Premium memberships
            if selected_membership_name == "Premium":
                available_features[key] = feature_obj
        else:
            # Regular features for all memberships
            available_features[key] = feature_obj
    
    if available_features:
        def show_feature_options():
            """
            Helper function to display feature options.
            """
            print("\nAvailable features:")
            for key, feature_obj in available_features.items():
                feature_type = " (Premium)" if isinstance(feature_obj, PremiumFeature) else ""
                status = "Available" if feature_obj.available else "Unavailable"
                # Get cost from the feature object
                feature_cost = feature_obj.cost
                feature_name = feature_obj.getName()
                print(f"{key}. {feature_name}{feature_type} - ${feature_cost:.2f} [{status}]")
            print(f"{len(available_features) + 1}. Skip additional features")
        
        show_feature_options()
        
        while True:
            feature_choice = input("\nEnter the number of your choice: ")
            
            if feature_choice == str(len(available_features) + 1):
                break
            
            if feature_choice in available_features:
                feature_obj = available_features[feature_choice]
                feature_name = feature_obj.getName()
                
                # Validate feature availability
                if not feature_obj.available:
                    print(f"\nERROR: The feature '{feature_name}' is currently unavailable.")
                    print("Please select an available feature from the options below.\n")
                    show_feature_options()
                    continue
                
                # Check if it's a premium feature
                is_premium_feature = isinstance(feature_obj, PremiumFeature)
                if is_premium_feature:
                    # Validate that the membership is Premium
                    if not isinstance(selected_membership_base, PremiumMembership):
                        print(f"\nERROR: Premium features can only be added to Premium memberships.")
                        print("Please select an available feature from the options below.\n")
                        show_feature_options()
                        continue
                    
                    # Add premium feature - create new instance wrapping the current membership
                    selected_membership = PremiumFeature(
                        cost=feature_obj.cost,
                        name=feature_name,
                        wrapee=selected_membership,
                        available=feature_obj.available
                    )
                else:
                    # Add regular feature - create new instance wrapping the current membership
                    selected_membership = Feature(
                        name=feature_name,
                        cost=feature_obj.cost,
                        wrapee=selected_membership,
                        available=feature_obj.available
                    )
                
                selected_additional_features.append(selected_membership)
                print(f"\nAdded feature: {selected_membership.name}")
                
                # Ask if user wants to add more features
                add_more = input("Would you like to add another feature? (y/n): ").lower()
                if add_more != 'y':
                    break
                else:
                    # Show options again before asking for next feature
                    print()
                    show_feature_options()
            else:
                print("\nInvalid choice, please try again.")
                show_feature_options()

    # Step 3: Group membership question (for discount calculation)
    print("\n" + "="*60)
    num_members = 1
    try:
        members_input = input("How many members are signing up together? (Enter 1 for individual): ")
        num_members = int(members_input)
        if num_members < 1:
            num_members = 1
        if num_members >= 2:
            print(f"\nGroup membership detected! You'll receive a 10% discount for {num_members} members.")
            # Update group_size in the membership chain
            base = get_base_membership(selected_membership)
            base.group_size = num_members
    except ValueError:
        num_members = 1

    # Step 4: User confirmation
    while True:
        final_cost = display_confirmation(selected_membership, selected_membership_name, 
                                         selected_additional_features)
        print("\nOptions:")
        print("1. Confirm and finalize membership")
        print("2. Cancel and make changes")
        
        confirm_choice = input("\nEnter your choice (1 or 2): ")
        
        if confirm_choice == "1":
            print("\n" + "="*60)
            print("MEMBERSHIP CONFIRMED!")
            print("="*60)
            print(f"\nThank you for choosing {selected_membership_name} Membership!")
            print(f"Your membership has been successfully processed.")
            print(f"Total amount: ${final_cost:.2f}")
            print("\nWelcome to our gym!")
            return int(final_cost)  # Return positive integer
        elif confirm_choice == "2":
            print("\nMembership selection cancelled.")
            return -1  # Return -1 if cancelled
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()