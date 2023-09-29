import base64
import pickle
import random
import os

def mix(s1: str, s2: str) -> str:
    if len(s1) != len(s2):
        raise ValueError('Invalid input')
    
    result = ""
    for c1, c2 in zip(s1, s2):
        r = 0
        
        for i in range(0, 8):
            # Is current bit == 1? 
            bc1 = (ord(c1) >> i) & 1
            bc2 = (ord(c2) >> i) & 1
            
            # 1 if both are 0 or both are 1, 0 elsewise
            bc_result = bc1==bc2
            
            # new bit set
            r += (bc_result << i)
        
        result += chr(r)
    
    return result

ingredients = ["apple", "mango", "peach", "grape", "lemon", "bread", "steak", "flour", "yeast", "sugar", "olive", "honey", "basil", "beans", "onion", "nutty", "melon", "sauce", "cream"]
new_ingredients = ingredients + ["flag-"]

random.shuffle(ingredients)
ingredients += new_ingredients

preparation = ingredients[0]
for ingredient in ingredients[1:]:
    preparation = mix(preparation, ingredient)
print(preparation)

for c in preparation:
    print(f"{ord(c):008b}", end="\t")
print()


obj = "flag-"
result=""
for c1, c2 in zip(preparation, obj):
    r = abs(ord(c1)^~ord(c2))
    result+=chr(r)
    

for c in result:
    print(f"{ord(c):008b}", end="\t")
print()

for c in "flag-":
    print(f"{ord(c):008b}", end="\t")
print()

print(mix(preparation, result))

if preparation == obj:
    print("Success")

data = base64.urlsafe_b64encode(pickle.dumps(new_ingredients)).decode()
command = f"curl -X GET -d \"data={data}\" http://challenges.2023.unitedctf.ca:12812/get_pickle"
print(os.popen(command).read())