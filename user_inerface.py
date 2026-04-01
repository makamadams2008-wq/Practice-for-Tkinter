import tkinter as tk

class Stats_Window:
    """Create the main window for tracking honey supplies"""
    def __init__(self, root):
        """Initilise all of the varables for stats window."""
        self.current_honey_supply_label = tk.Label(text="Honey: 10/100000")
        self.current_honey_supply_label.pack()

        self.current_week_label = tk.Label(text="Week 0")
        self.current_week_label.pack()

        self.new_week_button = tk.Button(text= "New Week -->", command = self.new_week)
        self.new_week_button.pack()

    def new_week(self):
        """Update all the values for the next week"""
        pass

class Config_Window:
    """Update & create values for the bees, hives, and apiary"""
    def __init__(self, root):
        """Initilise all of the varables for connfig window."""
        self.nav_bar_frame = tk.Frame()
        self.nav_bar_frame.pack()

        self.apairy_frame = tk.Frame()
        self.apairy_frame.pack()
        
        self.worker_bee_frame = tk.Frame()
        self.worker_bee_frame.pack()

        self.queen_bee_frame = tk.Frame()
        self.queen_bee_frame.pack()

        self.footer_frame = tk.Frame()
        self.footer_frame.pack()

class Apiary_Window:
    """Create a window for controlling all the hives"""
    def __init__(self, root):
        """Initilise all of the varables for apiary window."""
        self.apairy_setup_frame = tk.Frame()
        self.apairy_setup_frame.pack()

        self.apairy_config_frame = tk.Frame()
        self.apairy_config_frame.pack()

        self.enviroment_config_frame = tk.Frame()
        self.enviroment_config_frame.pack()

        self.active_hives_frame = tk.Frame()
        self.active_hives_frame.pack()

        self.add_hive_frame = tk.Frame()
        self.add_hive_frame.pack()

        self.new_week_button = tk.Button(text= "New Week -->", command = self.new_week)
        self.new_week_button.pack()

    def apiary_config(self):
        """Configure the apairy"""
        pass

    def initial_setup(self):
        """Initilise the apairy"""
        pass

    def config_enviroment(self):
        """Configure the enviroment"""
        pass

    def add_hive(self):
        """Add a new hive to the apiary"""
        pass

class Hive_window:
    """Create a window for controlling individual hives"""
    def __init__(self, root):
        """Initilise all of the varables for hive window."""
        hive_name_label = tk.Label(text="Hive Name")
        hive_name_label.pack()

        hive_energy_label = tk.Label(text="Hive Energy: 0.9")
        hive_energy_label.pack()

        hive_population_label= tk.Label(text="4320 Bees")
        hive_population_label.pack()

        forage_frame = tk.Frame()
        forage_frame.pack()

        forage_bee_counter_label = tk.Label(text="Bees foraging 143/ 4320") 
        forage_bee_counter_label.pack()

        forage_bee_counter_entry = tk.Entry(text="Enter the amount of bees you would like to send to forage")
        forage_bee_counter_entry.pack()

        forage_button = tk.Button(text="Forage", command=self.forage)
        forage_button.pack()

        new_queen_button = tk.Button(text= "This will link to the config tab")
        new_queen_button.pack()

        kill_hive_label = tk.Label(text="Kill Hive")
        kill_hive_label.pack()

        kill_hive_button = tk.Button(text="Enter", command= self.kill_hive)
        kill_hive_button.pack()

    def forage(self):
        "Send bees out to forage"
        pass
    
    def kill_hive(self):
        "Kill the hive and sell resorces"
        pass


if __name__ == "__main__":
    root = tk.Tk()
    main_window = Stats_Window(root)
    root.mainloop()