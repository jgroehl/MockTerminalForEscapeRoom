import tkinter as tk
from PIL import ImageTk, Image
from classes.LoginController import LoginController
from classes.BuildController import BuildController
from classes.UnlokController import UnlockController
from classes.VideoCapture import VideoCapture


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.START_ROW_COUNT = 2
        self.MAX_ROWS = 25
        self.delay = int(1000.0/24.0)
        self.FONT = ("Courier", 16)
        self.parent = parent
        self.canvas = None
        self.vid = VideoCapture()
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

    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        else:
            self.vid.restart()

        self.canvas.create_text(101, 301, fill="white", font="Consolas 28 bold", anchor="w",
                                text="BITE build success!")
        self.canvas.create_text(100, 300, fill="green", font="Consolas 28 bold", anchor="w",
                                text="BITE build success!")
        self.canvas.create_text(100, 360, fill="white", font="Consolas 24", anchor="w",
                                text="SuperCrumble artifact successfully generated.")
        self.canvas.create_text(101, 461, fill="white", font="Consolas 24 bold", anchor="w",
                                text="Congratulations!")
        self.canvas.create_text(100, 460, fill="green", font="Consolas 24 bold", anchor="w",
                                text="Congratulations!")
        self.canvas.create_text(100, 520, fill="white", font="Consolas 24", anchor="w",
                                text="You have successfully completed the CAMI escape room!")

        self.parent.after(self.delay, self.update)

    def show_end_screen(self):
        def all_children(window):
            _list = window.winfo_children()
            for item in _list:
                if item.winfo_children():
                    _list.extend(item.winfo_children())
            return _list

        widget_list = all_children(self.parent)
        for item in widget_list:
            item.pack_forget()

        self.canvas = tk.Canvas(self.parent, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()
        self.update()
