from models.feature import Feature

class PremiumFeature(Feature):
    def get_surcharge(self):
        return round(super().get_total_cost() * 0.15, 2)

    def get_total_cost(self):
        return self.get_base_cost() + self.get_additional_cost() + self.get_surcharge()

    def get_details(self):
        return f'Base cost: ${self.get_base_cost()}\nAdditional cost: ${self.get_additional_cost()}\n15% surcharge: ${self.get_surcharge()}\nTotal cost: ${self.get_total_cost()}'
