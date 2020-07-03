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

Tratamento dos dados relevantes para o estudo, nomeadamente:
- Baixas por Isolamento por data de entrada (`baixas_all.csv`);
- Baixas por Isolamento por distrito (`baixas_distrito.csv`);
- Layoff ao longo do tempo (`df_layoff.csv`) : informação relativa às Entidades Empregadoras (EE) que entregaram documentos;
- Layoff por Código de Atividade Económica/ Setor;
- Layoff por sexo;
- Layoff por distrito e dimensão da empresa; 
- Redução de atividade por data de registo dos pedidos (`reducao_atividade_porDia.csv`);
- Redução de atividade por distrito de residência (`reducao_atividade_porDistrito_Total.csv`, `reducao_atividade_porDistrito_porMes.csv` e `reducao_atividade_bydistrict_historicaData.csv`);
- Redução de atividade por sexo (`reducao_atividade_porSexo.csv` e `reducao_atividade_bysex_historicaData.csv`);
- Despedimentos Coletivos (`despedimentos_coletivos.csv`). 

Guarda os dados tratados (ficheiros .csv mencionados acima) em `dataframes/`.

## Dicionário de Dados
