'''
    sample code. PLEASE KEEP THE NAME OF THIS FILE AS msg.py

    You may run python msg.py to test this function. Ignore the moving cursor; it will not appear in the actual display.

'''
## INCLUDE THIS PART
import sys
sys.path.append("../../")
from utils.lcd import Message, display_test

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
    # you can create messages like this
    binary_thanks = '01010100 01001000 01000001 01001110 01001011 01010011 00100001'
    for i in range(47):
        msg_list.append( Message("Did you know....", binary_thanks[i:i+16], 0.1))
    msg_list.append( Message("...is binary for", "                ", 1.5) )
    msg_list.append( Message("...is binary for", "     THANKS!    ", 1.5) )
    msg_list.append( Message("from,           ", "", 1.5) )
    msg_list.append( Message("from,", "     Tom        ", 1) )
    ########################
    ## CUSTOMISATION END #
    ########################
    return msg_list

if __name__ == "__main__":
    ## THIS TESTS YOUR MESSAGES ON COMMAND LINE
    display_test(get_msg_list())
