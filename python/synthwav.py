import math
import wave
import sys
import re

sys.set_int_max_str_digits(1000000)

with open("hexscript.txt") as hex:
    valuehex = hex.read()

decimal = int(valuehex, 16)

idfk = re.sub(r'(.{3})', r'\1 ', str(decimal))
illegalpattern = r'\b0(\d{2})\b'
fix = re.sub(illegalpattern, r'\1', idfk)
illegalpattern2 = r'\b0(\d)\b'
fix2 = re.sub(illegalpattern2, r'\1', fix)

frequencies = re.findall(r'\b(\d{3})\b', fix2)

#print(frequencies)

## vv credit https://realpython.com/python-wav-files/ vv (this is basically entirely stolen lmao)

FRAMES_PER_SECOND = 44100

def sound_wave(frequency, num_seconds):
    for frame in range(round(num_seconds * FRAMES_PER_SECOND)):
        time = frame / FRAMES_PER_SECOND
        amplitude = math.sin(2 * math.pi * frequency * time)
        yield round((amplitude + 1) / 2 * 255)

with wave.open("output.wav", mode="wb") as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(1)
    wav_file.setframerate(FRAMES_PER_SECOND)

    for x in frequencies: ## credit https://www.w3schools.com/python/python_for_loops.asp
        int_freq = int(x)
        print(int_freq)
        wav_file.writeframes(bytes(sound_wave(int_freq, 0.2)))