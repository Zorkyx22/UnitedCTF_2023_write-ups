import base64

n =[543, 561, 865, 123, 421, 232, 654, 231, 142, 453, 968, 876, 567, 551, 565, 214, 215, 765, 323, 563, 235]
end_shift = 15
vals = {}
ops = [ (0, 1, int.__mul__),
        (0, 2, int.__add__),
        (1, 3, int.__add__),
        (1, 4, int.__sub__),
        (2, 4, int.__add__),
        (2, 5, int.__add__),
        (3, 6, int.__add__),
        (3, 7, int.__floordiv__),
        (4, 7, int.__add__),
        (4, 8, int.__mul__),
        (5, 8, int.__mod__),
        (5, 9, int.__add__),
        (6, 10, int.__mul__),
        (6, 11, int.__mod__),
        (7, 11, int.__add__),
        (7, 12, int.__add__),
        (8, 12, int.__sub__),
        (8, 13, int.__mul__),
        (9, 13, int.__add__),
        (9, 14, int.__mod__),
        (10, 15, int.__sub__),
        (10, 16, int.__add__),
        (11, 16, int.__sub__),
        (11, 17, int.__sub__),
        (12, 17, int.__sub__),
        (12, 18, int.__mod__),
        (13, 18, int.__floordiv__),
        (13, 19, int.__floordiv__),
        (14, 19, int.__mul__),
        (14, 20, int.__sub__),
    ]

for i in range(len(n)):
    vals[i] = [n[i]]

for op in ops:
    for p in vals[op[0]]:
        vals[op[1]].append(op[2](p, n[op[1]]))

max_vals = []
for i in range(6):
    max_vals.append(max(vals[end_shift + i]))

print(max(max_vals))