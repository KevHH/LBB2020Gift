'''
    sample code. PLEASE KEEP THE NAME OF THIS FILE AS msg.py

    You may run python3 msg.py to test this function. Ignore the moving cursor; it will not appear in the actual display.

'''
## INCLUDE THIS PART
import sys
sys.path.append("../../")
from utils.lcd import Message, display_test
import numpy as np

## DO NOT CHANGE THE NAME OF THIS FUNCTION. This will be imported to the main code
def get_msg_list():
    '''
        This function should return a list of Message objects you created.

        Our screen resolution is 2x16 pixels.

        Note that every Message object takes in 3 arguments:
            - line_one: a string no longer than 16 characters, specifying what to be displayed on first row
            - line_two: a string no longer than 16 characters, specifying what to be displayed on second row
            - duration: a number specifying the duration of display in seconds
    '''
    msg_list = []
    ########################
    ## CUSTOMISATION START #
    ########################

    for lines in [("THANK YOU", "ADAM AND ELENA"), ("FOR ALL THE HARD", "WORK PREPARING"), ("THIS AMAZING", "BOOTCAMP!")]:
        msg_line_one = chr(208) * 16 + lines[0] + chr(208) * (16 + np.max( [0, len(lines[1]) - len(lines[0])] ))
        msg_line_two = chr(208) * 16 + lines[1] + chr(208) * (16 + np.max( [0, len(lines[0]) - len(lines[1])] ))

        for i in range(16):
            msg_list.append(Message(msg_line_one[i:(i+16)], msg_line_two[i:(i+16)], 0.05))
            
        msg_list.append(Message(msg_line_one[16:(16+16)], msg_line_two[16:(16+16)], 1))
        
        for i in range(17,len(msg_line_one) - 16):
            msg_list.append(Message(msg_line_one[i:(i+16)], msg_line_two[i:(i+16)], 0.05))

    msg_list.append(Message("", "         - Kevin", 1))

    ########################
    ## CUSTOMISATION END #
    ########################
    return msg_list

if __name__ == "__main__":
    ## THIS TESTS YOUR MESSAGES ON COMMAND LINE
    display_test(get_msg_list())
