#!/usr/bin/python

# File to "spin" processor, used to check if shell is hanging when using '&'

with open("numbers.txt", "w") as f:
    for i in range(10000000):
        f.write("%d\n" % i)
print("done writing")
