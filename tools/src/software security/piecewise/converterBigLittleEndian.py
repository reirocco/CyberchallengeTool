#!/usr/bin/python
import os
import sys
from sys import byteorder

def main():

    if(len(sys.argv) == 4):
        number = int(sys.argv[1])
        order = str(sys.argv[2])
        arg_size = int(sys.argv[3])
        conv = Converter()
        print(conv.convert(number,order,arg_size))  #stampa i byte nell'output standard senza applicare formattazioni
        
    else:
        print("Program to convert a number into little-endian/big-endian as a hex.")
        print("You can use : ")
        print("./"+os.path.basename(__file__)+" <number_to_convert> <byte_order> <size>")
        print("use:")
        print("Available byte_order --> 'little' for little_endian, 'big' for big_endian")
        print("Available size --> (32-bit)4, (64-bit) 8")



class Converter:
    def convert(self,number, order, arg_size):
        number = int(number)
        #sys.stdout.buffer.write(number.to_bytes(arg_size,order))    #stampa i byte nell'output standard senza applicare formattazioni
        print(number)
        return number.to_bytes(arg_size,order)

if __name__ == "__main__":
    main()