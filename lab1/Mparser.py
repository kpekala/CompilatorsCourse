#!/usr/bin/python

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
    ("right","UMINUS")
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : ins_opt"""


def p_ins_opt(p):
    """ins_opt : ins """


def p_ins(p):
    """ins : ins in
             | in"""


def p_in_empty(p):
    """in : ';'"""


def p_ins_group(p):
    """in : '{' ins '}'"""


def p_assign(p):
    """in : ID '=' expr ';'
                | ID ASSIGNADD expr ';'
                | ID ASSIGNMINUS expr ';'
                | ID ASSIGNMUL expr ';'
                | ID ASSIGNDIV expr ';'"""


def p_expr_binop(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
            | expr DOTADD expr
            | expr DOTMINUS expr
            | expr DOTTIMES expr
            | expr DOTDIVIDE expr"""

def p_u_minus(p):
    """expr : '-' expr %prec UMINUS"""


def p_expr_lit(p):
    """expr : FLOATNUM
            | NUMBER"""


def p_expr_id(p):
    """expr : ID"""


def p_expr_str(p):
    """expr : STR"""


def p_expr_grp(p):
    """expr : '(' expr ')' """


def p_transpose(p):
    """expr : expr '\\''"""


def p_cond(p):
    """cond : expr '<' expr
            | expr '>' expr
            | expr LE expr
            | expr GE expr
            | expr EQ expr
            | expr NEQ expr"""


def p_literal_matrix(p):
    """expr : '[' lists ']'"""


def p_lists(p):
    """lists : list
             | lists ',' list"""


def p_list(p):
    """list : '[' seq ']'"""


def p_seq(p):
    """seq : expr
           | seq ',' expr"""


def p_fun(p):
    """fun : ZEROS
           | EYE
           | ONES"""


def p_funcall(p):
    """expr : fun '(' expr ')'"""


def p_while(p):
    """in : WHILE '(' cond ')' in"""


def p_for(p):
    """in : FOR ID '=' expr ':' expr in"""


def p_if(p):
    """in : IF '(' cond ')' in %prec IFX
            | IF '(' cond ')' in ELSE in"""


def p_control(p):
    """in : BREAK ';'
            | CONTINUE ';'
            | RETURN expr ';'"""


def p_print(p):
    """in : PRINT seq ';'"""


def p_access(p):
    """in : ID list '=' expr"""


parser = yacc.yacc()
