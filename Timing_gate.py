#!/usr/bin/python
#
# HD44780 LCD Test Script for Rocket Car challenge
# Raspberry Pi
#
#
 
# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND
 
#import
import RPi.GPIO as GPIO
import time
import os
 
# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11
 
# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_INT = True
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line 
 
# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005
 
def main():
  # Main program block  
  # Initialise display
  lcd_init()
 
  # Send some test
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string("Rocket Car")
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string("Challenge 2015.")
 
  time.sleep(5) # 3 second delay

  # Send some text
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string("Ready to record")
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string("rocket car...")

  #Results from Rocket Car Challenge

def lcd_init():
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
  
  # Initialise display
  lcd_byte(0x33,LCD_CMD)
  lcd_byte(0x32,LCD_CMD)
  lcd_byte(0x28,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD)
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x01,LCD_CMD)  

#def lcd_rocket(speed):
# speed = speed(LCD_WIDTH," ")
# for i in range(LCD_WIDTH):
#lcd_byte(ord(speed[i]),LCD_INT)
 
def lcd_string(message):
  # Send string to display
 
  message = message.ljust(LCD_WIDTH," ")  
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)      
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)   

  #Rocket Car function
def rocketcar():
  
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(17, GPIO.IN)
  GPIO.setup(18, GPIO.IN)
  GPIO.setup(27, GPIO.IN)

  start = time.time()
  stop = time.time()
  gateState1 = False
  gateState2 = False
  try:
  	print "Timer ready..."
  
  	while True:
  		if (GPIO.input(18) != gateState1):
        		gateState1 = not gateState1

                	if (gateState1 == True):
                		start = time.time()
                        	print "Gate 1 Success"
                        	break
  	while True:
  		if (GPIO.input(17) != gateState2):
        		gateState2 = not gateState2

                	if (gateState2 == False):
                        	lcd_init()
				lcd_byte(LCD_LINE_1, LCD.CMD)
				lcd_string("Recording error")
				lcd_byte(LCD_Line_2, LCD_CMD)
				lcd_string("Press restart")
				time.sleep(5) #5 second delay	

                	else:
				print "Gate 2 Success"
                        	stop = time.time()

                        	if stop-start > 0.0001:
				
                	        	x =  round((stop-start),2)
                                	s =  round(2/(stop-start),2)
					r =  round(3.6*(2/(stop-start)),2)
                                	#print "Rocket Car timing success!"
 					
					#Initialize LCD
					lcd_init()
					# Send output time and speed
	 				lcd_byte(LCD_LINE_1, LCD_CMD)
  					lcd_string("Time:%x sec" %x)
  					lcd_byte(LCD_LINE_2, LCD_CMD)
  					lcd_string("Successful Run!")
 
	  				time.sleep(5) # 5 second delay

					lcd_byte(LCD_LINE_1, LCD_CMD)
					lcd_string("Speed:%r km/h" %r)
					lcd_byte(LCD_LINE_2, LCD_CMD)
					lcd_string("Speed:%s m/s" %s)
					
					time.sleep(15) # 5 second delay
					break
				
  except KeyboardInterrupt:
	GPIO.cleanup()
	
    		 
if __name__ == '__main__':
  while True:
     main()
     rocketcar()
     GPIO.cleanup()
 # reload()
