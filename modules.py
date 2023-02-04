# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules


import datetime

today = datetime.date.today()

print(today)

# import custom module

import validator

from validator import validate_email

email = "mustafa@taner.com"

if validate_email(email):
    print("email is valid ")
else:
    print("email is bad")

