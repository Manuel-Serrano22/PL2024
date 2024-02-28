import re
import sys

def processarSomador(nomeFicheiro):
    on = False
    contador = 0

    with open(nomeFicheiro, "r", encoding="utf-8") as file1:
        for linha in file1:
            padrao = re.findall(r"(\bon\b)|(\boff\b)|((?:\+|-)?\b\d+\b)|(?<=\^|\s)(=)(?=\s|$)", linha, re.IGNORECASE)
            lista = [elem for tuplo in padrao for elem in tuplo if elem]

            for elem in lista:
                if elem.lower() == "off":
                    on = False
                elif elem.lower() == "on":
                    on = True
                elif elem == "=":
                    print(contador)
                elif on:
                    contador += int(elem)


def main():

    nomeArquivo = sys.argv[1]
    processarSomador(nomeArquivo)

if __name__ == "__main__":
    main()