#!/usr/bin/python
import AST
import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ("nonassoc","IFX"),
    ("nonassoc", "ELSE"),
    ("left", '+', '-'),
    ("left", '*', '/'),
    ("left", "DOTADD", "DOTMINUS"),
    ("left", "DOTTIMES", "DOTDIVIDE"),
    ("right","UMINUS"),
    ('left', "'")
)



def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : ins_opt"""
    p[0] = AST.Program(p[1])


def p_ins_opt(p):
    """ins_opt : ins """
    p[0] = p[1] if len(p) > 1 else None


def p_ins(p):
    """ins : ins in
             | in"""
    p[0] = p[1] + [p[2]] if len(p) > 2 else [p[1]]


def p_in_empty(p):
    """in : ';'"""


def p_ins_group(p):
    """in : '{' ins '}'"""
    p[0] = AST.Statements(p[2])

def p_assign(p):
    """in : ID '=' expr ';'
                | ID ASSIGNADD expr ';'
                | ID ASSIGNMINUS expr ';'
                | ID ASSIGNMUL expr ';'
                | ID ASSIGNDIV expr ';'"""
    p[0] = AST.Assign(p[2], AST.ID(p[1]), p[3])


def p_expr_binop(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
            | expr DOTADD expr
            | expr DOTMINUS expr
            | expr DOTTIMES expr
            | expr DOTDIVIDE expr"""
    p[0] = AST.BinExpr(p[2], p[1], p[3])

def p_u_minus(p):
    """expr : '-' expr %prec UMINUS"""


def p_expr_lit(p):
    """expr : FLOATNUM
            | NUMBER"""
    p[0] = AST.IntNum(p[1]) if type(p[1]) == int else AST.FloatNum(p[1])


def p_expr_id(p):
    """expr : ID"""
    p[0] = AST.ID(p[1])


def p_expr_str(p):
    """expr : STR"""
    p[0] = AST.String(p[1])



def p_expr_grp(p):
    """expr : '(' expr ')' """
    p[0] = p[2]


def p_transpose(p):
    """expr : expr '\\''"""
    p[0] = AST.Transpose(p[1])


def p_cond(p):
    """cond : expr '<' expr
            | expr '>' expr
            | expr LE expr
            | expr GE expr
            | expr EQ expr
            | expr NEQ expr"""
    p[0] = AST.BinCond(p[2], p[1], p[3])


def p_literal_matrix(p):
    """expr : '[' lists ']'"""
    p[0] = AST.Matrix(p[2])

def p_lists(p):
    """lists : list
             | lists ',' list"""
    p[0] = p[1] + [p[3]] if len(p) > 3 else [p[1]]


def p_list(p):
    """list : '[' seq ']'"""
    p[0] = p[2]


def p_seq(p):
    """seq : expr
           | seq ',' expr"""
    p[0] = p[1] + [p[3]] if type(p[1]) == list else [p[1]]


def p_fun(p):
    """fun : ZEROS
           | EYE
           | ONES"""
    p[0] = p[1]

def p_funcall(p):
    """expr : fun '(' expr ')'"""

    p[0] = AST.Fun(p[1], p[3])


def p_while(p):
    """in : WHILE '(' cond ')' in"""
    p[0] = AST.While(p[3], p[5])



def p_for(p):
    """in : FOR ID '=' expr ':' expr in"""
    p[0] = AST.For(p[2], p[4], p[6], p[7])


def p_if(p):
    """in : IF '(' cond ')' in %prec IFX
            | IF '(' cond ')' in ELSE in"""
    p[0] = AST.IfCond(p[3], p[5], p[7] if len(p) > 7 else None)


def p_control(p):
    """in : BREAK ';'
            | CONTINUE ';'
            | RETURN expr ';'"""
    if p[1] == 'break':
        p[0] = AST.Break()
    elif p[1] == 'continue':
        p[0] = AST.Continue()
    else:
        p[0] = AST.Return(p[2])


def p_print(p):
    """in : PRINT seq ';'"""
    p[0] = AST.Print(p[2])


def p_access(p):
    """in : ID list '=' expr"""




parser = yacc.yacc()
