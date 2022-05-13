from ast import arg
from distutils.filelist import findall
from numpy import number
from converterBigLittleEndian import Converter
import sys
import re

 
class Parser:

    def parse(self, input):
        string = str(input)
        print(string)
        
        if("Please send me the number" in string):
            res = re.findall(r'\d+', string)
            order = re.findall(r'[a-zA-Z]*-endian',string)
            number = int(res[0])
            arg_size = int(res[2])
            order = str(order[0]).split("-")[0]
            converter = Converter()
            return converter.convert(number,order,arg_size)
        else: 
            #sys.stdout.buffer.write("\n")
            return bytes("\n", 'utf-8')