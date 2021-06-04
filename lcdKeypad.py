#Created by Vincent Munyalo
#A product of EleTech ©2021
import RPi.GPIO as GPIO
import time
import sys
import drivers

display = drivers.Lcd()

L1 = 16
L2 = 20
L3 = 21
L4 = 5

C1 = 6
C2 = 13
C3 = 19

#Initialize GPIO inputs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
character_list = []

#Get entered phone number
def get_number():
    phone = (''.join(character_list))
    number = str(phone)
    return number

#Read entered character
def read_line(line, characters):
    character = 0
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        character = characters[0]
    elif(GPIO.input(C2) == 1):
        character = characters[1]
    elif(GPIO.input(C3) == 1):
        character = characters[2]
    
    if  character == 0:
        pass
    
    elif character == '*':
        try:
            character_list.pop()
            display.lcd_clear()
            display.lcd_display_string("Enter number:", 1)
            display.lcd_display_string(get_number(), 2)
            
        except:
            pass
        
    #Capture entered character and display
    elif character == '#':
        print('Number entered successfully')
        print('Phone number is ' + get_number())
        display.lcd_clear()
        display.lcd_display_string("Success!", 1)
        time.sleep(2)
        #display.lcd_clear()
        
        
    else:
        for i in range(1):
            print(character)
            character_list.append(character)
        
    GPIO.output(line, GPIO.LOW)
    return character

#Read entered text from membrane 3*4 keypad
def get_text():
    try:
        if len(get_number()) < 11:
            read_line(L1, ["1","2","3"])
            read_line(L2, ["4","5","6"])
            read_line(L3, ["7","8","9"])
            read_line(L4, ["*","0","#"])
            display.lcd_display_string(get_number(), 2)
            time.sleep(0.2)
        else:
            print('Number entered successfully')
            print('Phone number is ' + get_number())
            time.sleep(3)
            sys.exit()
            
            
    except KeyboardInterrupt:
        print("\nProgram is stopped")
        sys.exit()
        
       
display.lcd_clear()
display.lcd_display_string("    Welcome!", 1)
time.sleep(2)
display.lcd_clear()
display.lcd_display_string("Enter number:", 1)

while True:
    try:
        get_text()
        if len(get_number()) < 11:
            pass
         
        elif character == '#':
            #Capture entered character and display
            print('Number entered successfully')
            print('Phone number is ' + get_number())
            display.lcd_clear()
            display.lcd_display_string("Success!", 1)
            time.sleep(2)
            display.lcd_clear()
            GPIO.cleanup()
            break
        
        
        elif character[-1] != '#':
            print("Invalid entry!!")
            get_text()

        else:
            break
 
    except:
        print("Invalid entry")
        '''
        display.lcd_clear()
        time.sleep(1)
        display.lcd_display_string("Invalid entry", 1)
        time.sleep(3)
        display.lcd_clear()
        display.lcd_display_string("Try again.", 1)
        time.sleep(3)
        display.lcd_clear()
        GPIO.cleanup()
        display.lcd_display_string("Enter again:", 1)
        #get_number()
        phone = str(''.join(character_list))
        display.lcd_display_string(phone, 2)
        if len(get_number()) < 11:
            read_line(L1, ["1","2","3"])
            read_line(L2, ["4","5","6"])
            read_line(L3, ["7","8","9"])
            read_line(L4, ["*","0","#"])
            display.lcd_display_string(get_number(), 2)
            time.sleep(0.2)
         ''' 


