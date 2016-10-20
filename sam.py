
class Sam():

    def __init__(self):
        self.soccer_ability = 0
        self.coding_ability = 0
        self.softball_ability = 0
        self.stamina = 100
        self.happiness = 50

    def play_soccer(self, value):
        self.soccer_ability += value
        self.stamina -= 5
        self.happiness += 2

    def code(self, value):
        self.coding_ability += value
        self.stamina -= 2
        self.happiness -= 1

    def play_softball(self, value):
        self.softball_ability += value
        self.stamina -= 3
        self.happiness += 2

    def run(self, time):
        if time >= 3:
            self.stamina -= 6
        else:
            self.stamina -= 3
        self.happiness += 1

    def sleep(self, time):
        if time <= 7:
            self.stamina += 10
            self.happiness += 3
        else:
            self.stamina += 15
            self.happiness += 6

    def eat(self, value):
        self.stamina += value
