import time
import array
import math
import board
import digitalio
from adafruit_circuitplayground import cp
from adafruit_circuitplayground.express import cpx

alarm_mode = False

def alarm(amode, lasta):
    x, y, z = cpx.acceleration
    if lasta[0] != 0 and lasta[1] != 0 and lasta[2] != 0:
        if abs(x - lasta[0]) > 5.0 or abs(y - lasta[1]) > 5.0 or abs(z - lasta[2]) > 5.0:
            print("move")
            amode = True
    #print(str(x) + " " + str(y) + " " + str(z))
    if amode:
        print("alarm")
        cp.play_file("alarm.wav")
    return (amode, (x, y, z))

def colorled(start, end, move, color, t):
    for i in range(start, end, move):
        cp.pixels[i] = color
        time.sleep(t)

mode = False
cp.pixels.brightness = 0.1

bluecol = 255
inmode = True
def modulate(bright, indmode):
    if bright >= 255:
        indmode = True
    elif bright <= 0:
        indmode = False
    if indmode:
        bright -= 3
    else:
        bright += 3
    for i in range(0, 10, 1):
        cp.pixels[i] = (0,bright, 0)
    return (bright, indmode)



timenow = time.monotonic()
timelast = 0.0
totaltime = 0.0
modek = False
def getdelta(t1, t2):
    t2 = t1
    t1 = time.monotonic()
    delta = t1 - t2
    return (t1, t2, delta)

last_a = (0, 0, 0)

while True:
        if cpx.button_a:
            if mode == True:
                cp.pixels.brightness = 0.1
                mode = False
                alarm_mode = False
            else:
                cp.pixels.brightness = 0.1
                mode = True
            time.sleep(0.3)
        if mode:
            #delta time stuff
            tt = getdelta(timenow, timelast)
            timenow = tt[0]
            timelast = tt[1]
            delta = tt[2]
            totaltime += delta
            #alarm stuff
            if totaltime > 0.001:
                ret1 = alarm(alarm_mode, last_a)
                alarm_mode = ret1[0]
                last_a = ret1[1]
                print(str(last_a[0]) + " " + str(last_a[1]) + " " + str(last_a[2]))
                st = modulate(bluecol, inmode)
                bluecol = st[0]
                inmode = st[1]
                totaltime = 0
        else:
            tt = getdelta(timenow, timelast)
            timenow = tt[0]
            timelast = tt[1]
            delta = tt[2]
            totaltime += delta
            if totaltime > 0.8:
                if modek == False:
                    colorled(0, 10, 1, (255, 0, 0), 0)
                    modek = True
                else:
                    colorled(9, -1, -1, (0, 0, 0), 0)
                    modek = False
                totaltime = 0
