import math
from pwnlib.tubes.process import process
import numpy as np

conn = process('nc challenges.2023.unitedctf.ca 33749', True)
input = conn.recv().decode()
sampling_frequency, wave_duration, frequency, target_time = input.split(';')
sampling_frequency = int(sampling_frequency)
wave_duration = int(wave_duration)
frequency = int(frequency)
target_time = float(target_time)

space = np.linspace(0, wave_duration, sampling_frequency*wave_duration)
wave = np.sin((frequency*space)*(2*np.pi))
print(wave)

target_index = math.floor(target_time * (sampling_frequency*wave_duration))

response = wave[target_index]

conn.send(bytes(f"{response}".encode()))
conn.send(b'\n')
print(conn.recv())
conn.close()