# How to use a module

# USING ALL MODULE

import time
#NOTE: When you import a module directly like that, you have to write module name while using.
#What I mean?:

time.sleep(2)

"USING SPESIFIC THING/THINGS FROM A MODULE"

from math import pow

print(pow(2, 3))

# GIVE A NAME!

from math import pow as USALMA

print(USALMA(2, 4))

# How to create and use your own module ?

#First of all you should create your module.
# Nothing different. Just create a Python file.
#  Let’s create a module!

## myOwnModuleExample.py ##

import myOwnModuleExample
print(myOwnModuleExample.likePow(2, 4))

#OR

from myOwnModuleExample import likePow
print(likePow(2, 5))
