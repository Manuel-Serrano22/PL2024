import re
import sys
from decimal import Decimal

import ply.lex as lex


produtos = {1:("Coca-Cola", 2.50), 2:("Pepsi", 1.20), 3:("Sprite", 1.40),
            4:("Batatas Fritas", 1.00), 5:("Bolachas", 0.80), 6:("Cafe", 0.70),
            7:("Chocolate", 2.10)}

tokens = (
    "Listar",
    "PalavraMoeda",
    "Moeda",
    "Selecionar",
    "Sair"
    "Delimitador",
)

somadorMoedas = 0

def t_Listar(t):
    r"(?i)\bListar\b"
    for i in range(1, len(produtos)+1):
        print("Produto(id = " + str(i) + ") " + produtos[i][0] + " - " + str(produtos[i][1]) + "€")

def t_PalavraMoeda(t):
   r"(?i)\bMoeda\b"

def t_Moeda(t):
    r"1c|2c|5c|10c|20c|50c|1e|2e"
    global somadorMoedas
    if re.match("1c", t.value):
        somadorMoedas += Decimal('0.01')
    elif re.match("2c", t.value):
        somadorMoedas += Decimal('0.02')
    elif re.match("5c", t.value):
        somadorMoedas += Decimal('0.05')
    elif re.match("10c", t.value):
        somadorMoedas += Decimal('0.10')
    elif re.match("20c", t.value):
        somadorMoedas += Decimal('0.20')
    elif re.match("50c", t.value):
        somadorMoedas += Decimal('0.50')
    elif re.match("1e", t.value):
        somadorMoedas += Decimal('1.00')
    elif re.match("2e", t.value):
        somadorMoedas += Decimal('2.00')

def t_Selecionar(t):
    r"(?i)\bSelecionar\b\s+\d+"
    global somadorMoedas
    identificador = re.search(r"(\d+)", t.value).group(1)
    if(int(identificador) > len(produtos)):
        print("Não existe esse produto")
    else:
        produto = produtos[int(identificador)][0]
        valor = produtos[int(identificador)][1]

        if(valor > somadorMoedas):
            print("O valor do " + produto + " é: " + str(valor) + "€")
        else:
            print("O produto " + produto + " foi selecionado")
            somadorMoedas -= Decimal(str(valor))


def t_Sair(t):
    r"(?i)\bSair\b"
    print(t.value)

def t_Delimitador(t):
    r","

def substituir(match):
    if(re.match(r"^0", match.group(1))):
        if(re.match(r"^0", match.group(2))):
            novoSaldo = re.sub(r"0(\d+)", r"\1c", match.group(2))
        else:
            novoSaldo = re.sub(r"(\d+)", r"\1c", match.group(2))
    else:
        euros = re.sub(r"(\d+)", r"\1e", match.group(1))
        if (re.match(r"^0", match.group(2))):
            centimos = re.sub(r"0(\d+)", r"\1c", match.group(2))
        else:
            centimos = re.sub(r"(\d+)", r"\1c", match.group(2))
        novoSaldo = euros+centimos

        if(re.match("0", centimos)):
            novoSaldo = euros
    return novoSaldo

def t_newline(t):
    r"\n+"
    global somadorMoedas
    if(somadorMoedas != 0):
        novoSaldo = re.sub(r"(\d+)\.(\d+)", substituir, str(somadorMoedas))
        print("Saldo: ", novoSaldo)
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
            print(tok)

if __name__ == "__main__":
    main()
