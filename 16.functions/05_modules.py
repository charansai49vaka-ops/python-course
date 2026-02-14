# Basically modules are used to decrease the writting of another code which was already written by somebody else 
# there are two types of moduels in python language
# there are :  1. Built-in modules
#              2. External modules
# built-in modules are given by python language like sum, os, etc..
# external modules are given by the user from another user which was already written by other programmer
# List of all the built in Modules: https://docs.python.org/3/py-modindex.html
    # built-in modules
import math
print(math.sqrt(16))  #here math are the function which was used by python programmers

import saimodule
saimodule.hello()
#  we can able to import the modules using pip function in terminal
# pip install requests
import requests
r = requests.get("https://www.google.com")
print(r.text)  #it helps to get the full
#  html code of the google without writting it by using get function to receive it


import math
print(math.sqrt(25))

import saimodule
saimodule.hello()

import requests
s=requests.get("https://www.google.com")
print(s.text)


import sai
sai.name()