import ply.lex as lex

reserved = {
    "if": "IF",
    "else": "ELSE",
    "for": "FOR",
    "while": "WHILE",
    "break": "BREAK",
    "continue": "CONTINUE",
    "return": "RETURN",
    "eye": "EYE",
    "zeros": "ZEROS",
    "ones": "ONES",
    "print": "PRINT"
}

literals = "+-*/(),;='{}[]<>:"
tokens = [ 'NUMBER', 'ID',
          'DOTADD', 'DOTTIMES', 'DOTMINUS', 'DOTDIVIDE',
          'ASSIGNADD', 'ASSIGNMINUS', 'ASSIGNMUL', 'ASSIGNDIV',
          'LE', 'GE', 'NEQ', 'EQ', 'STR', 'FLOATNUM', 'UMINUS'
          ] + list(reserved.values())

t_DOTADD = r'\.\+'
t_DOTTIMES = r'\.\*'
t_DOTMINUS = r'\.-'
t_DOTDIVIDE = r'\./'

t_ASSIGNADD = r'\+='
t_ASSIGNMINUS = r'\-='
t_ASSIGNMUL = r'\*='
t_ASSIGNDIV = r'/='

t_LE = r'<='
t_GE = r'>='
t_NEQ = r'!='
t_EQ = r'=='

t_STR = r"\".*?\""

t_ignore = ' \t'


def t_FLOATNUM(t):
    r"\d*\.\d+|\d+\."
    t.value = float(t.value)
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, "ID")
    return t


def t_COMMENT(t):
    r'\#.*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
