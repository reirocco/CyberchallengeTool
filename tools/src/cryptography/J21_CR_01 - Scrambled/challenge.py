#!/bin/env python3

import random
import string
import itertools


'''
Se non pouoi invertirla, trova un'altro modo.
hint 2:
leggi la documentazione
hint 3:
crea una flag con lo stesso numero di caratteri univoci e con itertools fai il brute sulle combinazioni e filtra.
'''


def scramble(message, key):
    W = len(key)
    #print(W)
    while len(message) % (2 * W):
        message += "#"
    #print(message)

    for _ in range(128):
        message = message[1:] + message[:1]
        #print(" - " + message)
        message = message[0::2] + message[1::2]
        #print(" - " + message)
        message = message[1:] + message[:1]
        #print(" - " + message)
        res = ""
        #print("==============================================")
        for j in range(0, len(message), W):
            for k in range(W):
                res += message[j:j + W][key[k]]
        message = res

    return message


def unscramble(message, key):
    # TODO Write decrypt function before the CTF
    pass


if __name__ == '__main__':
    flag ="l_4Tnb_3cnnbcg3r3slCCm4Id__gb4u}ct{0mr3sds"
    flag2 = "CCIT{abcdefghijklmnopqrstuvzABZDEFGHWJKLM}"
    key = list(range(7))
    keys = itertools.permutations(key)  # creo la permutazione
    for x in keys:
        scrambled = scramble(flag2, x)
        if scrambled[19] == "C" and scrambled[20] == "C" and scrambled[3] == "T" and scrambled[23] == "I":
            print(scrambled)
            final_flag = ""
            for i in flag2:
                res = scrambled.find(i)
                final_flag += flag[res]
            print("final flag --> ", final_flag)
