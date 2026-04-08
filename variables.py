"""A local file for all of the verables."""

location_list = ["Mexico", "China", "Germany", "Kenya", "New Zealand", "Peru"]
LOCATIONS = {
    "Mexico": {
        "name": "Mexico",
        "temriptiure": 21,
        "sunlight_hours": 12,
        "wind_intecity": 0.4,
        "necter_flow": 0.7,
        "compitition": 0.6,
    },
    "China": {
        "name": "China",
        "temriptiure": 15,
        "sunlight_hours": 11,
        "wind_intecity": 0.5,
        "necter_flow": 0.9,
        "compitition": 0.9,
    },
    "Germany": {
        "name": "Germany",
        "temriptiure": 10,
        "sunlight_hours": 10,
        "wind_intecity": 0.3,
        "necter_flow": 0.6,
        "compitition": 0.7,
    },
    "Kenya": {
        "name": "Kenya",
        "temriptiure": 25,
        "sunlight_hours": 12,
        "wind_intecity": 0.5,
        "necter_flow": 0.5,
        "compitition": 0.4,
    },
    "New Zealand": {
        "name": "New Zealand",
        "temriptiure": 13,
        "sunlight_hours": 11,
        "wind_intecity": 0.7,
        "necter_flow": 0.8,
        "compitition": 0.8,
    },
    "Peru": {
        "name": "Peru",
        "temriptiure": 19,
        "sunlight_hours": 11,
        "wind_intecity": 0.4,
        "necter_flow": 0.7,
        "compitition": 0.5,
    }
}
difficulty_list = ["Beginner", "Easy", "Medium", "Hard", "Insane"]
difiiculty_multipliers = [1.4, 1.2, 1, 0.8, 0.6]
# Tkinter styling
current_window = "name_contnet_frame"
FONT_STATS = ("Arial", 12, "bold")
BACKGROUND_COLOR_A = "#FBF6C6"
BACKGROUND_COLOR_B = "#FEFCEC"
BACKGROUND_COLOR_C = "#FFEAD3"
FORGROUND_COLOR = "#000000"
ACCENT_COLOR = "#FD9D6D"

hive_name = "Untitled Hive"
hive_location = "Mexico"
difficulty = "Easy"
difficulty_x = difiiculty_multipliers[difficulty_list.index(difficulty)]

# Bee stats
bee_population = 100
week = 0
honey = 100
energy_level = 100
bee_health = 10
bee_energy_capacity = 10
bee_speed = 10
bee_honey_capacity = 10
is_alive = True
wasp_tax = 50

ALL_ATRUBUTES = [
    "bee_health",
    "bee_energy_capacity",
    "bee_speed",
    "bee_honey_capacity"
    ]
