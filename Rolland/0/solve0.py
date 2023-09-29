from Crypto.Util.number import inverse, long_to_bytes
import json

public_key_n = 0
public_key_e = 0
flag = ""
first_prime =0
with open("challenge1.json", "r") as f:
    lines = json.load(f)
    flag = int(lines["flag"])
    public_key_n = int(lines["n"])
    public_key_e = int(lines["e"])
    first_prime = int(lines["p"])

second_prime = int(public_key_n // first_prime)

phi = (first_prime-1)*(second_prime-1)

private_key = inverse(public_key_e, phi)

print(long_to_bytes(pow(flag, private_key, public_key_n)))