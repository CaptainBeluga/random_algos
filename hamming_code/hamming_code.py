from hamming import *

def fill_data():
    c = 0
    for d in range(n_codework):
        if(d not in ctr_pos):
            codework[d] = DATA[c]
            c+=1

    return codework


try:
    codework = fill_data()

    for f in range(bit_c):    
        if parity(f) % 2 != 0:
            codework[ctr_pos[f]] = "1"


    print(f"\n\n[+] DISPATCH CODEWORK => {codework}\n\n\n----------------------------------------------------------------\n")

    codework = ['1', '1', '1', '1', '0', '1', '0']

    print(f"\n[?] RECEIVER CODEWORK => {codework}\n")

    n = -1
    for f in range(bit_c):
        n+= ctr_pos[f]+1 if(parity(f) % 2 == 0 and codework[ctr_pos[f]] != "0") or (parity(f) % 2 != 0 and codework[ctr_pos[f]] != "1") else 0

    if n != -1:
        codework[n] = "0" if codework[n] == "1" else "1"

        print(f"[!] ACCURATE CODEWORK => {codework}\n")
        print(f"\n[-] ERROR FOUND in BIT N* {n+1}\n")

    #else:
        #print("\nNO ERROR FOUND !\n")

    print(f"\n----------------------------------------------------------------\n\n\n[+] MESSAGE => {real_message()}\n")

except IndexError:
    print("\nCHECK HAMMING SCHEME")