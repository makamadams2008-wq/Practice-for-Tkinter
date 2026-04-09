"""A local file for all of the variables."""

location_list = ["Mexico", "China", "Germany", "Kenya", "New Zealand", "Peru"]
LOCATIONS = {
    "Mexico": {
        "name": "Mexico",
        "temperature": 21,
        "sunlight_hours": 12,
        "wind_intensity": 0.4,
        "nectar_flow": 0.7,
        "competition": 0.6,
    },
    "China": {
        "name": "China",
        "temperature": 15,
        "sunlight_hours": 11,
        "wind_intensity": 0.5,
        "nectar_flow": 0.9,
        "competition": 0.9,
    },
    "Germany": {
        "name": "Germany",
        "temperature": 10,
        "sunlight_hours": 10,
        "wind_intensity": 0.3,
        "nectar_flow": 0.6,
        "competition": 0.7,
    },
    "Kenya": {
        "name": "Kenya",
        "temperature": 25,
        "sunlight_hours": 12,
        "wind_intensity": 0.5,
        "nectar_flow": 0.5,
        "competition": 0.4,
    },
    "New Zealand": {
        "name": "New Zealand",
        "temperature": 13,
        "sunlight_hours": 11,
        "wind_intensity": 0.7,
        "nectar_flow": 0.8,
        "competition": 0.8,
    },
    "Peru": {
        "name": "Peru",
        "temperature": 19,
        "sunlight_hours": 11,
        "wind_intensity": 0.4,
        "nectar_flow": 0.7,
        "competition": 0.5,
    }
}
difficulty_list = ["Beginner", "Easy", "Medium", "Hard", "Insane"]
difficulty_multipliers = [1.4, 1.2, 1, 0.8, 0.6]
# Tkinter styling
current_window = "name_content_frame"
FONT_STATS = ("Arial", 12, "bold")
BACKGROUND_COLOR_A = "#FBF6C6"
BACKGROUND_COLOR_B = "#FEFCEC"
BACKGROUND_COLOR_C = "#FFEAD3"
FORGROUND_COLOR = "#000000"
ACCENT_COLOR = "#FD9D6D"

hive_name = "Untitled Hive"
hive_location = "Mexico"
difficulty = "Easy"
difficulty_x = difficulty_multipliers[difficulty_list.index(difficulty)]

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

ALL_ATTRIBUTES = [
    "bee_health",
    "bee_energy_capacity",
    "bee_speed",
    "bee_honey_capacity"
    ]
