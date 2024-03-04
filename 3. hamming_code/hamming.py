def find_bit(n_bit):
    c = 0

    while True:
        if(n_bit <= pow(2,c)):
            return c
        else:
            c+=1

def bin_cleaner(number):
    n = str(bin(number).replace("0b",""))
    return f"{'0'*(power-len(n))}{n}"



def ctr_finder():
    for x in range(bit_c):
        ctr_pos.append(pow(2,x)-1)


def parity(bit_pos):
    bit_pos+=1
    c = 0
    d = 0

    for comb in combs:
        if comb[-bit_pos] == "1" and codework[d] == "1" and d not in ctr_pos:
                c+=1

        d+=1

    return c

def real_message():
    rl = ""
    for ll in range(n_codework):
        if ll not in ctr_pos:
            rl+=f"{codework[ll]} "
    
    return rl;


#HAMMING SCHEME

# HS (7,3)
# (codework_bits , check_bits)

n_codework = 7 #bits which compr
codework = list("0"*n_codework)

bit_c = 3
bit_d = n_codework - bit_c

#HAMMING FORMULA for a good hamming scheme
#check_bits + data_bits + 1 <= pow(2, check_bits)

if bit_c + bit_d + 1 <= pow(2,bit_c):
    DATA = "1010" #the effective message

    power = find_bit(n_codework)

    ctr_pos = []
    ctr_finder()

    combs = []

    for x in range(n_codework+1):
        if x != 0:
            combs.append(bin_cleaner(x))

else:
    print("HAMMING FORMULA NOT SATISFIED !")
    exit()