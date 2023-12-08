# compile.pyx
import argparse
from time import time
cimport cython

# Token Mapping
TOKEN_MAP = {
    '.': 'DOT',
    ':': 'POW',
    ';': 'MHM',
    '@': 'AT',
    '^': 'HAT',
    '!': 'BANG',
    '!!': 'BOING',
    '`': 'TICK',
    '```': 'TRICK',
    '~': 'TOCK',
    '#': 'CRUNCH',
    '%': 'BUNCH',
    "'": 'QUOTE',
    '"': 'TWOTE',
    '_': 'UH',
    '__': 'DUH',
    '&': 'AND',
    '&&': 'DAND',
    '?': 'HUH',
    '??': 'WHAH',
    '|': 'PIPE',
    '||': 'DRAIN',
    '<': 'CREEK',
    '>': 'SLAM',
    '{': 'ZIG',
    '}': 'ZAG',
    '[': 'BOX',
    ']': 'UNBOX',
    '(': 'OPE',
    ')': 'CLOPE',
    '-': 'DASH',
    '–': 'SPLASH',
    '—': 'SMASH',
    '/': 'SLASH',
    '\\': 'GASH',
    '=': 'EQUALS',
    '==': 'DEQUALS',
    '===': 'THREEQUALS',
    '!=': 'NEQUALS',
    '$': 'BLING',
    '£': 'STERBLING',
    '€': 'EURBLING',
    ':=': 'WAL',
    '=>': 'AWL',
    ':>': 'OWL',
    '?:': 'EL',
}

# Tokenize the input string
def tokenize(input_string):
    tokens = []
    i = 0
    while i < len(input_string):
        found = False
        for token_string in sorted(TOKEN_MAP.keys(), key=len, reverse=True):
            if input_string.startswith(token_string, i):
                tokens.append(TOKEN_MAP[token_string])
                i += len(token_string)
                found = True
                break
        if not found:
            i += 1  # Skip unknown characters
    return tokens

def parse(tokens):
    ast = []
    operators = ['DOT', 'POW', 'BANG', 'EQUALS', 'AND', 'DAND', 'HUH', 'WHAH', 'PIPE', 'DRAIN', 'CREEK', 'SLAM', 'ZIG', 'ZAG', 'BOX', 'UNBOX', 'OPE', 'CLOPE', 'DASH', 'SPLASH', 'SMASH', 'SLASH', 'GASH', 'DEQUALS', 'THREEQUALS', 'NEQUALS', 'BLING', 'STERBLING', 'EURBLING', 'WAL', 'AWL', 'OWL', 'EL']
    for token in tokens:
        if token in operators:
            # Convert the operator to lower case and append to the AST
            ast.append(token.lower())
        else:
            # If the token is not an operator, append it as is
            ast.append(token)
    return ast

# Generate Python code from AST
def generate_python_code(ast):
    return ' '.join(ast)

# Main function
cpdef main():
    start_time = time()
    
    parser = argparse.ArgumentParser(description='Uniword to Python compiler.')
    parser.add_argument('input', type=argparse.FileType('r'), help='The Uniword code to compile.')
    parser.add_argument('-o', '--output', help='The output file. If not provided, the result will be printed to the console.')
    args = parser.parse_args()

    uniword_code = args.input.read()
    tokens = tokenize(uniword_code)
    ast = parse(tokens)
    python_code = generate_python_code(ast)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(python_code)
    else:
        print(python_code)
    end_time = time()
    print(f"Compilation time: {(end_time - start_time) * 1000} ms")

# Example usage: python compile.py input.uni -o output.py
if __name__ == "__main__":
    main()

