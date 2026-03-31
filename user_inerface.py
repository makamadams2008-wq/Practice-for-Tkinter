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
    """Create a window for controlling the different hives"""
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



if __name__ == "__main__":
    root = tk.Tk()
    main_window = Stats_Window(root)
    root.mainloop()