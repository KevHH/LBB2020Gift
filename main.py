'''
    To-dos: add LCD display code
'''
import os
from importlib import import_module
from utils.lcd import display_test

all_msgs = []
for foldername in os.listdir("msgs"):
    if foldername not in ["sample2"]: # folders to ignore    
        if not os.path.exists("msgs/" + foldername + "/msg.py"):
            raise ValueError("Message file not detected in msgs/" + foldername)
        else:
            msg_list_func = getattr( import_module("msgs." + foldername + ".msg"), "get_msg_list")
            all_msgs.append(msg_list_func())

for msg_list in all_msgs:
    display_test(msg_list)


