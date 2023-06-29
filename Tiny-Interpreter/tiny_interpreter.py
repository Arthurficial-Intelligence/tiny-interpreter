def tokenize(code):
    return code.replace("+", " + ").replace("-", " - ").split()


def evaluate(code):
    tokens = tokenize(code)
    if tokens:
        result = int(tokens[0])
        tokens = tokens[1:]
        while tokens:
            op, num = tokens[0], int(tokens[1])
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            tokens = tokens[2:]
        return result
    else:
        return None


def interpret_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
        result = evaluate(code)
        print(f"{result}")


# Example Usage:
filename = "test.pen"
interpret_file(filename)
