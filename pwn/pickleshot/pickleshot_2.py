from typing import Tuple
import base64
import pickle
import re
import os

padlock = ['a', 'b', 'b', 'a', 'T', 'n']
obj = 'kraken'
obj = re.findall('.', obj)

delta_positions = []
for i in range(len(padlock)):
    delta_positions.append(ord(obj[i])-ord(padlock[i]))

class Movement:
    def __init__(self, move: str):
        self.__move = move
    
    def __reduce__(self) -> Tuple:
        return (self.__class__, (self.__move,))
    
    def move(self) -> str:
        return self.__move
    
class Movements:
    def __init__(self, movements: list):
        self.__movements = movements
    
    def __reduce__(self) -> Tuple:
        return (self.__class__, (self.__movements,))
        
    def movements(self) -> list:
        return self.__movements
    

moves  = []
for position in delta_positions:
    up = position > 0
    down = position < 0
    amount = abs(position)
    moves.extend(([Movement("UP")]*amount*up)+([Movement("DOWN")]*amount*down)+[Movement("RIGHT")])
moves.append(Movement("STOP"))

padlock_pos = 0
for movement in moves:        
    if movement.move() == 'STOP':
        break

    if movement.move() == "UP":
        padlock[padlock_pos] = chr(ord(padlock[padlock_pos]) + 1)

    if movement.move() == "DOWN":
        padlock[padlock_pos] = chr(ord(padlock[padlock_pos]) - 1)

    if movement.move() == "RIGHT":
        padlock_pos += 1

if "".join(padlock) == 'kraken':
    print("OK")
else:
    print("FAIL")

data = base64.urlsafe_b64encode(pickle.dumps(Movements(moves))).decode()
print(data, end="\n\n")
command = f"curl -X GET -d \"data={data}\" http://challenges.2023.unitedctf.ca:10761/get_whisky"
print(command, end="\n\n")
print(os.popen(command).read())