from models.membership import Membership


class Feature(Membership):

    def __init__(self, name: str, cost: float, wrapee: Membership, available: bool = True):
        super().__init__(cost, wrapee.group_size, available)
        self.name = name
        self.wrapee = wrapee

    def get_base_cost(self):
        return self.wrapee.get_base_cost()

    def get_additional_cost(self):
        return self.wrapee.get_additional_cost() + self.cost

    def get_total_cost(self):
        return self.get_base_cost() + self.get_additional_cost()

    def is_available(self):
        return self.available and self.wrapee.is_available()

    def get_name(self):
        return self.name
