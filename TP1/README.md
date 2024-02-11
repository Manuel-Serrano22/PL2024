# Análise de um dataset

## Autor
**Nome**: Manuel Serrano

**ID**: a100825

## Descrição

Primeiramente, é definida a função **processarDataSet**, cujo objetivo é ler o dataset, "emd.csv", e armazená-lo num dicionário. Neste dicionário, a chave corresponde ao identificador do atleta e o valor aos restantes dados do atleta. Isto permite que as funções apresentadas a seguir evitem estar sempre a percorrer o dataset.

A função **modalidadesDesportivas** recebe o dicionário com os dados do dataset já processados. Percorre-se esse dicionário, onde se extrai todas as modalidades desportivas presentes nos dados. Por fim, ordena-se as modalidades de forma alfabética.

Já, a função **atletasAptosInaptos** tem como objetivo calcular as percentagens de atletas aptos e inaptos. Para isso, verifica-se o resultado obtido pelo atleta no exame médico. Se o resultado for "true", o atleta é considerado apto; caso contrário, é considerado inapto. Em cada iteração sobre o dicionário de dados, verifica-se o resultado do exame médico e atualiza-se as variáveis "atletasAptos" e "totalAtletas". Após percorrer o dicionário, são calculadas as percentagens pedidas.

Por fim, a função **distribuicaoIdade**, tem como objetivo calcular a distribuição de idades dos atletas em intervalos de 5 anos. Para isso, percorre-se o dicionário de dados, extrai-se a idade de cada atleta e calcula-se o seu escalão, considerando o limite inferior do intervalo de 5 anos ao qual a idade pertence. De seguida, verifica-se se o intervalo já existe no dicionário "distribuição"; se sim, incrementa-se o contador para esse intervalo; se não, adiciona-se o intervalo à "distribuição". No final, o dicionário resultante é ordenado pelas chaves (intervalos de idade).

