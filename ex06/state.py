#import sys
def state_var ():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
} 
capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

flag = 'n'        

if capital in capital_cities.values():
          for code, city in capital_cities.items():
             if city == capital:
                state_code = code  
                for state, code in states.items():
                    if code == state_code:
                         print(state)
                                flag = 's'
                         

      #if sigla in states:
       #sigla = capital_cities[capital]
       # return capital_nome
    #return "Capital Desconhecido"


 #def encontrar_capital_city(estado):
  #  if estado in states:
   #   sigla = states[estado]
    #  print (capital_cities[sigla])  
     


    #if len(sys.argv) == 2:
    #    capital = (sys.argv[1]) 
    #    encontrar_estado_city(capital) 
    #else:
    #    print("Por favor, insira apenas uma Capital como argumento")


if __name__ == '__main__':
    state_var()
    get_state ('', join(sys.argv[1:].strip()))


