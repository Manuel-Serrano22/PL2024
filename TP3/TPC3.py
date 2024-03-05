import re
import sys

def processarSomador(nomeFicheiro):
    on = False
    contador = 0

    with open(nomeFicheiro, "r", encoding="utf-8") as file1:
        for linha in file1:
            padrao = re.findall(r"(\bon\b)|(\boff\b)|((?:\+|-)?\b\d+\b)|(?<=\^|\s)(=)(?=\s|$)", linha, re.IGNORECASE)

            for on2, off, num, igual in padrao:
                if off:
                    on = False
                elif on2:
                    on = True
                elif igual:
                    print(contador)
                elif on:
                    contador += int(num)


def main():

    nomeArquivo = sys.argv[1]
    processarSomador(nomeArquivo)

if __name__ == "__main__":
    main()