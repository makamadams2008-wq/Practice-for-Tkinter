"""Responsible for the front end."""

import tkinter as tk
from tkinter import messagebox
import contents.variables as variables
import contents.logic as logic
import math


class StatsWindow:
    """Create the main window for tracking honey supplies."""

    def __init__(self, parent):
        """Initate all of the variables for stats window."""
        # Allows me to destroy window later
        self.parent = parent

        # Configs the main frame
        self.container_frame = config_frame(parent, 4, 2, True, 0, 0, True)

        # All of the content for the main frame

        # Honey
        self.honey_required_label = tk.Label(self.container_frame, text="Main Stats", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_A, fg=variables.FORGROUND_COLOR)
        self.honey_required_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.current_honey_supply_label = tk.Label(self.container_frame, text=f"Honey Required This Week: {variables.honey}/{variables.wasp_tax}", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_C, fg=variables.FORGROUND_COLOR)
        self.current_honey_supply_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # Week
        self.current_week_label = tk.Label(self.container_frame, text=f"Week {variables.week}", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_C, fg=variables.FORGROUND_COLOR)
        self.current_week_label.grid(row=2, column=0, columnspan=4, sticky="nsew")

        # Energy
        self.current_energy_label = tk.Label(self.container_frame, text=f"Energy: {variables.energy_level}%", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_C, fg=variables.FORGROUND_COLOR)
        self.current_energy_label.grid(row=3, column=0, columnspan=4, sticky="nsew")

        self.hive_stats_label = tk.Label(self.container_frame, text="Other Stats", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_A, fg=variables.FORGROUND_COLOR)
        self.hive_stats_label.grid(row=4, column=0, columnspan=4, sticky="nsew")

        self.hive_stats_difficulty_label = tk.Label(self.container_frame, text=f"Difficulty: {variables.difficulty.get()}", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR)
        self.hive_stats_difficulty_label.grid(row=5, column=0, columnspan=4, sticky="nsew")

        self.hive_stats_environment_label = tk.Label(self.container_frame, text=f"Environment: {variables.hive_location.get()}", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR)
        self.hive_stats_environment_label.grid(row=6, column=0, columnspan=4, sticky="nsew")

        # Bees
        self.current_bee_stats_label = tk.Label(self.container_frame, text=f"Bee Stats", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_A, fg=variables.FORGROUND_COLOR)
        self.current_bee_stats_label.grid(row=7, column=0, columnspan=4, sticky="nsew")

        self.hive_population_label = tk.Label(self.container_frame, text=f"Population: {variables.bee_population}", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR)
        self.hive_population_label.grid(row=8, column=0, columnspan=4, sticky="nsew")

        self.bee_health_label = tk.Label(self.container_frame, text=f"Bee Health: {variables.bee_health}", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR)
        self.bee_health_label.grid(row=9, column=0, columnspan=4, sticky="nsew")

        self.hive_energy_capacity_label = tk.Label(self.container_frame, text=f"Energy capacity: {variables.bee_energy_capacity}", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR)
        self.hive_energy_capacity_label.grid(row=10, column=0, columnspan=4, sticky="nsew")

        self.bee_speed_label = tk.Label(self.container_frame, text=f"Bee Speed: {variables.bee_speed}", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR)
        self.bee_speed_label.grid(row=11, column=0, columnspan=4, sticky="nsew")

        self.bee_honey_capacity_label = tk.Label(self.container_frame, text=f"Bee Honey capacity: {variables.bee_honey_capacity}", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR)
        self.bee_honey_capacity_label.grid(row=12, column=0, columnspan=4, sticky="nsew")


class SetupWindow:
    """Create the main window."""

    def __init__(self, parent):
        """Initate all of the variables for apiary window."""
        # Allows me to destroy window later
        self.parent = parent

        # Configs the main frame
        self.container_frame = config_frame(parent, 1, 3, True, 0, 0, False)

        # Nav frame
        self.nav_frame = config_frame(self.container_frame, 4, 1, True, 0, 0, True)
        self.nav_label = tk.Label(self.nav_frame, text=variables.hive_name, font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR)
        self.nav_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Name  frame
        self.name_content_frame = config_frame(self.container_frame, 4, 3, True, 1, 0, True)
        self.name_entry = create_entry(self.name_content_frame, "Please pick a name", self.update_name)

        # Starter location frame
        self.starter_location_content_frame = config_frame(self.container_frame, 4, 7, False, 1, 0, True)
        variables.hive_location = self.starter_location_radio = create_radio(self.starter_location_content_frame, variables.location_list, "Please Pick A Starter Location", None)

        # Difficaulty frame
        self.difficulty_content_frame = config_frame(self.container_frame, 4, 6, False, 1, 0, True)
        variables.difficulty = self.Difficulty_radio = create_radio(self.difficulty_content_frame, variables.difficulty_list, "Please Pick A Difficulty", None)

        # Footer frame
        self.footer_frame = config_frame(self.container_frame, 4, 1, True, 2, 0, True)
        self.name_confirmation_button = tk.Button(self.footer_frame, text="Next Page -->", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR, command=self.next_page)
        self.name_confirmation_button.grid(row=0, column=0, columnspan=4, sticky="nsew")

    def next_page(self):
        """Change the page."""
        if variables.current_window == "name_content_frame":
            if variables.hive_name == "Untitled Hive" or variables.hive_name == "":
                messagebox.showerror("No change detected", f"Please pick a name and then click confirm!")
                return
            main_window.nav_label.config(text=variables.hive_name)
            self.name_content_frame.grid_forget()
            self.starter_location_content_frame.grid(row=1, column=0, sticky="nsew")
            variables.current_window = "starter_location_content_frame"

        elif variables.current_window == "starter_location_content_frame":
            self.starter_location_content_frame.grid_forget()
            self.difficulty_content_frame.grid(row=1, column=0, sticky="nsew")
            variables.current_window = "difficulty_content_frame"

        else:
            self.parent.destroy()
            main_window.parent.deiconify()
            stat_window.parent.deiconify()

    def update_name(self):
        """Update hive name on main_window."""
        variables.hive_name = self.name_entry.get()
        self.nav_label.config(text=variables.hive_name)


class HiveWindow:
    """Create a window for controlling individual hives."""
    
    def __init__(self, parent):
        """Initate all tk elements."""
        # Allows me to destroy window later
        self.parent = parent

        # Configs the main frame
        self.container_frame = config_frame(parent, 1, 2, True, 0, 0, False)

        # Nav frame
        self.nav_frame = config_frame(self.container_frame, 4, 2, True, 0, 0, True)

        self.nav_label = tk.Label(self.nav_frame, text=variables.hive_name, font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_A, fg=variables.FORGROUND_COLOR)
        self.nav_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.action_label = tk.Label(self.nav_frame, text="Actions", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_C, fg=variables.FORGROUND_COLOR)
        self.action_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # Actions frame

        self.content_frame = config_frame(self.container_frame, 4, 5, True, 1, 0, True)

        self.hibernate_action_button = tk.Button(self.content_frame, text="Hibernate", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR, command=self.hibernate)
        self.hibernate_action_button.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.expand_hive_action_button = tk.Button(self.content_frame, text="Increase Population", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR, command=self.expand_hive)
        self.expand_hive_action_button.grid(row=1, column=0, columnspan=4, sticky="nsew")

        self.forage_action_button = tk.Button(self.content_frame, text="Forage For Honey", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR, command=self.forage_for_honey)
        self.forage_action_button.grid(row=2, column=0, columnspan=4, sticky="nsew")

        self.level_up_action_button = tk.Button(self.content_frame, text="Level Up Bees", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR, command=self.level_up_bees)
        self.level_up_action_button.grid(row=3, column=0, columnspan=4, sticky="nsew")

        self.give_up_action_button = tk.Button(self.content_frame, text="Give up", font=variables.FONT_STATS, bg=variables.ACCENT_COLOR, fg=variables.FORGROUND_COLOR, command=self.give_up)
        self.give_up_action_button.grid(row=4, column=0, columnspan=4, sticky="nsew")

    def config_all(self):
        """Update the UI elements."""
        self.LABELS_TO_CONFIG = [stat_window.current_honey_supply_label, stat_window.current_week_label, stat_window.current_energy_label, stat_window.hive_population_label, stat_window.bee_health_label, stat_window.hive_energy_capacity_label, stat_window.bee_speed_label, stat_window.bee_honey_capacity_label]
        self.config_values_to = [f"Honey Required This Week: {variables.honey}/{variables.wasp_tax}", f"Week {variables.week}", f"Energy: {variables.energy_level}%", f"Population: {variables.bee_population}", f"Bee Health: {variables.bee_health}", f"Energy capacity: {variables.bee_energy_capacity}", f"Bee Speed: {variables.bee_speed}", f"Bee Honey capacity: {variables.bee_honey_capacity}"]
        for i in range(len(self.LABELS_TO_CONFIG)):
            self.LABELS_TO_CONFIG[i].config(text=self.config_values_to[i])

    def hibernate(self):
        """Activate when user clicks hibernate button."""
        messagebox.showinfo("Hibernating", "Your hive bees are currently hibernating, this is restoring their energy levels and starting a new week")
        state = logic.game_hive.hibernate()
        check_condition(state)
        self.config_all()

    def expand_hive(self):
        """Activate when user clicks increase population button."""
        if variables.energy_level >= 20:
            self.parent.attributes("-disabled", True)
            self.expand_widow = ExpandHive(config_root(self.parent))
        else:
            messagebox.showerror("Not enough energy", f"Sorry you dont have the required 20 energy for that try hibernating to restore it?")

    def forage_for_honey(self):
        """Activate when user clicks forage button."""
        answer = messagebox.askyesno("Send bees out to forage", "Are you sure you want to send your bees out to forage?")
        if answer:
            if variables.energy_level >= 30: 
                honey_found, bees_dead, state = logic.game_hive.forage_for_honey()
                check_condition(state)
                messagebox.showinfo("Back from foraging", f"A new week has passed your bees have arrived back from foraging where they found {honey_found} honey, Unfortunately {bees_dead} bees died in the process.")
                self.config_all()
            else:
                messagebox.showerror("Not enough energy", f"Sorry you dont have the required 30 energy for that try hibernating to restore it")

    def level_up_bees(self):
        """Activate when user clicks level up button."""
        percentage = round(math.log(variables.honey/2) ** 1.5, 2)
        answer = messagebox.askyesno("Level up bees", f"Leveling up your bees will use half of your honey to upgrade a random Attribute by {percentage}%, are you sure you want to risk it?")
        if answer:
            random_attribute, new_value, state = logic.game_hive.level_up()
            check_condition(state)
            messagebox.showinfo("Leveled Up", f"A new week has passed, your bees {random_attribute} has Increased to {new_value} but your honey has dropped to {variables.honey}.")
            self.config_all()

    def give_up(self):
        """Activate when user clicks give up button."""
        answer = messagebox.askyesno("Giving up already?", "Are you sure you want to give up?")
        if answer:
            root.destroy()


class ExpandHive:
    """Call when user expands hive."""

    def __init__(self, parent):
        """Create tk elements."""
        # Allows me to destroy window later
        self.parent = parent
        self.add_bee_count = 0

        # Configs the main frame
        self.container_frame = config_frame(parent, 4, 4, True, 0, 0, False)

        self.nav_label = tk.Label(self.container_frame, text="Increase Population", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR)
        self.nav_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.count_label = tk.Label(self.container_frame, text=f"Plus {self.add_bee_count} Bees For {self.add_bee_count*5} Honey", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR)
        self.count_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.minus_bees = tk.Button(self.container_frame, text="- 100 bees", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR, command=self.minus_from_bees)
        self.minus_bees.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.add_bees = tk.Button(self.container_frame, text="+ 100 bees", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR, command=self.add_to_bees)
        self.add_bees.grid(row=1, column=2, columnspan=2, sticky="nsew")

        self.confirmation_button = tk.Button(self.container_frame, text="Confirm", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_B, fg=variables.FORGROUND_COLOR, command=self.adapt_total)
        self.confirmation_button.grid(row=2, column=0, columnspan=4, sticky="nsew")

        self.confirmation_button = tk.Button(self.container_frame, text="Cancel", font=variables.FONT_STATS, bg=variables.ACCENT_COLOR, fg=variables.FORGROUND_COLOR, command=self.cancel)
        self.confirmation_button.grid(row=3, column=0, columnspan=4, sticky="nsew")

    def add_to_bees(self):
        """On button click add 100 bees to count."""
        if (self.add_bee_count + 100)*5 <= variables.honey:
            self.add_bee_count += 100
            self.count_label.config(text=f"Plus {self.add_bee_count} Bees For {self.add_bee_count*5} Honey")
        else:
            messagebox.showerror("Not enough honey", f"You dont have enough honey for that")

    def minus_from_bees(self):
        """On button click subtract 100 bees to count."""
        if (self.add_bee_count - 100) >= 0:
            self.add_bee_count -= 100
            self.count_label.config(text=f"Plus {self.add_bee_count} Bees For {self.add_bee_count*5} Honey")
        else:
            messagebox.showerror("Nice try", f"No exploits here!")

    def adapt_total(self):
        """On comfirm update values and close window."""
        if self.add_bee_count == 0:
            messagebox.showerror("No change detected", f"You Have selected a quantity of 0 bees!")
            return
        messagebox.showinfo("Population Increased", f"A new week has passed, your bees population has Increased by {self.add_bee_count} bees, your honey supply has decreased to {variables.honey - self.add_bee_count*5}")
        variables.bee_population += self.add_bee_count
        variables.honey -= self.add_bee_count*5

        state = logic.game_hive.increase_population()
        check_condition(state)
 
        main_window.parent.attributes("-disabled", False)
        main_window.config_all()
        self.parent.destroy()

    def cancel(self):
        """Destory window and open main on cancel."""
        self.parent.destroy()
        main_window.parent.attributes("-disabled", False)
        

def config_root(parent):
    """Configure the root."""
    child_root = tk.Toplevel(parent)
    child_root.grid_columnconfigure(0, weight=1)
    child_root.grid_rowconfigure(0, weight=1)
    return child_root


def config_frame(parent, cols, rows, visibility, row_pos, col_pos, adaptive):
    """Configure the frames."""
    # A frame for all content
    frame = tk.Frame(parent, bg=variables.BACKGROUND_COLOR_A, highlightthickness=0)
    if visibility is True :
        frame.grid(row=row_pos, column=col_pos, sticky="nsew")

    # Configures rows and columns differently depending if adaptive is True
    if adaptive is True :
        for i in range(cols):
            frame.columnconfigure(i, weight=1, uniform="stat_cols", minsize=50)

        for i in range(rows):
            frame.rowconfigure(i, weight=1, uniform="stat_rows", minsize=20)

    else:
        for i in range(cols):
            frame.columnconfigure(i, weight=1, minsize=50)

        for i in range(rows):
            frame.rowconfigure(i, weight=1, minsize=20)
    return frame


def create_entry(parent, message, func):
    """Create a tk entry."""
    label = tk.Label(parent, text=message, font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_C, fg=variables.FORGROUND_COLOR)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    enter_here_label = tk.Label(parent, text="Enter Here:", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_C, fg=variables.FORGROUND_COLOR)
    enter_here_label.grid(row=1, column=0, columnspan=2, sticky="nsew")

    entry = tk.Entry(parent, font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_C, fg=variables.FORGROUND_COLOR)
    entry.grid(row=1, column=2, columnspan=2, sticky="nsew")

    confirmation_button = tk.Button(parent, text="Confirm", font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_C, fg=variables.FORGROUND_COLOR, command=func)
    confirmation_button.grid(row=2, column=0, columnspan=4, sticky="nsew")
    return entry


def create_radio(parent, my_list, message, func):
    """Create a tk radio."""
    # Label
    my_label = tk.Label(parent, text=message, font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_C, fg=variables.FORGROUND_COLOR)
    my_label.grid(row=0, column=0, columnspan=4, sticky="nsew")
    # Setup
    list_variable = tk.StringVar()
    list_variable.set(str(my_list[0]))
    radios = []
    # Creating Radios
    for i, item in enumerate(my_list):
        new_radio = tk.Radiobutton(parent, text=str(item), variable=list_variable, value=item, command=func, font=variables.FONT_STATS, bg=variables.BACKGROUND_COLOR_C, fg=variables.FORGROUND_COLOR, selectcolor=variables.BACKGROUND_COLOR_B)
        new_radio.grid(row=i+1, column=0, columnspan=6, sticky="sew")
        radios.append(new_radio)
    # Returns the instance variable
    return list_variable


def check_condition(game_state):
    """Check win condition."""
    if game_state == "continue":
        return
    else:
        messagebox.showerror("GAME OVER", game_state)
        root.quit()
        root.destroy()
        import sys
        sys.exit()


if __name__ == "__main__":
    """Main."""
    root = tk.Tk()
    root.title("Main Game")
    root.withdraw()

    SetupWindow = SetupWindow(config_root(root))

    stat_window = StatsWindow(config_root(root))
    stat_window.parent.withdraw()

    main_window = HiveWindow(config_root(root))
    main_window.parent.withdraw()

    root.mainloop()
