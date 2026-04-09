"""This file is the backend of the app."""

import variables
import random
import math


class Hive:
    """Responsible for managing game state."""

    def __init__(self):
        """Form equations for the scaling."""
        self.location_survival_rate_expo = 1 - (variables.LOCATIONS[variables.hive_location]["competition"]) ** (2 - variables.LOCATIONS[variables.hive_location]["wind_intensity"] - ((variables.LOCATIONS[variables.hive_location]["sunlight_hours"] + variables.LOCATIONS[variables.hive_location]["sunlight_hours"]) / 27))
        self.honey_harvest_expo = variables.LOCATIONS[variables.hive_location]["nectar_flow"] ** 0.5

    def forage_for_honey(self):
        """Adjust the values when foraging."""
        bees_before = variables.bee_population
        variables.bee_population *= ((0.3 + (variables.difficulty_x + 1) ** 3 * variables.bee_health * variables.bee_speed / (4000 * ((variables.week+1) ** 0.5))) ** self.location_survival_rate_expo)
        variables.bee_population = round(variables.bee_population)
        honey_found = round(variables.bee_population*variables.bee_honey_capacity ** (self.honey_harvest_expo)) * variables.bee_energy_capacity/10
        variables.honey += honey_found
        state = self.new_week()
        bees_dead = bees_before - variables.bee_population
        variables.energy_level -= 30
        return honey_found, bees_dead, state

    def hibernate(self):
        """Act on hibernate button."""
        variables.energy_level = 100
        state = self.new_week()
        return state

    def increase_population(self):
        """Act on population button."""
        variables.energy_level -= 20
        state = self.new_week()
        return state

    def level_up(self):
        """Act on level up button."""
        random_attribute = random.choice(variables.ALL_ATTRIBUTES)
        current_value = getattr(variables, random_attribute)
        boost = (round((math.log((variables.honey+2.1)/2) ** 1.5 + 100)/100, 2))
        new_value = round(current_value * boost, 2)
        setattr(variables, random_attribute, new_value)
        variables.honey *= 0.5
        state = self.new_week()
        return random_attribute, new_value, state

    def new_week(self):
        """Initiate on a new week."""
        variables.honey -= variables.wasp_tax
        if variables.honey < 0:
            return f"You got stung by the wasp tax, you survived {variables.week} weeks, good game"
        if variables.bee_population <= 0:
            return f"All your bees are dead which is really hard to do, you survived {variables.week} weeks, good game"
        variables.wasp_tax = round(variables.wasp_tax ** (1.05 ** (2 - variables.difficulty_x)))
        variables.week += 1
        return "continue"


game_hive = Hive()
