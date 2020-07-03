## Conteúdo

O repositório contém:
- `original_files/`: Dados extraídos diretamente do MTSSS;
- `dataframes/`: Dados obtidos após tratamento;
- `data_extraction.ipynb`: notebook Python que extrai os últimos dados (ficheiro .xlsx) em [MTSSS](http://www.gep.mtsss.gov.pt/indicadores-covid-19-mtsss) e os guarda em formato .csv (divididos em categorias) no diretório `original_files/`;
- `data_extraction.py`: semelhante ao anterior mas em formato .py;
- `data_cleaning.ipynb`: notebook Python que trata e limpa os dados em `original_files/`, atualizando-os no diretório `dataframes/`;
- `data_analysis.ipynb`: notebook Python que trata da análise visual dos dados em `dataframes/`.

## Extracão de Dados

- Extrai o último ficheiro do [MTSSS](http://www.gep.mtsss.gov.pt/indicadores-covid-19-mtsss)
- Guarda todas as worksheets do ficheiro .xlsx separadamente em `original_files/`

## Tratamento de Dados

Dados considerados relevantes para o estudo, juntamente com alguns detalhes/assumptions tomados no seu tratamento:
- Baixas por Isolamento por data de entrada (`baixas_all.csv`);
- Baixas por Isolamento por distrito (`baixas_distrito.csv`);
- Layoff ao longo do tempo (`df_layoff.csv`) : informação relativa às Entidades Empregadoras (EE) que entregaram documentos;
- Layoff por Código de Atividade Económica/ Setor;
- Layoff por sexo;
- Layoff por distrito e dimensão da empresa; 
- Redução de atividade por data de registo dos pedidos (`reducao_atividade_porDia.csv`): 
  - A divisão das várias tabelas na worksheet de Redução de Atividade é obtida através da identificação das linhas que possuem todos as colunas em branco (excepto a primeira);
  - Nesta tabela são apenas mantidas as linhas com formato de data na primeira coluna de forma a remover as linhas com o total, uma vez que a existência destas não é consistente ao longo dos vários ficheiros publicados;
- Redução de atividade por distrito de residência (`reducao_atividade_porDistrito_Total.csv`, `reducao_atividade_porDistrito_porMes.csv` e `reducao_atividade_bydistrict_historicaData.csv`): 
  - Dado que não existe consistência nas colunas com o total de pedidos (por vezes são publicados ficheiros sem total ou com o total apenas para certos tipos de pedidos), começa-se por criar um .csv com os dados por mês para cada tipo (removendo as colunas sem identificação ou identificadas como total);
  - Depois é criado um .csv com os totais, obtidos a partir da soma para todos os meses;
- Redução de atividade por sexo (`reducao_atividade_porSexo.csv` e `reducao_atividade_bysex_historicaData.csv`);
- Despedimentos Coletivos (`despedimentos_coletivos.csv`). 

Guarda os dados tratados (ficheiros .csv mencionados acima) em `dataframes/`.

## Dicionário de Dados

Redução de Atividade por Dia - `reducao_atividade_porDia.csv` :
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

Redução de Atividade por Distrito, por Mês - `reducao_atividade_porDistrito_porMes.csv` :
| Coluna | Descrição |
| --- | --- |
| Distritos | Distrito de Residência |
| Tipo | Colunas com o número total de pedidos para cada tipo de pedido: COVID_RED_TI (Trabalhador Independente), COVID_PRO_RED_TI (Trabalhador Independente - Prorrogação), COVID_RED_MOE (Membro de Orgão Estatutário), COVID_PRO_RED_TI (Membro de Orgão Estatutário - Prorrogação)  |
| Month | Colunas com o número total de pedidos em cada mês dado o tipo de pedido. Para cada tipo aparecem apenas os meses para os quais existem contagens |

Redução de Atividade por Distrito, Total- `reducao_atividade_porDistrito_Total.csv` :
| Coluna | Descrição |
| --- | --- |
| Distritos | Distrito de residência |
| PRO_MOE | Número total de pedidos para Membro de Orgão Estatutário - Prorrogação |
| PRO_TI | Número total de pedidos para Trabalhador Independente - Prorrogação |
| MOE | Número total de pedidos para Membro de Orgão Estatutário  |
| TI | Número total de pedidos para Trabalhador Independente |

Redução de Atividade por Distrito, Dados Totais Históricos `reducao_atividade_bydistrict_historicalData.csv` :
| Coluna | Descrição |
| --- | --- |
| Distritos | Distrito de residência |
| Tipo | Tipo de pedido ((Trabalhador Independente, Trabalhador Independente - Prorrogação, Membro de Orgão Estatutário, Membro de Orgão Estatutário - Prorrogação))|
| Datas | As restantes colunas contêm o número total de pedidos por tipo e por distrito para a respetiva data|

Redução de Atividade por Sexo- `reducao_atividade_porSexo.csv` :
| Coluna | Descrição |
| --- | --- |
| TipoPedido | Tipo de pedido |
| Total | Número total de trabalhadores |
| Feminino | Número de trabalhadores do sexo feminino |
| Masculino | Número de trabalhadores do sexo masculino |

Redução de Atividade por Sexo, Dados Históricos `reducao_atividade_bysex_historicalData.csv` :
| Coluna | Descrição |
| --- | --- |
| TipoPedido | Tipo de pedido |
| Sexo | Sexo do trabalhador (feminino ou masculino) |
| Datas | As restantes colunas contêm o número total de pedidos por tipo e por sexo para a respetiva data|

Despedimentos Coletivos - `despedimentos_coletivos.csv` :
| Coluna | Descrição |
| --- | --- |
| DATA | Data de iniciação dos processos |
| COLETIVOS_TOTAL | Número total de processos de despedimento coletivo iniciados - valores acumulados com contagem reiniciada em cada mês  |
| COLETIVOS_MICRO | Número de processos de despedimento coletivo iniciados em Microempresas  (1 a 9 trabalhadores) - valores acumulados com contagem reiniciada em cada mês  |
| TRABALHADORES_TOTAL | Número total de trabalhadores a despedir - valores acumulados com contagem reiniciada em cada mês  |
| TRABALHADORES_MICRO | Número de trabalhadores a despedir em Microempresas  (1 a 9 trabalhadores) - valores acumulados com contagem reiniciada em cada mês  |
