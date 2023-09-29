from Crypto.Util.number import getPrime, GCD, inverse, bytes_to_long, isPrime
import random
import json
from tqdm import tqdm
import math

def generate_rsa_keys(e):
    while True:
        p = getPrime(512)
        q = getPrime(512)

        phi = (p - 1) * (q - 1)

        if GCD(e, phi) == 1:
            n = p * q
            d = inverse(e, phi)
            return (e, n), d

flag=0
n=0
e=0
with open("challenge4.json", 'r') as f:
    lines = json.load(f)
    flag=lines["flag"]
    n=lines["n"]
    e=lines["e"]

current = int(math.sqrt(n))
current += not(current % 2)
with tqdm(total=current) as pbar:
    while current > 0:
        pbar.update(1)
        p = n/current
        if p * current == n:
            print(f"Found factor : {current}")
        else:
            current-=2
if current <= 1:
    print("Failed")