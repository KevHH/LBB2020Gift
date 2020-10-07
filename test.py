from os import system, name 

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

import time

clear()


print('my dynamic text\nmy dynamic text\nmy dynamic text\n')

time.sleep(2)

clear()

print('hey\nhey\nhey\n')

time.sleep(2)