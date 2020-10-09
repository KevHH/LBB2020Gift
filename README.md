# LBB2020Gift
Documentation for setting up LCD display 1602 (controller HD44780) with Raspberry Pi and code for the gift to Adam and Elena.

## Instructions on adding your code (PLEASE READ THIS)

1. Git clone this repository.
2. Go into the `msg` folder. Make a copy of the `sample` folder and rename it to your name.
3. Edit the customisable part in `msg.py` file to put your messages. Do NOT change the file name `msg.py` or the function name `get_msg_list`.
4. Feel free to get creative! You may use animations in the way shown in the sample, or use symbols (ASCII 0 - 255) to draw pictures.   
5. When you are done, run `git pull` first to ensure you have the most up-to-date repo, and do `git push` to commit your code. 


## Materials (TBC)
- Raspberry Pi 4
- LCD Display 1602 with i2C backpack from https://www.amazon.co.uk/gp/product/B07PG1MTJ9/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1
- 5V to 3.3V logic level converter from https://www.amazon.co.uk/gp/product/B07PY3CRFM/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1

## Raspberry Pi Setup
Modified from: https://tutorials-raspberrypi.com/control-a-raspberry-pi-hd44780-lcd-display-via-i2c/ and https://www.raspberrypi-spy.co.uk/2015/05/using-an-i2c-enabled-lcd-screen-with-the-raspberry-pi/

![alt text](_data/raspberry_pi_GPIO.png)


