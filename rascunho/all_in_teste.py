import sys

states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def detect_expression_type(expression):
    # Check if expression is empty or successive commas
    if not expression or expression == ',':
        return None

    # Check if expression is a state or capital city
    expression = expression.strip()
    if expression.lower() in [state.lower() for state in states.keys()]:
        state = states[expression.capitalize()]
        return f'{capital_cities[state]} is the capital of {expression}'
    elif expression.upper() in capital_cities.keys():
        state = [key for key, value in states.items() if value == expression.upper()][0]
        return f'{capital_cities[expression.upper()]} is the capital of {state}'
    else:
        return f'{expression} is neither a capital city nor a state'

def process_expressions(expressions):
    # Check if expressions are provided
    if not expressions:
        return []

    # Split expressions by comma
    expressions = expressions.split(',')

    # Process expressions and detect their types
    results = [detect_expression_type(expr) for expr in expressions]

    return results

def main():
    # Check if correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 all_in.py \"expression1, expression2, ...\"")
        return

    expressions = sys.argv[1]

    # Process expressions
    results = process_expressions(expressions)

    # Display results
    for result in results:
        if result:
            print(result)

if __name__ == "__main__":
    main()
