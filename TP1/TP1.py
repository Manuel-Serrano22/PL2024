import sys

def processarDataSet(nomeArquivo):
    dicionario ={} # idAteleta -> dados

    with open(nomeArquivo, "r") as arquivo_csv:
        next(arquivo_csv) # ignora a primeira linha
        for linha in arquivo_csv:
            valores = linha.strip().split(',')  # elimina o "\n"
            dicionario[valores[0]] = valores[1:]

    return dicionario


#Listar de forma alfabetica as modalidades desportivas
def modalidadesDesportivas(dados):
    modalidades = set()

    for chave in dados.keys():
        dado = dados[chave]
        modalidades.add(dado[7])

    modalidadesOrdenadas = sorted(modalidades)
    return modalidadesOrdenadas


#Percentagens de atletas aptos e inaptos para a prática desportiva
def atletasAptosInaptos(dados):
    atletasAptos = 0
    totalAtletas = 0

    for chave in dados.keys():
        dado = dados[chave]
        totalAtletas += 1
        if dado[11] == "true":
            atletasAptos += 1

    percentagemAptos = (atletasAptos / totalAtletas) * 100
    percentagemInaptos = 100 - percentagemAptos

    return (percentagemAptos, percentagemInaptos)


#Distribuição de atletas por escalão etário
def distribuicaoIdade(dados):
    distribuicao = {}

    for chave in dados.keys():
        dado = dados[chave]
        idade = int((dado[4]))
        escalao = (idade // 5) * 5 #Atribui o escalão por limite inferior
        if (escalao, escalao + 4) in distribuicao:
            distribuicao[(escalao, escalao + 4)] += 1
        else:
            distribuicao[(escalao, escalao + 4)] = 1

    dicionario_ordenado = dict(sorted(distribuicao.items()))
    return dicionario_ordenado

def main():

    dicionarioDados = processarDataSet("emd.csv")

    modalidades = modalidadesDesportivas(dicionarioDados)
    print("Modalidades desportivas ordenadas alfabeticamente: ")
    print(modalidades)
    print("\n")

    (atletasAptos, atletasInaptos) = atletasAptosInaptos(dicionarioDados)
    print("Percentagens de atletas aptos e inaptos para a prática desportiva: ")
    print("Aptos: " + str(atletasAptos) + "%")
    print("Inaptos: " + str(atletasInaptos) + "%")
    print("\n")

    distribuicao = distribuicaoIdade(dicionarioDados)
    print("Distribuição de atletas por escalão etário: ")
    print(distribuicao)

main()