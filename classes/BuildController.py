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

        super().parse_text(app)

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
