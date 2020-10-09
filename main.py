'''
    To-dos: add LCD display code
'''
import os
from importlib import import_module
from utils.lcd import display_test, Message
from utils.lcd_display import display_lcd, display_lcd_init

all_msgs = []

for foldername in os.listdir("msgs"):
    if foldername not in ["sample", "_start_", "_end_"]: # folders to ignore    
        if not os.path.exists("msgs/" + foldername + "/msg.py"):
            raise ValueError("Message file not detected in msgs/" + foldername)
        else:
            msg_list_func = getattr( import_module("msgs." + foldername + ".msg"), "get_msg_list")
            all_msgs.append(msg_list_func())

# display
display_lcd_init()

while True:
    ## start
    display_lcd(   [Message("To Adam & Elena", "", 1) ,
                    Message("To Adam & Elena", "here is a small", 1) ,
                    Message("thank-you gift", "", 1) ,
                    Message("thank-you gift", "from LBBers 2020", 1) ,
                    Message("Enjoy :)", "", 3)] )

    for msg_list in all_msgs:
        # start message
        display_lcd( [Message("o" * (16-i), " " * i + "o" * (16-i), 0.01) for i in range(16)])
        
        # actual message
        display_lcd(msg_list)
        
        # end message
        display_lcd( [Message("o" * i, " " * (16-i) + "o" * i, 0.01) for i in range(16)])

        # pause
        display_lcd( [Message("", "", 2)])

    ## end
    display_lcd(   [Message("That's all!", "", 2) ,
                    Message("By LBBers", "     12 Oct 2020", 10)] )

    display_lcd( [Message("", "", 5)])