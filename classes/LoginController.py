from classes.Controller import BaseController


class LoginController(BaseController):

    def __init__(self):
        super().__init__()
        self.MAX_ATTEMPTS = 3
        self.current_attempt = 0
        self.usernamepasswordlist = ["tferge85:JBoSqCPs5uwA",
                                     "hmcnel95:1m4qtp13",
                                     "rbaume84:hL1GYXTvsD5g",
                                     "hweyh84:s71PoIw5hBBF"]

    def print_initial_statement(self, app):
        super().print_initial_statement(app)
        app.add_label(" Please use the 'login' command to log into the BITE system.", 1, sticky="W",
                      removable=True, color="#AAAAAA", row=2)

    def parse_text(self, app):
        text = app.get_console_text()
        self.last_command = text

        if text == "help":
            self.print_help(app)
            app.add_label(text="     cls:\tclears all input commands",
                          column=1,
                          sticky="W",
                          removable=True,
                          color=self.CONTROLLER_COLOR,
                          increment=True)
            return
        if text == "login" or text == "login help":
            self.print_help(app)
            return
        if len(text.strip().split(" ")) > 2 and text.strip().split(" ")[0] == "login":
            strings = text.split(" ")
            if (strings[1] == "-u" and
                    strings[3] == "-p" and len(strings) == 5):
                username = strings[2]
                password = strings[4]
                if username+":"+password in self.usernamepasswordlist:
                        app.set_build_controller(user=username)
                        return
                else:
                    self.current_attempt += 1
                    if self.current_attempt == self.MAX_ATTEMPTS:
                        app.set_unlock_controller()
                        return
                    app.add_label(text=self.CONTROLLER_PREFIX + "Invalid username password combination (" +
                                       str(self.MAX_ATTEMPTS-self.current_attempt) + " attempts remaining)",
                                  column=1,
                                  sticky="W",
                                  removable=True,
                                  color=self.CONTROLLER_COLOR,
                                  increment=True)
                    return
            else:
                app.add_label(text=self.CONTROLLER_PREFIX + "Invalid login command",
                              column=1,
                              sticky="W",
                              removable=True,
                              color=self.CONTROLLER_COLOR,
                              increment=True)
                self.print_help(app)
                return

        super().parse_text(app)

    def print_help(self, app):
        app.add_label(text=self.CONTROLLER_PREFIX + "Login command help:",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
        app.add_label(text="     login:\tthe login command. All parameters must be " +
                           "separated by a single space character.",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
        app.add_label(text="        -u:\tthe username (first command). For example '-u MyUsername'",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
        app.add_label(text="        -p:\tthe password (second command). For example '-p MySecurePassword123'",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
