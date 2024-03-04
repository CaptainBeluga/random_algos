N_BIT = 8

DATA = "11100111"
PG = "100011101"

sending = True # True / False
#sending = False
# True => Make CRC
# False => Check the CRC


def fill_data(DATA,N_BIT):
    GEN = []

    for x in range(N_BIT*2):
        GEN.append(DATA[x] if x < N_BIT else "0")
    return GEN

def crc_calc(GEN,PG,N_BIT,):
    c_count = 0

    while c_count < (N_BIT+1)*2:
        c = 0
        g = 0

        for x in GEN:
            if(x=="1"):
                break

            else:
                c+=1

        c_count+= c

        while g < N_BIT+1:
            GEN[c] = "0" if GEN[c] == PG[g] else "1"

            c+=1
            g+=1

    return GEN


def pretty_print(arr):
    msg = ""
    for a in arr:
        msg+= f"{a} "
    
    return msg[:-1]

try:
    #HOW TO RUN
    #GEN = fill_data(DATA,N_BIT)

    #RES_GEN = crc_calc(GEN,PG,N_BIT)



    if sending:
        #SENDING
        RES_GEN = crc_calc(fill_data(DATA,N_BIT),PG,N_BIT)

        print(f"\nCRC-{N_BIT} => {RES_GEN[N_BIT:]}\n\nPAYLOAD => {pretty_print(DATA)} | {pretty_print(RES_GEN[N_BIT:])}")


    else:
        #RECEIVING
        RES_GEN = crc_calc(['1','1','1','0','0','1','1','1','1', '1', '1', '0', '0', '0', '0', '1'],PG,N_BIT) #correct payload
        #RES_GEN = crc_calc(['1','1','1','0','0','1','1','1','0', '1', '1', '0', '0', '0', '0', '1'],PG,N_BIT) #wrong payload

        err = False
        for rg in RES_GEN:
            if rg!="0":
                err = True
                break
        
        print(f"\nPAYLOAD => {pretty_print(DATA)} | {pretty_print(PG)}")
        print("\n[/] ERRORE/I TROVATI !\n" if err else "\n[+] MESSAGGIO CORRETTO !\n")

        #if err:
        #    print("\n[/] ERRORI TROVATI !\n")

        #else:
        #    print("\n[+] MESSAGGIO CORRETTO !\n")

except IndexError:
    print("\n[X] IL MESSAGGIO NON È GENERATO CON IL POLINOMIO GENERATORE (PG) !")