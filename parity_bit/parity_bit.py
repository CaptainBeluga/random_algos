def count(message):
    c = 0

    for w in message:
        if w == "1":
            c+=1

    return c

#SENDER
message = "011101"

print(f"-> SENDER MESSAGE => {message}")


if count(message)%2 == 0:
    message+= "0"

else:
    message+= "1"


#   011101 | 0

#  MESSAGE | PARITY BIT

#RECEIVER
message_rec = message[:len(message)-1]
print(f"<- RECEIVER MESSAGE => {message_rec}\n")

if count(message_rec) % 2 == int(message[len(message)-1]):
    print("[+] PARITY BIT CHECK => SUCCESS\n")

else:
    print("[!] THE MESSAGE IS CORRUPTED\n")