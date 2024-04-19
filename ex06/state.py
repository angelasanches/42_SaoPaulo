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

    flag = 'n'        
    if capital in capital_cities.values():
          for code, city in capital_cities.items():
             if city == capital:
                state_code = code  
                for state, code in states.items():
                    if code == state_code:
                        print(state)
                        flag = 's'

    if len(capital.split()) > 1 or flag == 's':
        pass
    else:
     print ("Unknown capital city")

    

if __name__ == '__main__':
    if len(sys.argv) == 2:
         get_state(''.join(sys.argv[1:]).strip())

    