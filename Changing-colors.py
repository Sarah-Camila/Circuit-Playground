import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

max = 255
while max > 0:
    try:
        color_opt=  int(input("Choose the color: Red(1), Green(2) or Blue(3): "))
    except:
        print("Error")
    if 1<= color_opt <= 3:

        if 1 == color_opt:
            for i in range(10):
                cp.pixels[i]=(255,0,0)
            cp.pixels.show()
            time.sleep(0.3)
        if 2 == color_opt:
            for i in range(10):
                cp.pixels[i]=(0,255,0)
            cp.pixels.show()
            time.sleep(0.3)
        if 3 == color_opt:
            for i in range(10):
                cp.pixels[i]=(0,0,255)
            cp.pixels.show()
            time.sleep(0.3)
    else:
        print("Choose a number between 1 and 3.")
        max = max - 1
        quit = input("Press -q- to quit: ").lower()
        if quit=='q':
            print("Program ended.")
            break   
