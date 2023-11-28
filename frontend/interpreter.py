
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))



# here you can call you functions 
from initial_vals import *
from subunits import *

def interpreter(code, tab):

    pars = Parser_Function(tab)


    try: 
        tab.code = code

        tab.row = 0
        tab.line = tab.code[tab.row] 

        pars.get_rid_multiple_lines()
        pars.get_rid("^HAI ?", "code initialized", "No lolcode initailization, Add the keyword 'HAI'")
        pars.get_rid_new_line()
        pars.get_rid("^ *", "spacing")
        pars.get_rid_multiple_lines()

        Variable(tab, pars).main()
        pars.get_rid_multiple_lines()

        while True:
            pars.get_rid_multiple_lines()
            if pars.get_lexemes(["terminate"], False):
                break

            pars.get_rid("^ *", "spacing")
            pars.get_lexemes(["statement"])

    except:
       
        return tab
