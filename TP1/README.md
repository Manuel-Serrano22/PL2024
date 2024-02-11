# Análise de um dataset

Primeiramente, é definida a função **processarDataSet**, cujo objetivo é ler o dataset, "emd.csv", e armazená-lo num dicionário. Neste dicionário, a chave corresponde ao identificador do atleta e o valor aos restantes dados do atleta. Isto permite que as funções apresentadas a seguir evitem estar sempre a percorrer o dataset.

A função **modalidadesDesportivas** recebe o dicionário com os dados do dataset já processados. Percorre-se esse dicionário, onde se extrai todas as modalidades desportivas presentes nos dados. Por fim, ordena-se as modalidades de forma alfabética.

A função **atletasAptosInaptos** tem como objetivo calcular as percentagens de atletas aptos e inaptos. Para isso, verifica-se o resultado obtido pelo atleta no exame médico. Se o resultado for "true", o atleta é considerado apto; caso contrário, é considerado inapto. Em cada iteração sobre o dicionário de dados, verifica-se o resultado do exame médico e atualiza-se as variáveis "atletasAptos" e "totalAtletas". Após percorrer o dicionário, são calculadas as percentagens pedidas.
