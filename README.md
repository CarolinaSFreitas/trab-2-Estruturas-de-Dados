# 🐍 Trabalho #2: Listas, Dicionários e Conjuntos

Utilizando os pacotes requests e/ou BeautifulSoup realizar uma pesquisa na Web ou uma API, para obtenção de dados que devem ser manipulados como uma lista de dicionários. As opções devem incluir
as seguintes ações:
  - Listagem dos dados classificados (em ordem) de algum atributo
  - Agrupamento dos dados por algum atributo (para contagem, total ou média)
  - Realizar alguma das operações dos conjuntos sobre a lista de dicionários (intersecção, união, diferença)
  - Pesquisar dados nas listas


## 🛠️ Como meu trabalho foi construído:

+ Usando a API da Vinícola Freitas e a API da Vinícola Soares
  * Node.js
  * npm
  * Express
  * Sequelize
  * MySQL2
  * Cors
  * nodemon
  * Insomnia
  
+ Usando Python
  * Requests
  * Colorama


## 👷🏻‍♀️ O que meu programa faz:

Construí um programa de Análise de Vinícola que irá consumir minhas duas APIs (Vinícola Freitas e Vinícola Soares). O programa possui as seguintes funções:

  1. Listar Vinhos por Preço - Lista os registros de vinhos da API em ordem ascendente de preço (do mais barato ao mais caro)
  2. Ver Total de Vinhos por Tipo - Agrupamento de registros de vinhos e total por tipo (seco, tinto, suave)
  3. Ver Marcas em Comum entre as Vinícolas - Faz a intersecção dos dados de marcas de vinho das duas APIs
  4. Ver Marcas Exclusivas de cada Vinícola - Faz a diferença entre os dados de marcas das duas APIs
  5. Pesquisar por marca de vinho e tipo - Busca nas duas APIs os dados de acordo com a busca realizada pelo usuário 
