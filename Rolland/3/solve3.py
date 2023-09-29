from Crypto.Util.number import *
import json
from sympy.ntheory.modular import crt
from sympy.simplify.simplify import nthroot
import math
import re
import libnum


rem = []
mod = []
e = 3
with open("./challenge3.json", "r") as file:
    input = json.load(file)
    rem.extend([input["flag1"], input["flag2"], input["flag3"]])
    mod.extend([input["n1"], input["n2"], input["n3"]])

res=libnum.solve_crt(rem,mod)
res = nthroot(res, 3)

print(f"Decipher : {long_to_bytes(res)}")