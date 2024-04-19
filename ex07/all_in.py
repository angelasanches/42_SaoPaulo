import re
import sys

def detect_expression_type(expressions):
    # Check if expressions are provided
    if not expressions:
        return

    # Split expressions by comma
    expressions = expressions.split(',')

    # Remove leading and trailing spaces from each expression
    expressions = [expr.strip() for expr in expressions]

    # Initialize regex pattern for capital and state detection
    capital_pattern = re.compile(r'^[A-Z][a-z]*$')
    state_pattern = re.compile(r'^[A-Z][a-z]*$')

    # Dictionary to store state-capital mappings
    state_capitals = {
        "New Jersey": "Trenton",
        "Oregon": "Salem"
    }

    # Iterate through expressions
    for expr in expressions:
        # Check for empty expression or successive commas
        if not expr or expr == ',':
            continue

        # Check if expression is a capital
        if capital_pattern.match(expr):
            # Check if the capital is associated with a state
            for state, capital in state_capitals.items():
                if capital.lower() == expr.lower():
                    print(f'{capital} is the capital of {state}')
                    break
        # Check if expression is a state
        elif state_pattern.match(expr):
            # Check if the state has a known capital
            state = expr
            if state in state_capitals.values():
                for st, capital in state_capitals.items():
                    if capital == state:
                        print(f'{capital} is the capital of {st}')
                        break
            else:
                print(f'{state} is neither a capital city nor a state')
        # If neither a capital nor a state
        else:
            print(f'{expr} is neither a capital city nor a state')

# Main function
def main():
    # Check if correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 all_in.py \"expression1, expression2, ...\"")
        return

    expressions = sys.argv[1]

    # Call function to detect expression types
    detect_expression_type(expressions)

# Execute the main function
if __name__ == "__main__":
    main()
