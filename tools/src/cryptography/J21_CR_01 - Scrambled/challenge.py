#!/bin/env python3

import random

def scramble(message, key):
    W = len(key)
    print(W)
    while len(message) % (2*W):
        message += "#"
    print(message)

    for _ in range(128):
        message = message[1:] + message[:1]
        print(" - "+message)
        message = message[0::2] + message[1::2]
        print(" - "+message)
        message = message[1:] + message[:1]
        print(" - "+message)
        res = ""
        print("==============================================")
        for j in range(0, len(message), W):
            for k in range(W):
                res += message[j:j+W][key[k]]
        message = res

    return message


def unscramble(message, key):
    # TODO Write decrypt function before the CTF
    pass

if __name__ == '__main__':


    flag = "abcd"
    key = list(range(7))
    random.shuffle(key)
    scrambled = scramble(flag, key)

    print(scrambled)