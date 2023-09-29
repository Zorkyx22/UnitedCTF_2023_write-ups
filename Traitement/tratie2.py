import matplotlib.pylab as plt
import math
from pwnlib.tubes.process import process
import numpy as np

conn = process('nc challenges.2023.unitedctf.ca 24918', True)
input = conn.recv().decode()
input = "468; 60; 0.14"
sampling_frequency, wave_duration, frequency= input.split(';')
print(f"{sampling_frequency}, {wave_duration}, {frequency}")
sampling_frequency = int(sampling_frequency)
wave_duration = int(wave_duration)
frequency = float(frequency)

space = np.linspace(0, wave_duration, sampling_frequency*wave_duration)
wave1 = np.sin((0.3*space)*(2*np.pi))
wave2 = np.sin((0.18*space)*(2*np.pi))
wave3 = np.sin((frequency*space)*(2*np.pi))
wave_total = wave1 + wave2 + wave3


count = 0
actual_height = wave_total[0]
ascending = wave_total[1] > wave_total[0]
response = 0

for height in wave_total:
    old_height = actual_height
    actual_height = height
    if(ascending):
        if height < old_height:
            count += 1
            ascending = False
            print(old_height)
    else:
        if height > old_height:
            ascending = True
            print(old_height)
    if count == 12:
        response = height
        break


#target_index = math.floor(target_time * (sampling_frequency*wave_duration))

#response = wave[target_index]

print(f"{response}==0.9996069929701328 : {response==0.9996069929701328}")
conn.send(bytes(f"{response}".encode()))
conn.send(b'\n')
print(conn.recv())
conn.close()