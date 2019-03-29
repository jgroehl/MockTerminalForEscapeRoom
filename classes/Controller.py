class BaseController(object):
    def __init__(self, user=None):
        self.CONTROLLER_PREFIX = "  > "
        self.CONTROLLER_COLOR = "#7494a1"
        self.last_command = ""
        self.user = user

    def print_initial_statement(self, app):
        app.add_label(" Welcome to BITE Compiler", 1, sticky="W", removable=True, color="#96640c", row=1)

    def parse_text(self, app):
        text = app.get_console_text()
        self.last_command = text

        if text == "cls":
            app.gray_out_current_text()
            app.cls()
            return

        if text == "version":
            app.add_label(text=self.CONTROLLER_PREFIX + "BITE Compiler V6.13.986_6667",
                          column=1,
                          sticky="W",
                          removable=True,
                          color=self.CONTROLLER_COLOR,
                          increment=True)
            app.add_label(text=self.CONTROLLER_PREFIX + "Last changes by tferge74",
                          column=1,
                          sticky="W",
                          removable=True,
                          color=self.CONTROLLER_COLOR,
                          increment=True)
            return

        app.add_label(text=self.CONTROLLER_PREFIX + "Command not valid. Try enter 'help' to get information.",
                      column=1,
                      sticky="W",
                      removable=True,
                      color=self.CONTROLLER_COLOR,
                      increment=True)
