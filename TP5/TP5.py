import re
import sys
from decimal import Decimal

import ply.lex as lex


produtos = {1:("Coca-Cola", Decimal("2.50")), 2:("Pepsi", Decimal("1.20")), 3:("Sprite", Decimal("1.40")),
            4:("Batatas Fritas", Decimal("1.00")), 5:("Bolachas", Decimal("0.80")), 6:("Cafe", Decimal("0.70")),
            7:("Chocolate", Decimal("2.10"))}

tokens = (
    "Listar",
    "Moeda",
    "Selecionar",
    "Sair",
)

somadorMoedas = 0

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

def saldoUtilizador(valor):
    novoSaldo = re.sub(r"(\d+)\.(\d+)", substituir, str(valor))
    print("Saldo: ", novoSaldo)
    return novoSaldo

def t_Listar(t):
    r"(?i)\bListar\b"
    for i in range(1, len(produtos)+1):
        print("Produto(id = " + str(i) + ") " + produtos[i][0] + " - " + str(produtos[i][1]) + "€")

def t_Moeda(t):
    r"(?i)moeda\s+(?:(1c|2c|5c|10c|20c|50c|1e|2e),\s+)*(1c|2c|5c|10c|20c|50c|1e|2e)\s+\.$"
    listaMoedas = re.findall(r"(1c)|(2c)|(5c)|(10c)|(20c)|(50c)|(1e)|(2e)", t.value)
    global somadorMoedas
    for _1c, _2c, _5c, _10c, _20c, _50c, _1e, _2e in listaMoedas:
        if _1c:
            somadorMoedas += Decimal('0.01')
        elif _2c:
            somadorMoedas += Decimal('0.02')
        elif _5c:
            somadorMoedas += Decimal('0.05')
        elif _10c:
            somadorMoedas += Decimal('0.10')
        elif _20c:
            somadorMoedas += Decimal('0.20')
        elif _50c:
            somadorMoedas += Decimal('0.50')
        elif _1e:
            somadorMoedas += Decimal('1.00')
        elif _2e:
            somadorMoedas += Decimal('2.00')
    saldoUtilizador(somadorMoedas)

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
            print("O valor do " + produto + " é: " + saldoUtilizador(valor))
            saldoUtilizador(somadorMoedas)
        else:
            print("O produto " + produto + " foi selecionado")
            somadorMoedas -= valor
            saldoUtilizador(somadorMoedas)

def calcularTroco():
    moedas = [1, 2, 5, 10, 20, 50, 100, 200]  # em centimos
    global somadorMoedas
    saldoUtilizador = somadorMoedas
    saldoUtilizadorCentimos = int(saldoUtilizador * 100)
    troco = {}

    for moeda in reversed(moedas):
        while saldoUtilizadorCentimos >= moeda:
            quantidade_moedas = saldoUtilizadorCentimos // moeda
            if(moeda not in troco):
                troco[moeda] = quantidade_moedas
            else:
                troco[moeda] += quantidade_moedas
            saldoUtilizadorCentimos -= quantidade_moedas * moeda

    print(troco)
    return troco

def formatarTroco(troco):
    troco_formatado = ""
    for moeda in troco.keys():
        quantidade = troco[moeda]
        if quantidade > 0:
            if moeda >= 100:
                troco_formatado += f"{quantidade}x {moeda // 100}e "
            else:
                troco_formatado += f"{quantidade}x {moeda}c "
    return troco_formatado.strip()

def t_Sair(t):
    r"(?i)\bSair\b"
    troco = calcularTroco()
    trocoNovo = formatarTroco(troco)
    print(f"Pode retirar o troco: {trocoNovo}")
    print("Até à próxima.")


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore  = ' \t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

def main():
    print("2024-03-08, Stock carregado, Estado atualizado.")
    print("Bom dia. Estou disponível para atender o seu pedido.")
    lexer = lex.lex()
    for linha in sys.stdin:
        lexer.input(linha)
        for tok in lexer:
            print(tok)

if __name__ == "__main__":
    main()
