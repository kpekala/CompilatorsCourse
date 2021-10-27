import ply.lex as lex

literals = "+-*/()"
tokens = ('PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'NUMBER', 'ID',
          'DOTADD', 'DOTTIMES', 'DOTMINUS', 'DOTDIVIDE')
t_DOTADD = r'\.\+'
t_DOTTIMES = r'.\*'
t_DOTMINUS = r'.-'
t_DOTDIVIDE = r'./'
t_ignore = ' \t'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
