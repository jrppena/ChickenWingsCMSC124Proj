import subunits as s

class Input():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        # grammar for variable
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "variable name", "there should be a variable")
        var_name = self.tab.capture_group[0]

        # get variable with error handling
        s.Variable(self.tab, self.pars).get_var()

        # put the current data in the front end
        self.tab.show_data()

        # wait for the users' input
        self.tab.root_front.wait_variable(self.tab.buffer)

        # format the user's input using get_lexemes
        prev_line = self.tab.line 
        format_input = self.tab.buffer.get().strip() 
        self.tab.line = format_input + self.tab.line
        value = self.pars.get_lexemes(["input"], error=False)
        if value!= None:
            self.tab.variables[var_name]  = value
        else : 
            self.tab.variables[var_name]  = format_input
            self.tab.line = prev_line

        # grammar: new line
        self.pars.get_rid_new_line()
        return  self.tab.variables[var_name]

