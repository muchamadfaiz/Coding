"""here we want to import our module called sales.py

from "modul_name" import "object_name/function_name, otherobject_name"
in python all is an object, variable is object, function is object etc
we can import single or multiple object using a comma
dont import all module using (*) just import that you need because 
it can overwrite the object with the same name on that module"""
from sales import calc_shipping, calc_tax

# other way to import the module
# instead of we starting with "from" we start with "import"
# import "modul_name"
import sales # so now in this module we have an object called sales
# and the we can access its member with (.)
sales.calc_tax()
sales.calc_shipping()

calc_shipping()
calc_tax()

"""summary
- so basically we can either import the entire module as an object -> 
import sales
sales.calc_tax()
- or we can import specific object from that module
from sales import calc_tax
calc_tax()"""