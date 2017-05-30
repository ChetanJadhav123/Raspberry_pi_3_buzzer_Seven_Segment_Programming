import RPi.GPIO as GPIO
import time

i = 0
c = 0
k = 0
j = 0

S_A = 23
S_B = 24
S_C = 5
S_D = 6
S_E = 13
S_F = 19
S_G = 26

T_1 = 16
T_2 = 20
T_3 = 21

def main():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)      

    GPIO.setup(S_A, GPIO.OUT) 
    GPIO.setup(S_B, GPIO.OUT) 
    GPIO.setup(S_C, GPIO.OUT) 
    GPIO.setup(S_D, GPIO.OUT)
    GPIO.setup(S_E, GPIO.OUT) 
    GPIO.setup(S_F, GPIO.OUT) 
    GPIO.setup(S_G, GPIO.OUT)
    
    GPIO.setup(T_1, GPIO.OUT)
    GPIO.setup(T_2, GPIO.OUT)
    GPIO.setup(T_3, GPIO.OUT) 

    while True:
        for i in range(150):
            time.sleep(1)
            trigger1(c)
            time.sleep(1)
            trigger2(c)
            time.sleep(1)
            trigger3(c)

            if i is 150:
                c=c+1
                if c is 10:
                    k=k+1
                    c=0
                    if k is 10:
                        j=j+1
                        k=0
                        if j is 10:
                            j=0
            i=i+1



def trigger1(c):
    if c is 0:
        GPIO.output(T_1, False)
        GPIO.output(T_2, True)
        GPIO.output(T_3, True)
        seven_segment(0xC0)
        break

    if c is 1:
        GPIO.output(T_1, False)
        GPIO.output(T_2, True)
        GPIO.output(T_3, True)
        seven_segment(0xF9)
        break

    if c is 2:
        GPIO.output(T_1, False)
        GPIO.output(T_2, True)
        GPIO.output(T_3, True)
        seven_segment(0xA4)
        break

    if c is 3:
        GPIO.output(T_1, False)
        GPIO.output(T_2, True)
        GPIO.output(T_3, True)
        seven_segment(0xB0)
        break

    if c is 4:
        GPIO.output(T_1, False)
        GPIO.output(T_2, True)
        GPIO.output(T_3, True)
        seven_segment(0x99)
        break

    if c is 5:
        GPIO.output(T_1, False)
        GPIO.output(T_2, True)
        GPIO.output(T_3, True)
        seven_segment(0x92)
        break

    if c is 6:
        GPIO.output(T_1, False)
        GPIO.output(T_2, True)
        GPIO.output(T_3, True)
        seven_segment(0x82)
        break

    if c is 7:
        GPIO.output(T_1, False)
        GPIO.output(T_2, True)
        GPIO.output(T_3, True)
        seven_segment(0xF8)
        break

    if c is 8:
        GPIO.output(T_1, False)
        GPIO.output(T_2, True)
        GPIO.output(T_3, True)
        seven_segment(0x80)
        break

    if c is 9:
        GPIO.output(T_1, False)
        GPIO.output(T_2, True)
        GPIO.output(T_3, True)
        seven_segment(0x90)
        break
    


                      
def trigger2(k):
    if k is 0:
        GPIO.output(T_1, True)
        GPIO.output(T_2, False)
        GPIO.output(T_3, True)
        seven_segment(0xC0)
        break

    if k is 1:
        GPIO.output(T_1, True)
        GPIO.output(T_2, False)
        GPIO.output(T_3, True)
        seven_segment(0xF9)
        break

    if k is 2:
        GPIO.output(T_1, True)
        GPIO.output(T_2, False)
        GPIO.output(T_3, True)
        seven_segment(0xA4)
        break

    if k is 3:
        GPIO.output(T_1, True)
        GPIO.output(T_2, False)
        GPIO.output(T_3, True)
        seven_segment(0xB0)
        break

    if k is 4:
        GPIO.output(T_1, True)
        GPIO.output(T_2, False)
        GPIO.output(T_3, True)
        seven_segment(0x99)
        break

    if k is 5:
        GPIO.output(T_1, True)
        GPIO.output(T_2, False)
        GPIO.output(T_3, True)
        seven_segment(0x92)
        break

    if k is 6:
        GPIO.output(T_1, True)
        GPIO.output(T_2, False)
        GPIO.output(T_3, True)
        seven_segment(0x82)
        break

    if k is 7:
        GPIO.output(T_1, True)
        GPIO.output(T_2, False)
        GPIO.output(T_3, True)
        seven_segment(0xF8)
        break

    if k is 8:
        GPIO.output(T_1, True)
        GPIO.output(T_2, False)
        GPIO.output(T_3, True)
        seven_segment(0x80)
        break

    if k is 9:
        GPIO.output(T_1, True)
        GPIO.output(T_2, False)
        GPIO.output(T_3, True)
        seven_segment(0x90)
        break



def trigger3(j):
    if j is 0:
        GPIO.output(T_1, True)
        GPIO.output(T_2, True)
        GPIO.output(T_3, False)
        seven_segment(0xC0)
        break

    if j is 1:
        GPIO.output(T_1, True)
        GPIO.output(T_2, True)
        GPIO.output(T_3, False)
        seven_segment(0xF9)
        break

    if j is 2:
        GPIO.output(T_1, True)
        GPIO.output(T_2, True)
        GPIO.output(T_3, False)
        seven_segment(0xA4)
        break

    if j is 3:
        GPIO.output(T_1, True)
        GPIO.output(T_2, True)
        GPIO.output(T_3, False)
        seven_segment(0xB0)
        break

    if j is 4:
        GPIO.output(T_1, True)
        GPIO.output(T_2, True)
        GPIO.output(T_3, False)
        seven_segment(0x99)
        break

    if j is 5:
        GPIO.output(T_1, True)
        GPIO.output(T_2, True)
        GPIO.output(T_3, False)
        seven_segment(0x92)
        break

    if j is 6:
        GPIO.output(T_1, True)
        GPIO.output(T_2, True)
        GPIO.output(T_3, False)
        seven_segment(0x82)
        break

    if j is 7:
        GPIO.output(T_1, True)
        GPIO.output(T_2, True)
        GPIO.output(T_3, False)
        seven_segment(0xF8)
        break

    if j is 8:
        GPIO.output(T_1, True)
        GPIO.output(T_2, True)
        GPIO.output(T_3, False)
        seven_segment(0x80)
        break

    if j is 9:
        GPIO.output(T_1, True)
        GPIO.output(T_2, True)
        GPIO.output(T_3, False)
        seven_segment(0x90)
        break



def seven_segment(bits):
    
    GPIO.output(S_A, False)
    GPIO.output(S_B, False)
    GPIO.output(S_C, False)
    GPIO.output(S_D, False)
    GPIO.output(S_E, False)
    GPIO.output(S_F, False)
    GPIO.output(S_G, False)
        
    if bits&0x01==0x01:
        GPIO.output(S_A, True)
    if bits&0x02==0x02:
        GPIO.output(S_B, True)
    if bits&0x04==0x04:
        GPIO.output(S_C, True)
    if bits&0x08==0x08:
        GPIO.output(S_D, True)
    if bits&0x10==0x10:
        GPIO.output(S_E, True)
    if bits&0x20==0x20:
        GPIO.output(S_F, True)
    if bits&0x40==0x40:
        GPIO.output(S_G, True)


if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
