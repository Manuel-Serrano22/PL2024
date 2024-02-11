# Análise de um dataset

Primeiramente, é definida a função **processarDataSet**, cujo objetivo é ler o dataset, "emd.csv", e armazená-lo num dicionário. Neste dicionário, a chave corresponde ao identificador do atleta e o valor aos restantes dados do atleta. Isto permite que as funções apresentadas a seguir evitem estar sempre a percorrer o dataset.

A função **modalidadesDesportivas** recebe o dicionário com os dados do dataset já processados. Percorre-se esse dicionário, onde se extrai todas as modalidades desportivas presentes nos dados. Por fim, ordena-se as modalidades de forma alfabética.
