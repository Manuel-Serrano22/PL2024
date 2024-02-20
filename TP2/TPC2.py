import re
import sys

ordLista = False

def substituirLink(match):

    texto = match.group(1)  # Texto
    link = match.group(2)  # URL

    return f'<a href="{link}"> {texto}</a>'

def substituirImagem(match):

    caminho = match.group(2)
    descricao = match.group(1)

    return f'<img src="{caminho}" alt="{descricao}"/>'

def listaOrdenada(linha):
    global ordLista

    match = re.findall(r"^\d+\. (.*)", linha)

    if match:
        if not ordLista:
            ordLista = True
            resultado = '<ol>\n'
        else:
            resultado = ''
        resultado += f'    <li>{match[0]}</li>\n'
    elif ordLista:
        ordLista = False
        resultado = '</ol>\n' + linha
    else:
        resultado = linha

    return resultado

def mdTOhtlm(nomeArquivo):

    with open(nomeArquivo, "r", encoding= 'utf-8') as ficheiroMD:
        with open("ficheiroHTML.html", "w") as ficheiroHTML:
            for linha in ficheiroMD:
                linha = re.sub(r"^#{1,3} (.*)", r"<h1>\1</h1>", linha) #cabeçalho
                linha = re.sub(r"\*{2}(.*?)\*{2}", r"<b>\1</b>", linha) #negrito
                linha = re.sub(r"\*(.*?)\*", r"<i>\1</i>", linha) #italico
                linha = re.sub(r"[^!]\[(.*?)\]\((.*?)\)", substituirLink, linha) #link
                linha = re.sub(r"\!\[(.*?)\]\((.*?)\)", substituirImagem, linha) #imagem
                #escrever a linha resultante de cada iteração no ficheiroHTML e sempre numa nova linha
                linha = listaOrdenada(linha) # lista ordenada
                ficheiroHTML.write(linha)

def main():
    print(r"Aviso: os ficheiros devem terminar com \n")

    nomeArquivo = sys.argv[1]
    mdTOhtlm(nomeArquivo)

if __name__ == "__main__":
    main()