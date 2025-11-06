# atvd 59
58

import random

ns = random.randint(0,11)
palpite = 0
acertou = False
while not acertou:
   ne = int(input('qual o numero que vc quer: '))
   palpite += 1
   if ne == ns:
    acertou = True
   else:
    if ne > ns:
        print("tente um menor: ")
    elif ne < ns:
        print("tente um maior: ")

print("fim, vc acertou com {} tentativas".format(palpite))