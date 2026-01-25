https://pythonhow.com/


#importing 

#importing module
from configparser import SectionProxy
import test_functions
test_functions.get_todos()


#importing functions from module
from test_functions import get_todos,write_todos
get_todos


import modules.functions
modules.functions.get_todos()

from modules.functions import get_todos,write_todos
write_todos()

__name__ is set by Python for every module.

If a file is run directly (entry point), 
its __name__ is "__main__".

If a file is imported, its __name__ is the 
module’s import path (e.g., package.module).


which means if we are importing a file and the imported 
file has this Section

if __name__ = "__main__":
    print("something")

the lines under this if block will be executed only 
when the file is run directly and not if it is imported

