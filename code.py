# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import array
import math
import board
import digitalio
from adafruit_circuitplayground import cp
from adafruit_circuitplayground.express import cpx

"""try:
    from audiocore import RawSample
except ImportError:
    from audioio import RawSample

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!


FREQUENCY = 2540  # 440 Hz middle 'A'
SAMPLERATE = 8000  # 8000 samples/second, recommended!


# Generate one period of sine wav.
length = SAMPLERATE // FREQUENCY
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15) + 2 ** 15)

# Enable the speaker
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True

audio = AudioOut(board.SPEAKER)
sine_wave_sample = RawSample(sine_wave)"""

alarm_mode = False

def alarm(amode):

    if alarm_mode:
        print("alarm")
        #audio.play(sine_wave_sample, loop=False)
    else:
        print("not alarm")
    #audio.play(sine_wave_sample, loop=True)  # Play the single sine_wave sample continuously...
    #cp.play_file("shoota.wav")
    time.sleep(0.001)
    return amode

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
        cp.pixels[i] = bright
    return (bright, indmode)

for i in range(0, 10, 1):
    cp.pixels[i] = (0, 0, 255)

timenow = time.monotonic()
timelast = 0.0
totaltime = 0.0
modek = False
def getdelta(t1, t2):
    t2 = t1
    t1 = time.monotonic()
    delta = t1 - t2
    return (t1, t2, delta)

while True:
        if cpx.button_a:
            if mode == True:
                cp.pixels.brightness = 0.1
                mode = False
            else:
                cp.pixels.brightness = 0.1
                mode = True
            time.sleep(0.1)
        if mode:
            alarm_mode = alarm(alarm_mode)
            st = modulate(bluecol, inmode)
            bluecol = st[0]
            inmode = st[1]
        else:
            tt = getdelta(timenow, timelast)
            timenow = tt[0]
            timelast = tt[1]
            delta = tt[2]
            totaltime += delta
            print(delta)
            if totaltime > 0.8:
                if modek == False:
                    colorled(0, 10, 1, (0, 255, 0), 0)
                    modek = True
                else:
                    colorled(9, -1, -1, (0, 0, 0), 0)
                    modek = False
                totaltime = 0
 # for the duration of the sleep (in seconds)
#audio.stop()  # and then stop.
