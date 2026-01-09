def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        
        except ValueError:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
            
        else:
            return n
            

            
def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        
        except ValueError:
            print('\033[0;31mErro! Digite um número real válido.\033[m')
            
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0.0
            
        else:
            return n2
        
        



# Programa Principal
n = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')

print(f'O número inteiro digitado foi {n} e o real foi {n2}')