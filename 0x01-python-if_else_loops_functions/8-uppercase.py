#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c)-(ord('z')-ord('Z')))
        print("{}".format(c), end="")
    print("")
