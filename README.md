# Dados sobre o impacto no mercado de trabalho 😷
[Mini-projeto](https://github.com/dssg-pt/covid19pt-data/issues/152) realizado no âmbito do [repositório de dados sobre a COVID-19 em Portugal](https://github.com/dssg-pt/covid19pt-data)

## 🤔 Contexto:
Um dos maiores impactos do COVID-19 em Portugal tem sido no mercado de trabalho. Como tal, dados relacionados com desemprego, pedidos de _layoff_ ou baixas têm uma extrema importância para melhor entender este impacto, acompanhar e prever a sua evolução. O Ministério do Trabalho, Solidariedade e Segurança Social (MTSSS) disponibiliza estes dados, ao longo do tempo, [num ficheiro .xlsx]( http://www.gep.mtsss.gov.pt/indicadores-covid-19-mtsss).

## 🥅 Objectivo:
Criar uma pipeline de extração diária de dados do ficheiro `.csv` publicado pelo MTSSS com um dicionário de dados associados.

## 👥 Equipa:
* [John Briceno Torres](https://github.com/jbricenot)
* [Mariana Galrinho](https://github.com/marianabvsg)
* [Ana Horta](https://github.com/japana26)

## 🎯 Resultado final:
Criação de um conjunto de ficheiros `.csv` e dicionários de dados com fontes consideradas relevantes para estudos de impacto da COVID-19 no mercado de trabalho em Portugal.

Os conjuntos de ficheiros criados e dicionários de dados correspondentes encontram-se disponíveis [aqui](data_dictionary.md).

## 🧱 Principais etapas:
* Criar um ficheiro `csv` com dados que considerem relevantes desse ficheiro, tais como:
    - Baixas por isolamento.
    - Pedidos de layoff.
    - Despedimentos.
    - Criar um dicionário de dados (tabela em Markdown ou ficheiro .`csv`) com o significado de cada variável.
* Criar um script para atualizar diariamente estes dados extraindo-os da plataforma, com uma lógica semelhante ao que temos feito no repositório (usando o Github Actions).
* Criar um script de teste para testar a validade dos dados e o funcionamento do script, com os testes considerados relevantes.
* Incluir os scripts no workflow atual.

