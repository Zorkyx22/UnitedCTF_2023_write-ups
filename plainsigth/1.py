with open("./lire_entre_les_lignes_1.txt", "r") as f:
    lines = f.readlines()
    message = []
    for line in lines:
        message.extend(''.join([chr(int(a, 2)) for a in line.split(' ')]))
    print(''.join(message))