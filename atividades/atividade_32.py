# atvd 32
31

dv = int(input('qual a distancia da viagem? '))
if dv <= 200:
    ct = dv * 0.5
    print("a viagem sera de {}km e vc pagara {}R$".format(dv, ct))
else:
    ct = dv * 0.45
    print("a viagem sera de {}km e vc pagara {}R$".format(dv, ct))