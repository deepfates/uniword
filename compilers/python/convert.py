# Convert to Uniword
# This script converts Python code to Uniword code.
# Example usage: python convert.py input.py -o output.uni
from compile import TOKEN_MAP
import argparse

# Reverse Token Mapping
# This dictionary maps Uniword tokens back to their Python equivalents.
REVERSE_TOKEN_MAP = {v: k for k, v in TOKEN_MAP.items()}

# Convert Python to Uniword
# This function takes Python code as input and returns the equivalent Uniword code.
def python_to_uniword(python_code):
    uniword_code = []
    for word in python_code.split():
        if word in REVERSE_TOKEN_MAP:
            uniword_code.append(REVERSE_TOKEN_MAP[word])
        else:
            uniword_code.append(word)
    return ' '.join(uniword_code)

# Main function
# This function handles command line arguments and controls the flow of the program.
def main():
    
    parser = argparse.ArgumentParser(description='Python to Uniword converter.')
    parser.add_argument('input', type=argparse.FileType('r'), help='The Python code to convert.')
    parser.add_argument('-o', '--output', help='The output file. If not provided, the result will be printed to the console.')
    args = parser.parse_args()

    python_code = args.input.read()
    uniword_code = python_to_uniword(python_code)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(uniword_code)
    else:
        print(uniword_code)

if __name__ == "__main__":
    main()
