#! /usr/bin/python3
from email.mime import base
import struct
import sys
from zoneinfo import reset_tzpath
file = open("./file.txt",'r').read()
file = file.split("\n")
array = []

# popolo array leggendo da file
for x in file:
    x = int(x, base=16)
    res = x.to_bytes(4, byteorder='little') or b'\0'
    array.append(res.hex())

# eseguo sottrazioni
tmp = ""
cont = 0
for x in array:
    
    if int(x,16) != (0x00000000):
        if cont == 0:
            tmp += (chr(int(x,16)))
        else:
            tmp += (chr((int(x,16) - int(old,16))))
    old = x
    cont = cont + 1 

print(tmp)
