from organism import Organism

class Plant(Organism):
    def __init__(self):
        super().__init__()
        cost = 35
        self.powerup = 0

    def attack(self, nonplant):
        pass
    def apply_powerup(self, card):
        pass
    def weaken_powerup(self):
        pass
