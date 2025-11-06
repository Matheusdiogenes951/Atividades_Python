# atvd 29
28


import random
ns = random.randint(0,5)
ne = int(input('qual o numero que vc quer: '))
if ns == ne:
    print('parabens vc escolheu o numero {} e o pc escolheu o numero {}'.format(ne,ns))
else:
    print('o pc escoheu {} tente novamente'.format(ns))