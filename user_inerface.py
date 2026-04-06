import tkinter as tk

import varables

class Stats_Window:
    
    """Create the main window for tracking honey supplies"""
    def __init__(self, parent):
        """Initilise all of the varables for stats window."""

        #configs the main frame
        self.container_frame = config_frame(parent, 4, 2, True, 0, 0, True)

        # All of the content for the main frame
        self.current_honey_supply_label = tk.Label(self.container_frame, text="Honey: 10/100000", font=varables.font_stats, bg=varables.background_color_c, fg = varables.forground_color)
        self.current_honey_supply_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.current_week_label = tk.Label(self.container_frame, text="Week 0", font=varables.font_stats, bg = varables.background_color_b, fg = varables.forground_color)
        self.current_week_label.grid(row=1, column=0, columnspan=2, sticky = "nsew")

        self.new_week_button = tk.Button(self.container_frame, text= "New Week -->", command = self.new_week, font=varables.font_stats, bg=varables.background_color_b, fg = varables.forground_color)
        self.new_week_button.grid(row=1, column=2, columnspan=2, sticky = "nsew")

        self.current_week_label = tk.Label(self.container_frame, text="Week 5", font=varables.font_stats, bg=varables.background_color_c, fg = varables.forground_color)
        self.current_week_label.grid(row=2, column=0, columnspan=4, sticky = "nsew")
        

    def new_week(self):
        """Update all the values for the next week"""
        pass

class Setup_Window:
    """Create the main window"""
    def __init__(self, parent):
        """Initilise all of the varables for apiary window."""

        #configs the main frame
        self.container_frame = config_frame(parent, 1, 3, True, 0, 0, False)

        # Nav frame 
        self.nav_frame = config_frame(self.container_frame, 4, 1, True, 0, 0, True)

        self.nav_label = tk.Label(self.nav_frame, text="Makams Hive", font=varables.font_stats, bg=varables.background_color_b, fg = varables.forground_color)
        self.nav_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        # Name  frame 
        self.setup_contnet_frame = config_frame(self.container_frame, 4, 3, False, 1, 0, True)
        
        self.name_label = tk.Label(self.setup_contnet_frame, text="Please Pick A Hive Name", font=varables.font_stats, bg=varables.background_color_c, fg = varables.forground_color)
        self.name_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.enter_here_label = tk.Label(self.setup_contnet_frame, text="Enter Here:", font=varables.font_stats, bg=varables.background_color_c, fg = varables.forground_color)
        self.enter_here_label.grid(row=1, column=0, columnspan=2, sticky = "nsew")

        self.name_entry = tk.Entry(self.setup_contnet_frame, font=varables.font_stats, bg=varables.background_color_c, fg = varables.forground_color)
        self.name_entry.grid(row=1, column=2, columnspan=2, sticky = "nsew")

        self.name_confirmation_button = tk.Button(self.setup_contnet_frame, text="Confirm Name", font=varables.font_stats, bg=varables.background_color_c, fg = varables.forground_color)
        self.name_confirmation_button.grid(row=2, column=0, columnspan=4, sticky = "nsew")

        # Difficulty  frame 
        self.difficulty_contnet_frame = config_frame(self.container_frame, 4, 3, True, 1, 0, True)

        self.name_label = tk.Label(self.difficulty_contnet_frame, text="Please Pick A Starter Location", font=varables.font_stats, bg=varables.background_color_c, fg = varables.forground_color)
        self.name_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        # Footer frame 
        self.footer_frame = config_frame(self.container_frame, 4, 1, True, 2, 0, True)

        self.name_confirmation_button = tk.Button(self.footer_frame, text="Next Page -->", font=varables.font_stats, bg=varables.background_color_b, fg = varables.forground_color)
        self.name_confirmation_button.grid(row=0, column=0, columnspan=4, sticky = "nsew")


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


def config_root(parent):
        child_root = tk.Toplevel(parent)
        child_root.grid_columnconfigure(0, weight=1)
        child_root.grid_rowconfigure(0, weight=1)
        return child_root

def config_frame(parent, cols, rows, visability, row_pos, col_pos, adaptive):

    """Configure the frames"""
    # A frame for all content
    frame = tk.Frame(parent, bg = varables.background_color_a, highlightthickness=0)
    if(visability == True):
        frame.grid(row=row_pos, column=col_pos, sticky="nsew")
    
    # Configures rows and columbs differently depending if adaptive = True
    if adaptive == True:
        for i in range(cols):
            frame.columnconfigure(i, weight= 1, uniform="stat_cols", minsize="50px")

        for i in range(rows):
            frame.rowconfigure(i, weight= 1, uniform="stat_rows", minsize="30px")

    else:
        for i in range(cols):
            frame.columnconfigure(i, weight= 1, minsize="50px")

        for i in range(rows):
            frame.rowconfigure(i, weight= 1, minsize="30px")
     
    return frame


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Game")
    main_window = Setup_Window(config_root(root))
    stat_window = Stats_Window(config_root(root))
    

    root.mainloop()