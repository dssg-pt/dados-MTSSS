## Conteúdo

O repositório contém:
- `original_files/`: Dados extraídos diretamente do MTSSS;
- `dataframes/`: Dados obtidos após tratamento;
- `notebooks/`:
    - `data_extraction.ipynb`: notebook Python que extrai os últimos dados (ficheiro .xlsx) em [MTSSS](http://www.gep.mtsss.gov.pt/indicadores-covid-19-mtsss) e os guarda em formato .csv (divididos em categorias) no diretório `original_files/`;
    - `data_cleaning.ipynb`: notebook Python que trata e limpa os dados em `original_files/`, atualizando-os no diretório `dataframes/`;
    - `data_analysis.ipynb`: notebook Python que trata da análise visual dos dados em `dataframes/`.
- `src/`:
    - `data_extraction.py`: semelhante a `data_extraction.ipynb`  mas em formato .py;
    - `data_cleaning.py`: semelhante a `data_cleaning.ipynb` mas em formato .py;
- `issues.txt`: ficheiro .txt com descrição dos problemas que ocorrem devido a inconsistências na estrutura dos dados nos ficheiros em `original_files/`.


## Extração de Dados

- Extrai o último ficheiro do [MTSSS](http://www.gep.mtsss.gov.pt/indicadores-covid-19-mtsss)
- Guarda todas as worksheets do ficheiro .xlsx separadamente em `original_files/`


## Tratamento de Dados

Dados considerados relevantes para o estudo, juntamente com alguns detalhes/assumptions tomados no seu tratamento:
#### Baixas por Isolamento
- Baixas por data de entrada (`baixas_all.csv`);
- Baixas por distrito (`baixas_distrito.csv`);
#### Layoff
- Layoff por dia (`df_layoff.csv`) : informação relativa às Entidades Empregadoras (EE) que entregaram documentos;
- Layoff por setor económico- Quantidade de companhias em layoff: Informação relativa a quantidade de companhias por setor económico que entraram em layoff. Esta informação e anexa a um dataframe que contem a informação histórica obtida por relatórios antigos (`historical_data_company.csv`)
- Layoff por setor económico- Quantidade de trabalhadores em layoff: Informação relativa a quantidade de trabalhadores por setor económico que entraram em layoff. Esta informação e anexa a um dataframe que contem a informação histórica obtida por relatórios antigos (`historical_data_person.csv`)
- Layoff por setor económico- Quantidade de trabalhadores por género em layoff: Informação relativa a quantidade de trabalhadores divididos por género, por setor económico, que entraram em layoff. (`df_work.csv`)
- Layoff por dimensão da empresa: Informação relativa a quantidade de companhias divididas por dimensão da empresa que entraram em layoff. Esta informação e anexa a um dataframe que contem a informação histórica obtida por relatórios antigos (`historical_data_company_size.csv`)
- Layoff por região: Informação relativa a quantidade de companhias divididas por região da empresa, que entraram em layoff. (`organization_region.csv`)
 
#### Redução de Atividade
- Redução de atividade por data de registo dos pedidos (`reducao_atividade_porDia.csv`): 
  - A divisão das várias tabelas na worksheet de Redução de Atividade é obtida através da identificação das linhas que possuem todos as colunas em branco (excepto a primeira);
  - Nesta tabela são apenas mantidas as linhas com formato de data na primeira coluna de forma a remover as linhas com o total, uma vez que a existência destas não é consistente ao longo dos vários ficheiros publicados;
- Redução de atividade por distrito de residência (`reducao_atividade_porDistrito_Total.csv`, `reducao_atividade_porDistrito_porMes.csv` e `reducao_atividade_bydistrict_historicaData.csv`): 
  - Dado que não existe consistência nas colunas com o total de pedidos (por vezes são publicados ficheiros sem total ou com o total apenas para certos tipos de pedidos), começa-se por criar um .csv com os dados por mês para cada tipo (removendo as colunas sem identificação ou identificadas como total);
  - Depois é criado um .csv com os totais, obtidos a partir da soma para todos os meses;
- Redução de atividade por sexo (`reducao_atividade_porSexo.csv` e `reducao_atividade_bysex_historicaData.csv`);
#### Despedimentos Coletivos
- Despedimentos por dia (`despedimentos_coletivos.csv`). 

Guarda os dados tratados (ficheiros .csv mencionados acima) em `dataframes/`, excepto os dataframes `historical_data_company.csv` , `historical_data_person.csv` e `historical_data_company_size.csv`, que se encontram guardados em `original_files/`.


## Dicionário de Dados

## Baixas

#### Baixas por Data de entrada - `baixas_all.csv` :
| Coluna | Descrição |
| --- | --- |
| DATA | Data de entrada |
| POR DIA | Número de prestações requiridas por dia |
| ACUMULADOS | Número de prestações acumulado ao longo do tempo |

#### Baixas por Distrito - `baixas_distrito.csv` :
| Coluna | Descrição |
| --- | --- |
| DISTRITO | Distrito de entrada da prestação |
| TOTAL | Número de prestações total por distrito |

## Layoff 

#### Layoff por Data (Quanto a Entidades Empregadoras (EEs) que entregaram documento) - `df_layoff.csv` :
| Coluna | Descrição |
| --- | --- |
| DATA | Data  |
| Nº TRABALHADORES | Número de trabalhadores - valor acumulado |
| REMUNERAÇÕES DECLARADAS | Massa salarial - valor acumulado |

#### Layoff por Setor e Sexo (Quanto a Entidades Empregadoras (EEs) que entregaram documento) - `df_work.csv` :
| Coluna | Descrição |
| --- | --- |
| Setor | Setores de Indústria  |
| Nº empresas | Número de empresas em layoff |
| Nº TRABALHADORES | Número total de trabalhadores em layoff |
| FEMININO | | Nº de trabalhadores do sexo feminino em layoff |
| MASCULINO | Nº de trabalhadores do sexo masculino em layoff |

#### Layoff por setor económico- Quantidade de companhias em layoff - `historical_data_company.csv`:
| Coluna | Descrição |
| --- | --- |
| Setor | Setores de Indústria  |
| Datas | As restantes colunas contêm o número total de companhias em layoff para a respetiva data|

#### Layoff por setor económico- Quantidade de trabalhadores em layoff - `historical_data_person.csv`
| Coluna | Descrição |
| --- | --- |
| Setor | Setores de Indústria  |
| Datas | As restantes colunas contêm o número total de trabalhadores em layoff para a respetiva data|

#### Layoff por dimensão da empresa - `historical_data_company_size.csv`
| Coluna | Descrição |
| --- | --- |
| TOTAL | Dimensão da empresa  |
| Datas | As restantes colunas contêm o número total de empresas em layoff divididos por dimensão para a respetiva data|

#### Layoff por região - `organization_region.csv`
| Coluna | Descrição |
| --- | --- |
| Region | região do Portugal  |
| N° Empresas | Numero total de companhias em layoff para a respetiva região |
| Percentual(%) | Numero percentual da região comparado com o total do Portugal |



## Redução de Atividade

#### Redução de Atividade por Dia - `reducao_atividade_porDia.csv` :
| Coluna | Descrição |
| --- | --- |
| DATA | Data de registo dos pedidos |
| TI_ParagemTotal | Número de pedidos de Paragem Total para Trabalhadores Independentes   |
| TI_Reducao | Número de pedidos de Redução de Atividade para Trabalhadores Independentes |
| TI_Total | Número total de pedidos para Trabalhadores Independentes  |
| PRO_TI_ParagemTotal | Número de pedidos de Paragem Total para Trabalhadores Independentes - Prorrogação   |
| PRO_TI_Reducao | Número de pedidos de Redução de Atividade para Trabalhadores Independentes - Prorrogação |
| PRO_TI_Total | Número total de pedidos para Trabalhadores Independentes - Prorrogação |
| MOE_ParagemTotal | Número de pedidos de Paragem Total para Membro de Orgão Estatutário   |
| MOE_Reducao | Número de pedidos de Redução de Atividade para Membro de Orgão Estatutário |
| MOE_Total | Número total de pedidos para Membro de Orgão Estatutário  |
| PRO_MOE_ParagemTotal | Número de pedidos de Paragem Total para Membro de Orgão Estatutário - Prorrogação   |
| PRO_MOE_Reducao | Número de pedidos de Redução de Atividade para Membro de Orgão Estatutário - Prorrogação |
| PRO_MOE_Total | Número total de pedidos para Membro de Orgão Estatutário - Prorrogação |

#### Redução de Atividade por Distrito, valor acumulado para cada Mês - `reducao_atividade_porDistrito_porMes.csv` :
| Coluna | Descrição |
| --- | --- |
| Distritos | Distrito de Residência |
| Tipo | Colunas com o número total de pedidos para cada tipo de pedido: COVID_RED_TI (Trabalhador Independente), COVID_PRO_RED_TI (Trabalhador Independente - Prorrogação), COVID_RED_MOE (Membro de Orgão Estatutário), COVID_PRO_RED_TI (Membro de Orgão Estatutário - Prorrogação)  |
| Month | Colunas com o número total de pedidos em cada mês dado o tipo de pedido. Para cada tipo aparecem apenas os meses para os quais existem contagens |

#### Redução de Atividade por Distrito, valor acumulado Total- `reducao_atividade_porDistrito_Total.csv` :
| Coluna | Descrição |
| --- | --- |
| Distritos | Distrito de residência |
| PRO_MOE | Número total de pedidos para Membro de Orgão Estatutário - Prorrogação |
| PRO_TI | Número total de pedidos para Trabalhador Independente - Prorrogação |
| MOE | Número total de pedidos para Membro de Orgão Estatutário  |
| TI | Número total de pedidos para Trabalhador Independente |

#### Redução de Atividade por Distrito, Dados Totais Históricos `reducao_atividade_bydistrict_historicalData.csv` :
| Coluna | Descrição |
| --- | --- |
| Distritos | Distrito de residência |
| Tipo | Tipo de pedido ((Trabalhador Independente, Trabalhador Independente - Prorrogação, Membro de Orgão Estatutário, Membro de Orgão Estatutário - Prorrogação))|
| Datas | As restantes colunas contêm o número total de pedidos por tipo e por distrito para a respetiva data|

#### Redução de Atividade por Sexo- `reducao_atividade_porSexo.csv` :
| Coluna | Descrição |
| --- | --- |
| TipoPedido | Tipo de pedido |
| Total | Número total de trabalhadores |
| Feminino | Número de trabalhadores do sexo feminino |
| Masculino | Número de trabalhadores do sexo masculino |

#### Redução de Atividade por Sexo, Dados Históricos `reducao_atividade_bysex_historicalData.csv` :
| Coluna | Descrição |
| --- | --- |
| TipoPedido | Tipo de pedido |
| Sexo | Sexo do trabalhador (feminino ou masculino) |
| Datas | As restantes colunas contêm o número total de pedidos por tipo e por sexo para a respetiva data|



## Despedimentos Coletivos

#### Despedimentos Coletivos por Dia - `despedimentos_coletivos.csv` :
| Coluna | Descrição |
| --- | --- |
| DATA | Data de iniciação dos processos |
| COLETIVOS_TOTAL | Número total de processos de despedimento coletivo iniciados - valores acumulados com contagem reiniciada em cada mês  |
| COLETIVOS_MICRO | Número de processos de despedimento coletivo iniciados em Microempresas  (1 a 9 trabalhadores) - valores acumulados com contagem reiniciada em cada mês  |
| TRABALHADORES_TOTAL | Número total de trabalhadores a despedir - valores acumulados com contagem reiniciada em cada mês  |
| TRABALHADORES_MICRO | Número de trabalhadores a despedir em Microempresas  (1 a 9 trabalhadores) - valores acumulados com contagem reiniciada em cada mês  |
