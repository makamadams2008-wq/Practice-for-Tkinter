import tkinter as tk

class Stats_Window:
    """ This class is for the main UI that alows you to chnage week and track honey supplies"""
    def __init__(self, root):
        """Initilises all of the varables for my stats window."""
        self.current_honey_supply_label = tk.Label(text="Honey: 10/100000")
        self.current_honey_supply_label.pack()

        self.current_week_label = tk.Label(text="Week 0")
        self.current_week_label.pack()

        self.new_week_button = tk.Button(text= "New Week -->", command = self.new_week)
        self.new_week_button.pack()

    def new_week():
        pass

if __name__ == "__main__":
    