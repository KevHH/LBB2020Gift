from os import system, name 
import time

class Message:
    def __init__(self, line_one, line_two, duration):
        '''
            Arguments:
                - line_one: a string no longer than 16 characters, specifying what to be displayed on first row
                - line_two: a string no longer than 16 characters, specifying what to be displayed on second row
                - duration: a number specifying the duration of display in seconds
        ''' 
        # sanitisation
        if not isinstance(line_one, str):
            raise ValueError("line_one must be a string")
        if len(line_one) > 16:
            raise ValueError("line_one must not exceed 16 characters")
        if not isinstance(line_two, str):
            raise ValueError("line_two must be a string")
        if len(line_two) > 16:
            raise ValueError("line_two must not exceed 16 characters")
        if not isinstance(duration, (int, float)):
            raise ValueError("duration must be an int or a float")
        # store
        self.line_one = line_one
        self.line_two = line_two
        self.duration = duration

def display_test(msg_list):
    '''
        Take in a list of objects of Message class, and display them in terminal
    '''
    # sanitisation
    for i, msg in enumerate(msg_list):
        if not isinstance(msg, Message):
            raise ValueError("Item " + str(i) + " in the list is not a Message object")
    
    # display
    clear()

    for msg in msg_list:
        print(msg.line_one)
        print(msg.line_two)
        time.sleep(msg.duration)
        clear()


##########################
# Auxiliary functions
##########################

# function to clear screen
def clear():   
    # for windows 
    if name == 'nt': 
        _ = system('cls')   
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

