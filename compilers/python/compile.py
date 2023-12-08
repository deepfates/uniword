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
    # Add more mappings as needed
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

# Parse tokens into an AST
def parse(tokens):
    ast = []
    for token in tokens:
        if token in ['DOT', 'POW', 'BANG', 'EQUALS']:
            # These are placeholders for demonstration
            ast.append(token.lower())
        else:
            ast.append('pass')  # Replace 'pass' with actual Python code as needed
    return ast

# Generate Python code from AST
def generate_python_code(ast):
    return ' '.join(ast)

# Main function
def main():
    uniword_code = "Your Uniword code here"  # Replace with actual Uniword code
    tokens = tokenize(uniword_code)
    ast = parse(tokens)
    python_code = generate_python_code(ast)
    print(python_code)

if __name__ == "__main__":
    main()
