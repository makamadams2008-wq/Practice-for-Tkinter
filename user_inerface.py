import tkinter as tk
from logic import test_func
test_func()
class Stats_Window:
    """Create the main window for tracking honey supplies"""
    def __init__(self, root):
        """Initilise all of the varables for my stats window."""
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
        """Initilise all of the varables for my connfig window."""
        self.current_honey_supply_label = tk.Label(text="Honey: 10/100000")
        self.current_honey_supply_label.pack()

        self.current_week_label = tk.Label(text="Week 0")
        self.current_week_label.pack()

        self.new_week_button = tk.Button(text= "New Week -->", command = self.new_week)
        self.new_week_button.pack()

    def new_week(self):
        """Update all the values for the next week"""
        pass



if __name__ == "__main__":
    root = tk.Tk()
    main_window = Stats_Window(root)
    root.mainloop()