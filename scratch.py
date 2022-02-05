mydict = {
    "thing 1":{"block 1":1, "block 2":2, "block 3":3},
    "thing 2":{"block 1":1, "block 2":2, "block 3":3},
    "thing 3":{"block 1":1, "block 2":2, "block 3":3},
}

for k, v in mydict.items():
    print(f'{k}, {v}')

i for i in mydict:
    print(i)