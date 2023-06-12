# Projeto de Análise de Dados - FreeCodeCamp
 Este é um projeto proposto pelo curso de Análise de Dados com Python no FreeCodeCamp
 
 ## Proposta
 
Criação de uma função chamada `calculate()` em `media_var_std.py` que use Numpy para gerar a média, variância, desvio padrão, valor máximo, valor mínimo e soma das linhas, colunas e todos os elementos em uma matriz 3 x 3.
A entrada da função deve ser uma lista contendo 9 dígitos. A função deve converter a lista em uma matriz Numpy 3 x 3 e, em seguida, retornar um dicionário contendo a média, variância, desvio padrão, valor máximo, valor mínimo e soma de todos os elementos ao longo de ambos os eixos e para todos os valores da matriz.

## Solução
Para a solução do enunciado proposto, foi importada a biblioteca NumPy. A função `calculate()` recebe uma lista e ela é convertida em uma array através do método np.array() e transformada em uma array 3x3 através do método reshape(). Por último foi criado o escopo de um dicionário com as chaves pré-estabelecidas: {mean, variance, standard deviation, max, min, sum}. Cada chave citada recebeu como valor uma lista contendo 3 elementos, com os métodos necessários para calcular o que foi pedido no enunciado.
 
