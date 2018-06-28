from organism import Organism

class Non_Plant(Organism):
    def __init__(self):
        super().__init__()
        worth = 20
        self.hp = 80
        self.dmg = 5

    def attack(self, plant):
        pass
