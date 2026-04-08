import variables
import random
class Hive:

    def __init__(self):

        # Equations
        self.location_survivle_rate_expo = 1- (variables.locations[variables.hive_location]["compitition"])**(2 -variables.locations[variables.hive_location]["wind_intecity"] - ((variables.locations[variables.hive_location]["sunlight_hours"] + variables.locations[variables.hive_location]["sunlight_hours"])/27))
        self.honey_harvest_expo = variables.locations[variables.hive_location]["necter_flow"]**0.5

    def forage_for_honey(self):
        bees_before = variables.bee_population
        variables.bee_population *= ((0.3 + variables.difficulty_x/2)**self.location_survivle_rate_expo)
        honey_found = variables.bee_population*variables.bee_honey_capacity**(self.honey_harvest_expo)
        variables.honey += honey_found
        self.new_week()
        bees_dead  = bees_before - variables.bee_population
        return honey_found, bees_dead

    def hibernate(self):
        variables.energy_level = 100
        self.new_week()

    def incress_population(self):
        population_incresse = round(random.uniform(0.4, 0.6)*variables.bee_population, 2)
        variables.bee_population += population_incresse
        self.new_week()
        return population_incresse
    
    def level_up(self):
        random_atrubute = random.choice(variables.all_atrubutes)
        curent_value = getattr(variables, random_atrubute)
        boost = (round(variables.percent_mod, 4))
        new_value = curent_value * boost
        setattr(variables, random_atrubute, new_value)
        self.new_week()
        return random_atrubute, new_value

    def new_week(self):
        variables.week += 1


game_hive = Hive()