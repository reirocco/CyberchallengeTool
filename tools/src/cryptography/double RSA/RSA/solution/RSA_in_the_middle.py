import hashlib
from random import randint, random
import binascii
import binary_search

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from sympy import mod_inverse

if __name__ == '__main__':


    ####################################################

    n = 0xf18af5fccbe293ccb2562f26c3753f2853081a19b94e3360648a02bf5301906f5eac584ef2b28a65edcb389879451e7e1b33341676f2d9a2c87469a0a36d1ec03f047e011b49305fcdf8d19de846c03f23035c5707593f391d725e58b47454c6f5e9484572423a7970aaf26f94f0ef5b8656c8f6febf5d5613dd6dbd8f0fba7a2c9765baa09613bb68b5df87b746e8c960e393a5ec5ea962211a91e506477c761836e1d4844adeab0efdccd9e1ff66398779823ad23971408d216db931e4425a1b16c2a778e5c4c7bcfba0c76a5aeab130c713b68de95087fc1fe12acb3aca6d4c822be6d6d5cbcd45bb3af83223fa93043af40fa29859090a4bdb70c93ce829
    e = 0x10001
    c = 0x8ba3b0acb1cd020ddce07a70994317da188a90777370b0e2eb512d6e8ed6e748e462a51cb7dc752a82fa2bc0c0cb5654c71650308e4a8f2ab083b1a024cbc86265658064b2778f1f4e6188df9a9d305c03e93626bfd5bba581ee63ec64f4f3c6c24ef980a7604f5adbdef8d99661c49545fd48610199918fa1e143e27233e4cb1fb161de4f2ad4ca9c767de854a2ca2dcc14ea4067086dffb5bd1bdd68cbed4a676810fae603a82b6476c0515eae03f17d157f89f0180f763701733bc460e4b7b16770846dd67b813f467f6845bcf44786cf261154c62f0bf1132b6d0907f5ea7b449035b65eab1fec5551a064a359383119248121d462989c991596c2a97874

    list_left = [];

    y_to_e = pow(64, e, n);
    y_to_e_inv = mod_inverse(y_to_e, n);
    val = (y_to_e_inv * c) % n;

    for y in range(1, 2 ** 13):
        y_to_e = pow(y, e, n)
        y_to_e_inv = mod_inverse(y_to_e, n);
        val = (y_to_e_inv * c) % n;
        list_left.append(val);

    indexes, int_list = binary_search.efficient_list_sorting(list_left);

    for x in range(1, 2 ** 13):

        x_to_e = pow(x, e, n);

        pos = binary_search.dicotomic_search(int_list, 0, len(int_list) - 1, x_to_e);
        if pos > 0:
            print("We found valid x and y values");
            y = indexes[pos];
            print("y = " + str(y + 1) + ", x = " + str(x));
            print("m = " + str(x * (1 + y)));
            print("-----------------------------------------");
