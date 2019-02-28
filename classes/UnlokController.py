from classes.Controller import BaseController


class UnlockController(BaseController):

    def __init__(self):
        super().__init__()
        self.usernamepasswordlist = ["PUK"]

    def print_initial_statement(self, app):
        super().print_initial_statement(app)
        app.add_label(" Too many unsuccessful login attempts. Please use the 'unlock' return to the BITE system.", 1,
                      sticky="W", removable=True, color="#FF3333", row=2)

    def parse_text(self, app):
        text = app.get_console_text()
        self.last_command = text

        if text == "help":
            app.add_label(text="     Did you really think you are getting help to 'hack' into the BITE system..",
                          column=1,
                          sticky="W",
                          removable=True,
                          color=self.CONTROLLER_COLOR,
                          increment=True)
            return
        if text == "unlock" or text == "unlock help":
            self.print_help(app)
            return
        if len(text.strip().split(" ")) > 2 and text.strip().split(" ")[0] == "unlock":
            strings = text.split(" ")
            if strings[1] == "-k" and len(strings) == 3:
                key_phrase = strings[2]
                if key_phrase in self.usernamepasswordlist:
                        app.set_login_controller()
                        return
                else:
                    app.add_label(text=self.CONTROLLER_PREFIX + "Invalid unlock key",
                                  column=1,
                                  sticky="W",
                                  removable=True,
                                  color=self.CONTROLLER_COLOR,
                                  increment=True)
                    return
            else:
                app.add_label(text=self.CONTROLLER_PREFIX + "Invalid unlock command usage",
                              column=1,
                              sticky="W",
                              removable=True,
                              color=self.CONTROLLER_COLOR,
                              increment=True)
                self.print_help(app)
                return

        super().parse_text(app)

    def print_help(self, app):
        app.add_label(text=self.CONTROLLER_PREFIX + "Unlock command help:",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
        app.add_label(text="     unlock:\tthe unlock command. The argument must be " +
                           "separated by a space character.",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
        app.add_label(text="        -k:\tthe unlock key. For example '-k MySecureUnlockKey123'",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)