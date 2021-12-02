import sys
import scanner
import Mparser
import PrintTree



def test_scanner():
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)
    text = file.read()
    lexer = scanner.lexer
    lexer.input(text)  # Give the lexer some input
    while True:
        tok = scanner.lexer.token()
        if not tok:
            break  # No more input
        print("%d: %s(%s)" % (tok.lineno, tok.type, tok.value))

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example2.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)


    parser = Mparser.parser
    text = file.read()
    ast = parser.parse(text, lexer=scanner.lexer)
    ast.printTree(0)

