import tkinter as tk
from PIL import ImageTk, Image
from classes.LoginController import LoginController
from classes.BuildController import BuildController
from classes.UnlokController import UnlockController


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.START_ROW_COUNT = 2
        self.MAX_ROWS = 25
        self.FONT = ("Courier", 16)
        self.parent = parent
        self.row_count = self.START_ROW_COUNT
        self.terminal = None
        self.entered_text = None
        self.cmd_label = None
        self.controller = LoginController()
        self.labels = []
        self.initUI()

    def initUI(self):

        self.parent.title("BITE Compiler")
        self.pack(fill="both", expand=True, side="top")
        self.parent.wm_state("normal")
        self.fullscreen_activate()
        self.configure(background='black', cursor='none')
        self.grid_columnconfigure(1, weight=1)
        img = ImageTk.PhotoImage(Image.open("resources/bite.png"))
        img_panel = tk.Label(self, image=img)
        img_panel.configure(background='black')
        img_panel.photo = img
        img_panel.grid(column=1, row=0, sticky="W")
        self.cmd_label = tk.Label(self, text=">:  ")
        self.cmd_label.configure(background='black', foreground='white', font=self.FONT)
        self.cls()

    def restore_last_command(self, event="none"):
        self.entered_text.set(self.controller.last_command)

    def delete_command(self, event="none"):
        self.entered_text.set("")

    def add_label(self, text, column, sticky="", removable=True, color="white", increment=False, row=None):

        self.gray_out_current_text()

        if self.row_count > self.MAX_ROWS:
            self.cls()
            self.row_count += 1

        if increment:
            self.row_count += 1

        label = tk.Label(self, text=text)
        if row is None:
            row = self.row_count
        label.grid(column=column, row=row, sticky=sticky)
        label.configure(background='black', foreground=color, font=self.FONT)
        if removable:
            self.labels.append(label)

        self.update_terminal_position()

    def gray_out_current_text(self):
        if self.terminal is not None and self.entered_text.get() is not "":
            _text = self.entered_text.get()
            self.row_count += 1
            self.update_terminal_position()
            self.add_label("    ", 0)
            self.add_label(_text, 1, sticky="W", color="#AAAAAA")

    def get_console_text(self):
        return self.entered_text.get().strip()

    def update_terminal_position(self):
        if self.terminal is not None:
            self.terminal.destroy()
        self.cmd_label.grid(column=0, row=self.row_count + 1)
        self.entered_text = tk.StringVar()
        self.terminal = tk.Entry(self, textvariable=self.entered_text, insertbackground="white", borderwidth=0)
        self.terminal.configure(background='black', foreground='white', cursor='none', font=self.FONT)
        self.terminal.grid(column=1, row=self.row_count + 1, sticky="WE")
        self.terminal.bind("<Return>", self.parse)
        self.terminal.bind("<Up>", self.restore_last_command)
        self.terminal.bind("<Down>", self.delete_command)
        ##fixme delete this escape binding in the end!
        self.terminal.bind("<Escape>", self.exit)
        self.terminal.focus()

    def parse(self, event="none"):
        self.controller.parse_text(self)

    def set_controller(self, controller):
        self.controller = controller
        self.cls()

    def set_unlock_controller(self):
        self.set_controller(UnlockController())

    def set_login_controller(self):
        self.set_controller(LoginController())

    def set_build_controller(self, user=""):
        self.set_controller(BuildController(user=user))

    def cls(self):
        self.gray_out_current_text()
        for label in self.labels:
            label.destroy()
        self.labels=[]
        self.row_count = self.START_ROW_COUNT
        self.controller.print_initial_statement(self)

    def fullscreen_activate(self, event="none"):
        self.parent.focus_set()
        self.parent.attributes("-fullscreen", True)
        self.parent.wm_attributes("-topmost", 1)

    def exit(self, event="none"):
        exit()
