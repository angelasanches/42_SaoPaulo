import sys

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
    
def encontrar_capital_city(estado):
    if estado in states:
      sigla = states[estado]
      print (capital_cities[sigla])  
 #   if sigla in capital_cities: 
 #       return capital_cities[sigla]
    else:
       print("estado desconhecido")

if len(sys.argv) == 2:
    estado = (sys.argv[1]) 
    encontrar_capital_city(estado) 
else:
   print("Por favor, insira apenas um estado como argumento")

