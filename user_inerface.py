import tkinter as tk

from varables import font_stats

class Stats_Window:
    
    """Create the main window for tracking honey supplies"""
    def __init__(self, root):
        """Initilise all of the varables for stats window."""

        # A frame for all content
        self.main_frame = tk.Frame(root, bg = "red", highlightthickness=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Configures rows and columbs
        for i in range(4):
            self.main_frame.columnconfigure(i, weight= 1, uniform="stat_cols", minsize="50px")

        for i in range(2):
            self.main_frame.rowconfigure(i, weight= 1, uniform="stat_rows", minsize="30px")
            
        # All of the content for the main frame
        self.current_honey_supply_label = tk.Label(self.main_frame, text="Honey: 10/100000", font=font_stats, bg="grey")
        self.current_honey_supply_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.current_week_label = tk.Label(self.main_frame, text="Week 0", font=font_stats, bg="yellow")
        self.current_week_label.grid(row=1, column=0, columnspan=2, sticky = "nsew")

        self.new_week_button = tk.Button(self.main_frame, text= "New Week -->", command = self.new_week, font=font_stats, bg="yellow")
        self.new_week_button.grid(row=1, column=2, columnspan=2, sticky = "nsew")
        

    def new_week(self):
        """Update all the values for the next week"""
        pass

class Config_Window:
    """Update & create values for the bees, hives, and apiary"""
    def __init__(self, root):
        """Initilise all of the varables for connfig window."""
        self.nav_bar_frame = tk.Frame()
        self.nav_bar_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.apairy_frame = tk.Frame()
        self.apairy_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")
        
        self.worker_bee_frame = tk.Frame()
        self.worker_bee_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.queen_bee_frame = tk.Frame()
        self.queen_bee_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.footer_frame = tk.Frame()
        self.footer_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")

class Apiary_Window:
    """Create a window for controlling all the hives"""
    def __init__(self, root):
        """Initilise all of the varables for apiary window."""
        self.apairy_setup_frame = tk.Frame()
        self.apairy_setup_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.apairy_config_frame = tk.Frame()
        self.apairy_config_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.enviroment_config_frame = tk.Frame()
        self.enviroment_config_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.active_hives_frame = tk.Frame()
        self.active_hives_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.add_hive_frame = tk.Frame()
        self.add_hive_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.new_week_button = tk.Button(text= "New Week -->", command = self.new_week)
        self.new_week_button.grid(row=0, column=0, columnspan=4, sticky = "nsew")


    def new_week(self):
        """Change values for new week"""
        pass

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
        hive_name_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        hive_energy_label = tk.Label(text="Hive Energy: 0.9")
        hive_energy_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        hive_population_label= tk.Label(text="4320 Bees")
        hive_population_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        forage_frame = tk.Frame()
        forage_frame.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        forage_bee_counter_label = tk.Label(text="Bees foraging 143/ 4320") 
        forage_bee_counter_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        forage_bee_counter_entry = tk.Entry(text="Enter the amount of bees you would like to send to forage")
        forage_bee_counter_entry.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        forage_button = tk.Button(text="Forage", command=self.forage)
        forage_button.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        new_queen_button = tk.Button(text= "This will link to the config tab")
        new_queen_button.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        kill_hive_label = tk.Label(text="Kill Hive")
        kill_hive_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        kill_hive_button = tk.Button(text="Enter", command= self.kill_hive)
        kill_hive_button.grid(row=0, column=0, columnspan=4, sticky = "nsew")

    def forage(self):
        "Send bees out to forage"
        pass
    
    def kill_hive(self):
        "Kill the hive and sell resorces"
        pass

def config_root(parent):
        child_root = tk.Toplevel(parent)
        child_root.grid_columnconfigure(0, weight=1)
        child_root.grid_rowconfigure(0, weight=1)
        return child_root

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Game")
    root.geometry("500x500")
    stat_window = Stats_Window(config_root(root))
    apiary_window = Apiary_Window(config_root(root))

    root.mainloop()