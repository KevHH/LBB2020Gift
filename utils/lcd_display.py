from .lcd import Message
from .libs import lcd_i2c 
import time

def display_lcd_init():
    '''
        Initialise lcd screen
    '''
    lcd_i2c.lcd_init()

def display_lcd(msg_list):
    '''
        Take in a list of objects of Message class, and display them on LCD screen
    '''
    # sanitisation
    for i, msg in enumerate(msg_list):
        if not isinstance(msg, Message):
            raise ValueError("Item " + str(i) + " in the list is not a Message object")

    for msg in msg_list:
        lcd_i2c.lcd_string(msg.line_one, lcd_i2c.LCD_LINE_1)
        lcd_i2c.lcd_string(msg.line_two, lcd_i2c.LCD_LINE_2)
        time.sleep(msg.duration)