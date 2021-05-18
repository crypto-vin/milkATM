import RPi.GPIO as GPIO
import time

L1 = 16
L2 = 20
L3 = 21
L4 = 5

C1 = 6
C2 = 13
C3 = 19

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
    else:
        for i in range(1):
            print(character)
    GPIO.output(line, GPIO.LOW)
    return character
    
def get_text():
    try:
        while True:
            read_line(L1, ["1","2","3"])
            read_line(L2, ["4","5","6"])
            read_line(L3, ["7","8","9"])
            read_line(L4, ["*","0","#"])
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nProgram is stopped")
        
    else:
        pass
    
def get_number():      
    print(get_text())
    character_list.append(get_text())
    if get_text() == '*':
        character_list.pop()
    else:
        pass

for g in range(10):
    get_number()

if get_text() == '#':
    print('Number entered successfully')
number = str(character_list[ : ])
print(number)
