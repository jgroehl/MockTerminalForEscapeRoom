from classes.Controller import BaseController


class BuildController(BaseController):

    def print_initial_statement(self, app):
        super().print_initial_statement(app)
        app.add_label(" Welcome to the BITE system. You are currently logged in as " + self.user + ".", 1, sticky="W",
                      removable=True, color="#33FF33", row=2)

    def parse_text(self, app):
        text = app.get_console_text()
        self.last_command = text

        if text == "help":
            self.print_help(app)
            return
        if text == "logout":
            app.set_login_controller()
            return

        text_args = text.split(" ")

        if text_args[0] == "bite":
            if len(text_args) > 1 and text_args[1] == "build":
                if self.check_arguments(text_args):
                    app.show_end_screen()
                    return
                else:
                    app.add_label(text="Your use of the bite command did not achieve your goal :(",
                                  column=1,
                                  sticky="W",
                                  removable=True,
                                  color=self.CONTROLLER_COLOR,
                                  increment=True)
                    return
            else:
                self.print_bite_help(app)
                return

        super().parse_text(app)

    def check_arguments(self, args):
        return False

    def print_bite_help(self, app):
        app.add_label(text="  bite command reference:",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
        app.add_label(text="     bite:\tto compile use 'bite build' with corresponding arguments:",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
        app.add_label(text="     arguments:\tplease refer to the bite build manual for the arguments.",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)

    def print_help(self, app):
        app.add_label(text=self.CONTROLLER_PREFIX + "Core commands list:",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
        app.add_label(text="     cls:\tclears all input commands",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
        app.add_label(text="     bite:\tstarts a bite build for more information type 'bite help'",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
        app.add_label(text="     logout:\tlogs the current user out of the bite build system",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
