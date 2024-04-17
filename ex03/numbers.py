               
with open('numbers.txt', 'r') as arquivo:
                numbers = arquivo.read()
                      
numero = numbers.split(',')   

for numeros in numero:
       print(numeros.strip())

