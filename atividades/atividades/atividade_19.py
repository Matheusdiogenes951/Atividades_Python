# atvd 19
18

from math import sin, cos, hypot, tan, radians
aq = int(input('digite o valor de um angulo '))
s = sin(radians(aq))
c = cos(radians(aq))
t = tan(radians(aq))
print("o seno do angulo e {:.2f}, o cosseno e {:.2f} e a tangente e {:.2f}".format(s, c, t))