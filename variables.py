import math
import tkinter as tk

location_list = ["Mexico", "China", "Germany", "Kenya", "New Zealand", "Peru"]
locations = {
    "Mexico" : {
        "name" :  "Mexico",
        "temriptiure" : 21,
        "sunlight_hours": 12,
        "wind_intecity": 0.4,
        "necter_flow": 0.7,
        "compitition": 0.6,
    },
    "China" : {
        "name" :  "China",
        "temriptiure" : 15,
        "sunlight_hours": 11,
        "wind_intecity": 0.5,
        "necter_flow": 0.9,
        "compitition": 0.9,
    },
    "Germany" : {
        "name" :  "Germany",
        "temriptiure" : 10,
        "sunlight_hours": 10,
        "wind_intecity": 0.3,
        "necter_flow": 0.6,
        "compitition": 0.7,
    },
    "Kenya" : {
        "name" :  "Kenya",
        "temriptiure" : 25,
        "sunlight_hours": 12,
        "wind_intecity": 0.5,
        "necter_flow": 0.5,
        "compitition": 0.4,
    },
    "New Zealand" : {
        "name" :  "New Zealand",
        "temriptiure" : 13,
        "sunlight_hours": 11,
        "wind_intecity": 0.7,
        "necter_flow": 0.8,
        "compitition": 0.8,
    },
    "Peru" : {
        "name" :  "Peru",
        "temriptiure" : 19,
        "sunlight_hours": 11,
        "wind_intecity": 0.4,
        "necter_flow": 0.7,
        "compitition": 0.5,
    }
}
difficulty_list = ["Beginner", "Easy", "Medium", "Hard", "Insane"]
difiiculty_multipliers = [1.4, 1.2, 1, 0.8, 0.6]

# Tk inter styling 
current_window = "name_contnet_frame"
font_stats = ("Arial", 12, "bold")

background_color_a = "#435457"
background_color_b = "#5E6F72"
background_color_c = "#353D3F"
forground_color = "#FFBB00"
accent_color = "#78ECDD"
boader_color = "#ECECEC"

hive_name = "Untitled Hive"
hive_location = "Mexico" 
difficulty = "Easy"

difficulty_x = difiiculty_multipliers[difficulty_list.index(difficulty)]

bee_population = 100
week = 0
honey = 100
honey_quota = 0
energy_level =  100
bee_health = 10
bee_energy_capacity = 10
bee_speed = 1
bee_honey_capacity = 10

is_alive = True

percent_mod = (math.log(honey/2) ** 1.5 + 100)/100

