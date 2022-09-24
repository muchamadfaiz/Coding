""""COMPILED PYTHON FILES
if we run this program (app.py)
it will be a new folder named pycache which is a compiled version of the module that we import
python stores the module in the compiled version is to speed up module loading
so next time we load our program pythn will look at the conten of this folder
and if we do have a compiled version of that module python will simply load that compiled version
this will result in faster loading of the module
on pycache the is binary data of our sales module compilation""""

from sales import calc_shipping, calc_tax

import sales 
sales.calc_tax()
sales.calc_shipping()

calc_shipping()
calc_tax()
