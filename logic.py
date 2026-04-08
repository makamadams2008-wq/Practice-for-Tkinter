import variables
import random
class Hive:

    def __init__(self):
        self.workers = Workers()
        self.name = variables.hive_name
        self.alive = True
        self.hive_energy = variables.energy_level
        self.honey_stocks = variables.is_alive
        self.quota = variables.honey_quota

        # Equations
        self.location_survivle_rate_expo = 1- (variables.locations[variables.hive_location]["compitition"])**(2 -variables.locations[variables.hive_location]["wind_intecity"] - ((variables.locations[variables.hive_location]["sunlight_hours"] + variables.locations[variables.hive_location]["sunlight_hours"])/27))
        self.honey_harvest_expo = variables.locations[variables.hive_location]["necter_flow"]**0.5

    def forage_for_honey(self):
        self.workers.count*((0.3 + variables.difficulty_x/2)**self.location_survivle_rate_expo)
        self.honey_stocks+=self.workers.count*self.workers.honey_capacity**(self.honey_harvest_expo)
        self.new_week()

    def hibernate(self):
        self.hive_energy = 100
        self.new_week()


    def incress_population(self):
        self.workers.count += random(0.4, 0.6)
        self.new_week()
    
    def level_up(self):
        self.workers.level_up()
        self.new_week()

    def update_dashboard(self):
        pass

    def new_week(self):
        self.update_dashboard()
        pass

class Workers:

    def ___init__(self):

        self.health = variables.bee_health
        self.count = variables.bee_population
        self.energy_capasity = variables.bee_energy_capacity
        self.speed = variables.bee_speed
        self.honey_capacity =variables.bee_honey_capacity

    
    def level_up(self):
        pass
