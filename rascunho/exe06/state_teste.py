import sys

def get_state(capital):

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


    for state_code, capital_city in capital_cities.items():
        if capital_city == capital:
        # for state_code, capital_city in capital_cities.items():
        #if capital_city == capital:
            return list(states.keys())[list(states.values()).index(state_code)]
        return ("Capital Desconhecida")

    
if __name__ == '__main__':
    capital = input('Digite a Capital: ')
   # capital = capital_city:
    state = get_state(capital)
    print(state)

