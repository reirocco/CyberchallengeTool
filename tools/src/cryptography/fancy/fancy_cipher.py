import copy

#plaintext m: binary string of length 16

k = [0,0,0,1,0,0,1,0,1,1,0,1,1,0,0,0]

m = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0]

#key k: binary string of length 10
def my_fancy_cipher(m,k):
    
    c = copy.copy(m)

    #Encryption process
    for i in range(7):
        for j in range(0,len(k)):

            if k[j]==1:
                pos_0 = ((i+j)+2)%16
                pos_1 = (j+i)%16
                tmp = c[pos_0]
                c[pos_0] = (c[j]+k[pos_1%len(k)])%2
                c[pos_1] = (tmp+k[pos_0%len(k)])%2
            

    return c


print(my_fancy_cipher(m,k))