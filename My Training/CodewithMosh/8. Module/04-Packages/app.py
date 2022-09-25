# Packages
# as an entry point they will no cache (pycache)
# as our program we want to organize our code into sub directories
# otherwise we will be confuse with having hundred or thousand python files on one folder


# from sales # if we do this, python cant find a sales module on directory
           # because we has moved the module on sub-directory "ecommerce"
           # we must add a file python called __init__.py
           # with this python will treat the ecommerce folder as a package
           # package is a container for one or more module
           # in file system terms, a package is mapped to a directory and a module is mapped to a file 

# this example is too long and not clean
import ecommerce.sales
ecommerce.sales.calc_shipping()

# this example is better and cleaner
from ecommerce.sales import calc_tax
