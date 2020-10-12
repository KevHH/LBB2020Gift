'''
    sample code. PLEASE KEEP THE NAME OF THIS FILE AS msg.py

    You may run python3 msg.py to test this function. Ignore the moving cursor; it will not appear in the actual display.

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
    msg_list.append( Message("Amazing, thanks!", " Adam and Elena", 2) )
    msg_list.append( Message(" You are from", "outer space <3!", 2) )

    # or you can create "animations" like this
    for i in range(7):
        if i % 2 == 0:
            space_ship = "oOoO≡≡)==>"
        else:
            space_ship = "OoOo≡≡)==>"
        msg_list.append(Message( " " * i + space_ship, "    Rodrigo", 0.5)) # iteratively add messages with number of spaces before ^_^ = i
    ########################
    ## CUSTOMISATION END #
    ########################
    return msg_list

if __name__ == "__main__":
    ## THIS TESTS YOUR MESSAGES ON COMMAND LINE
    display_test(get_msg_list())
