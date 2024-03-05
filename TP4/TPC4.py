import re
import sys
import ply.lex as lex

tokens = (
   'Numero', # no maximo com 2 casas decimais
   'Select',
   'From',
   'Where',
   'MaiorQue',
   'Delimitador',
   'AtributoOuTabela',
)

def t_Numero(t):
    r"(\+|-)?(\d+)(.\d{1,2})?"
    return t

def t_Select(t):
    r"(?i)\bSelect\b"
    return t

def t_From(t):
    r"(?i)\bfrom\b"
    return t

def t_Where(t):
    r"(?i)\bwhere\b"
    return t

def t_MaiorQue(t):
    r">="
    return t

def t_Delimitador(t):
    r",|;"
    return t

def t_AtributoOuTabela(t):
    r"[A-Za-z]\w+"
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore  = ' \t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)


def main():
    lexer = lex.lex()
    for linha in sys.stdin:
        lexer.input(linha)
        for tok in lexer:
            print(tok.type, tok.value)

if __name__ == "__main__":
    main()