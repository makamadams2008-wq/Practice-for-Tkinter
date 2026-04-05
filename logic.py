

class Apiary:

    def __init__(self, name, location, dificualty):
        self.week_of_year = 0
        self.name = name 
        self.location = location
        self.dificulty = dificualty
        self.hives = []
    
    def new_week(self):
        pass

    def change_conditions(self):
        pass

    def change_copitition(self):
        pass

    def inspect_hive(self):
        pass

    def create_hive(self):
        pass

    def kill_hive(self):
        pass


class Hive:

    def __init__(self, name, population):

        self.name = name
        self. alive = True
        self.population = population 
        self.hive_energy = 1
        self.honey_stocks = 0
        self. honey_capasity = 100

    def forage_for_honey(self):
        pass

    def hibernate(self):
        pass

    def incress_population(self):
        pass

    def harvest_honey(self):
        pass
    
    def create_queen(self):
        pass
