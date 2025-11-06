# atvd 30
29

vc = int(input('qual a velocidade do carro? '))
vm = 80
multa = 7.0
if vc >= 80:
    cp = (vc - vm) * multa
    vp = print("vc estava acima do limite e tera que pagar uma multa de {}".format(cp))
else:
    print("vc estava no limite permitido!!!")