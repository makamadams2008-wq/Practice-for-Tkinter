import tkinter as tk

from tkinter import messagebox

import variables

class Stats_Window:
    
    """Create the main window for tracking honey supplies"""
    def __init__(self, parent):
        """Initilise all of the variables for stats window."""

        # Allows me to destroy window latter
        self.parent = parent

        #configs the main frame
        self.container_frame = config_frame(parent, 4, 2, True, 0, 0, True)

        # All of the content for the main frame

        # Honey
        self.honey_required_label = tk.Label(self.container_frame, text="Main Stats", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.honey_required_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.current_honey_supply_label = tk.Label(self.container_frame, text=f"Honey Required This Week: {variables.honey}/{variables.honey_quota}", font=variables.font_stats, bg=variables.background_color_c, fg = variables.forground_color)
        self.current_honey_supply_label.grid(row=1, column=0, columnspan=4, sticky = "nsew")
        # Week
        self.current_week_label = tk.Label(self.container_frame, text=f"Week {variables.week}", font=variables.font_stats, bg = variables.background_color_c, fg = variables.forground_color)
        self.current_week_label.grid(row=2, column=0, columnspan=4, sticky = "nsew")

        # Energy
        self.current_energy_label = tk.Label(self.container_frame, text=f"Energy: {variables.energy_level}%", font=variables.font_stats, bg=variables.background_color_c, fg = variables.forground_color)
        self.current_energy_label.grid(row=3, column=0, columnspan=4, sticky = "nsew")

        self.hive_stats_label = tk.Label(self.container_frame, text="Other Stats", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.hive_stats_label.grid(row=4, column=0, columnspan=4, sticky = "nsew")

        self.hive_stats_difficulty_label = tk.Label(self.container_frame, text=f"Difficualty: {variables.difficulty.get()}", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.hive_stats_difficulty_label.grid(row=5, column=0, columnspan=4, sticky = "nsew")

        self.hive_stats_enviroment_label = tk.Label(self.container_frame, text=f"Enviroment: {variables.hive_location.get()}", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.hive_stats_enviroment_label.grid(row=6, column=0, columnspan=4, sticky = "nsew")

        #bees 

        self.current_bee_stats_label = tk.Label(self.container_frame, text=f"Bee Stats", font=variables.font_stats, bg=variables.background_color_c, fg = variables.forground_color)
        self.current_bee_stats_label.grid(row=7, column=0, columnspan=4, sticky = "nsew")

        self.hive_population_label = tk.Label(self.container_frame, text=f"Population: {variables.bee_population}", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.hive_population_label.grid(row=8, column=0, columnspan=4, sticky = "nsew")

        self.bee_heath_label = tk.Label(self.container_frame, text=f"Bee Health: {variables.bee_health}", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.hive_stats_difficulty_label.grid(row=9, column=0, columnspan=4, sticky = "nsew")

        self.hive_energy_capasity_label = tk.Label(self.container_frame, text=f"Energy Capasity: {variables.bee_energy_capacity}", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.hive_energy_capasity_label.grid(row=10, column=0, columnspan=4, sticky = "nsew")

        self.bee_speed_label = tk.Label(self.container_frame, text=f"Bee Speed: {variables.bee_speed}", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.bee_speed_label.grid(row=11, column=0, columnspan=4, sticky = "nsew")

        self.bee_honey_capasity_label = tk.Label(self.container_frame, text=f"Bee Honey Capasity: {variables.bee_honey_capacity}", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.bee_honey_capasity_label.grid(row=12, column=0, columnspan=4, sticky = "nsew")
        
        
        

    def new_week(self):
        """Update all the values for the next week"""
        pass

class Setup_Window:
    """Create the main window"""
    def __init__(self, parent):
        """Initilise all of the variables for apiary window."""

        # Allows me to destroy window latter
        self.parent = parent

        #configs the main frame
        self.container_frame = config_frame(parent, 1, 3, True, 0, 0, False)

        # Nav frame 
        self.nav_frame = config_frame(self.container_frame, 4, 1, True, 0, 0, True)

        self.nav_label = tk.Label(self.nav_frame, text=variables.hive_name, font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.nav_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        # Name  frame 
        self.name_contnet_frame = config_frame(self.container_frame, 4, 3, True, 1, 0, True)
        
        self.name_entry = createEntry(self.name_contnet_frame, "Please pick a name", lambda: self.update_name() )

        # Starter location frame 
        self.starter_location_contnet_frame = config_frame(self.container_frame, 4, 7, False, 1, 0, True)

        variables.hive_location = self.starter_location_radio = createRadio(self.starter_location_contnet_frame, variables.location_list, "Please Pick A Starter Location", None)

        # Difficaulty frame 
        self.difficaulty_contnet_frame = config_frame(self.container_frame, 4, 6, False, 1, 0, True)

        variables.difficulty = self.difficualty_radio = createRadio(self.difficaulty_contnet_frame, variables.difficulty_list, "Please Pick A Difficulty", None)

        # Footer frame 
        self.footer_frame = config_frame(self.container_frame, 4, 1, True, 2, 0, True)

        self.name_confirmation_button = tk.Button(self.footer_frame, text="Next Page -->", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color, command =self.next_page)
        self.name_confirmation_button.grid(row=0, column=0, columnspan=4, sticky = "nsew")

    def next_page(self):
        if variables.current_window == "name_contnet_frame":  
            self.name_contnet_frame.grid_forget()
            self.starter_location_contnet_frame.grid(row=1, column=0, sticky="nsew")
            variables.current_window = "starter_location_contnet_frame"

        elif variables.current_window == "starter_location_contnet_frame":
            self.starter_location_contnet_frame.grid_forget()
            self.difficaulty_contnet_frame.grid(row=1, column=0, sticky="nsew")
            variables.current_window = "difficaulty_contnet_frame"
        
        else:
            self.parent.destroy()
            main_window.parent.deiconify()
            stat_window.parent.deiconify()
            
    
    def update_name(self):
        variables.hive_name = self.name_entry.get()
        self.nav_label.config(text=variables.hive_name)

class Hive_window:
    """Create a window for controlling individual hives"""
    def __init__(self, parent):

        # Allows me to destroy window latter
        self.parent = parent

        #configs the main frame
        self.container_frame = config_frame(parent, 1, 2, True, 0, 0, False)

        # Nav frame 
        self.nav_frame = config_frame(self.container_frame, 4, 2, True, 0, 0, True)

        self.nav_label = tk.Label(self.nav_frame, text= variables.hive_name, font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.nav_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.action_label = tk.Label(self.nav_frame, text= "Actions", font=variables.font_stats, bg=variables.background_color_c, fg = variables.forground_color)
        self.action_label.grid(row=1, column=0, columnspan=4, sticky = "nsew")

        # Actions frame 

        self.content_frame = config_frame(self.container_frame, 4, 5, True, 1, 0, True)

        self.hybernate_action_button = tk.Button(self.content_frame, text="Hybernate", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color, command =self.hybernate)
        self.hybernate_action_button.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.exspand_hive_action_button = tk.Button(self.content_frame, text="Incresse Population", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color, command = self.exspand_hive)
        self.exspand_hive_action_button.grid(row=1, column=0, columnspan=4, sticky = "nsew")

        self.forage_action_button = tk.Button(self.content_frame, text="Forage For Honey", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color, command =self.forage_for_honey)
        self.forage_action_button.grid(row=2, column=0, columnspan=4, sticky = "nsew")

        self.level_up_action_button = tk.Button(self.content_frame, text="Level Up Bees", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color, command =self.level_up_bees)
        self.level_up_action_button.grid(row=3, column=0, columnspan=4, sticky = "nsew")

        self.give_up_action_button = tk.Button(self.content_frame, text="Give up", font=variables.font_stats, bg=variables.accent_color, fg = variables.forground_color, command =self.give_up)
        self.give_up_action_button.grid(row=4, column=0, columnspan=4, sticky = "nsew")


    def hybernate(self):
        messagebox.showinfo("Hybernating", "Your hive bees are currently hybernating, this is restoring there energy levels and starting a new week")

    def exspand_hive(self):
        self.exspand_widow =Exspand_Hive(config_root(self.parent))
        self.parent.withdraw()

    def forage_for_honey(self):
        messagebox.askyesno("Send bees out to forage", "Are you sure you want to send your bees out to forage?")
        #next week
        messagebox.showinfo("Back from foraging", "Your bees have arived back from foraging where they found 12000 honey")

        pass
    def level_up_bees(self):
        messagebox.askyesno("Level up bees", "are you sure you want to level up your bees by 10 percent for 100 honey?")

    def give_up(self):
        messagebox.askyesno("Giving up already?", "Are you sure you want to give up?")

    
    def kill_hive(self):
        "Kill the hive and sell resorces"
        pass

class Exspand_Hive:

    def __init__(self, parent):

        # Allows me to destroy window latter
        self.parent = parent

        self.add_bee_count = 0
        #configs the main frame
        self.container_frame = config_frame(parent, 4, 3, True, 0, 0, False)

        self.nav_label = tk.Label(self.container_frame, text= "Incress Population", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.nav_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.count_label = tk.Label(self.container_frame, text= f"Plus {self.add_bee_count} Bees For {self.add_bee_count*5} Honey", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color)
        self.count_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        self.minus_bees = tk.Button(self.container_frame, text="- 100 bees", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color, command =self.minus_from_bees)
        self.minus_bees.grid(row=1, column=0, columnspan=2, sticky = "nsew")

        self.add_bees = tk.Button(self.container_frame, text="+ 100 bees", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color, command =self.add_to_bees)
        self.add_bees.grid(row=1, column=2, columnspan=2, sticky = "nsew")

        self.conffirmation_button = tk.Button(self.container_frame, text="Conffirm", font=variables.font_stats, bg=variables.background_color_b, fg = variables.forground_color, command =self.adapt_total)
        self.conffirmation_button.grid(row=2, column=0, columnspan=4, sticky = "nsew")


    def add_to_bees(self):
        self.add_bee_count += 100
        self.count_label.config(text=f"Plus {self.add_bee_count} Bees For {self.add_bee_count*5} Honey")
    def minus_from_bees(self):
        self.add_bee_count -= 100
        self.count_label.config(text=f"Plus {self.add_bee_count} Bees For {self.add_bee_count*5} Honey")
    
    def adapt_total(self):
        variables.bee_population += self.add_bee_count
        self.parent.destroy()
        main_window.parent.deiconify()

        



def config_root(parent):
        child_root = tk.Toplevel(parent)
        child_root.grid_columnconfigure(0, weight=1)
        child_root.grid_rowconfigure(0, weight=1)
        return child_root

def config_frame(parent, cols, rows, visability, row_pos, col_pos, adaptive):

    """Configure the frames"""
    # A frame for all content
    frame = tk.Frame(parent, bg = variables.background_color_a, highlightthickness=0)
    if(visability == True):
        frame.grid(row=row_pos, column=col_pos, sticky="nsew")
    
    # Configures rows and columbs differently depending if adaptive = True
    if adaptive == True:
        for i in range(cols):
            frame.columnconfigure(i, weight= 1, uniform="stat_cols", minsize=50)

        for i in range(rows):
            frame.rowconfigure(i, weight= 1, uniform="stat_rows", minsize=20)

    else:
        for i in range(cols):
            frame.columnconfigure(i, weight= 1, minsize=50)

        for i in range(rows):
            frame.rowconfigure(i, weight= 1, minsize=20)
     
    return frame

def createEntry(parent, message, func):
        label = tk.Label(parent, text=message, font=variables.font_stats, bg=variables.background_color_c, fg = variables.forground_color)
        label.grid(row=0, column=0, columnspan=4, sticky = "nsew")

        enter_here_label = tk.Label(parent, text="Enter Here:", font=variables.font_stats, bg=variables.background_color_c, fg = variables.forground_color)
        enter_here_label.grid(row=1, column=0, columnspan=2, sticky = "nsew")

        entry = tk.Entry(parent, font=variables.font_stats, bg=variables.background_color_c, fg = variables.forground_color)
        entry.grid(row=1, column=2, columnspan=2, sticky = "nsew")

        confirmation_button = tk.Button(parent, text="Confirm", font=variables.font_stats, bg=variables.background_color_c, fg = variables.forground_color, command=func)
        confirmation_button.grid(row=2, column=0, columnspan=4, sticky = "nsew")

        return entry

def createRadio(parent, my_list, message, func):
        # Lable
        my_label = tk.Label(parent, text= message, font=variables.font_stats, bg=variables.background_color_c, fg = variables.forground_color)
        my_label.grid(row=0, column=0, columnspan=4, sticky = "nsew")
        
        # Setup
        list_variable = tk.StringVar()
        list_variable.set(str(my_list[0]))
        radios = []
        # Creating Radials
        for i, item in enumerate(my_list):
            newRadio = tk.Radiobutton(parent, text = str(item), variable = list_variable, value=item, command=func, font=variables.font_stats, bg=variables.background_color_c, fg = variables.forground_color, selectcolor = variables.background_color_b)
            newRadio.grid(row=i+1, column=0, columnspan= 6, sticky="sew")
            radios.append(newRadio)
        # Returns the instance verable
        return list_variable


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Game")
    root.withdraw()

    setup_window = Setup_Window(config_root(root))

    stat_window = Stats_Window(config_root(root))
    stat_window.parent.withdraw()

    main_window = Hive_window(config_root(root))
    main_window.parent.withdraw()

    root.mainloop()