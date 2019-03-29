import tkinter as tk
from classes.View import App
root = tk.Tk()
App(root).pack(side="top", fill="both", expand=True)
root.mainloop()
