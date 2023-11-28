# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import array
import math
import board
import digitalio
from adafruit_circuitplayground import cp

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

# A single sine wave sample is hundredths of a second long. If you set loop=False, it will play
# a single instance of the sample (a quick burst of sound) and then silence for the rest of the
# duration of the time.sleep(). If loop=True, it will play the single instance of the sample
# continuously for the duration of the time.sleep().

def alarm():
    #audio.play(sine_wave_sample, loop=True)  # Play the single sine_wave sample continuously...
    #cp.play_file("shoota.wav")
    time.sleep(1)

def sleepmode(start, end, move, color, t):
    for i in range(start, end, move):
        cp.pixels[i] = color
        time.sleep(t)

mode = False
cp.pixels.brightness = 0.1

while True:
        if mode:
            alarm()
        else:
            sleepmode(0, 10, 1, (255, 0, 0), 0)
            time.sleep(0.9)
            sleepmode(10, 0, -1, (0, 0, 0), 0)
            time.sleep(0.9)
 # for the duration of the sleep (in seconds)
#audio.stop()  # and then stop.