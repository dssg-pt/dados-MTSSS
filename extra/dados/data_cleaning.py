#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import dateparser
import numpy as np
from datetime import date


### Nº de Baixas Por Isolamento
def baixas_all_data():
    df_baixas = pd.read_csv('original_files/Baixas por Isolamento.csv')
    #Select the relevant information, deleting the first 8 rows
    df_baixas = df_baixas.iloc[6:]
    baixas = df_baixas[df_baixas.columns[:3]]
    #Reset indexes
    baixas.reset_index(drop=True, inplace=True)
    #Get indexes that separate tables
    b = np.concatenate(( [True], pd.isnull(baixas.iloc[:,0]), [True] )) 
    indexes = np.flatnonzero(b[1:] != b[:-1]) 
    baixas_all = baixas[indexes[0]:indexes[1]]
    #dropping rows with nan values
    baixas_all.dropna(inplace=True)
    #renaming the columns
    baixas_all.columns = ['DATA', 'POR DIA', 'ACUMULADOS']
    #fomatting the date 
    baixas_all['DATA'] = baixas_all['DATA'].apply(dateparser.parse)
    baixas_all.to_csv(r'dataframes/baixas_all.csv', index = False)
    return baixas_all

def baixas_distrito_data():
    df_baixas = pd.read_csv('original_files/Baixas por Isolamento.csv')
    #Select the relevant information, deleting the first 8 rows
    df_baixas = df_baixas.iloc[6:]
    baixas = df_baixas[df_baixas.columns[:3]]
    #Reset indexes
    baixas.reset_index(drop=True, inplace=True)
    #Get indexes that separate tables
    b = np.concatenate(( [True], pd.isnull(baixas.iloc[:,0]), [True] )) 
    indexes = np.flatnonzero(b[1:] != b[:-1]) 
    baixas_distrito = baixas[indexes[4]:indexes[5]]
    #dropping rows with nan values
    baixas_distrito.dropna(axis=1, how='any', inplace=True)
    #renaming the columnsS']
    baixas_distrito.columns = ['DISTRITO', 'TOTAL']
    baixas_distrito.to_csv(r'dataframes/baixas_distrito.csv', index = False)
    return baixas_distrito


### Lay Off - Estimativa
def layoff_data():
    df_layoff = pd.read_csv('original_files/Layoff – Estimativa .csv')
    df_layoff.dropna(axis=0, how='any', inplace=True)
    df_layoff.columns = ['DATA', 'Nº NISS_EE', 'Nº TRABALHADORES', 
                            'REMUNERAÇÕES DECLARADAS']
    df_layoff.drop(['Nº NISS_EE'], axis=1, inplace=True) 
    df_layoff['DATA'] = df_layoff['DATA'].apply(lambda x: x.split(' ')[0])
    df_layoff['DATA'] = df_layoff['DATA'].apply(lambda x: x.replace('/', '-'))
    df_layoff['DATA'] = df_layoff['DATA'].apply(lambda x: x.split('-'))
    df_layoff['month'] = df_layoff['DATA'].apply(lambda x: x[1])
    df_layoff['day'] = df_layoff['DATA'].apply(lambda x: x[2] if len(x[0]) > 2 else x[0])
    df_layoff['year'] = df_layoff['DATA'].apply(lambda x: x[0] if len(x[0]) > 2 else x[2])
    df_layoff['DATA'] = pd.to_datetime(df_layoff[['day', 'month', 'year']])
    df_layoff.drop(['month', 'day', 'year'], axis=1, inplace=True) 
    df_layoff['DATA'] = df_layoff['DATA'].mask(df_layoff['DATA'].dt.year == 2021, 
                             df_layoff['DATA'] + pd.offsets.DateOffset(year=2020))
    df_layoff.to_csv(r'dataframes/df_layoff.csv', index = False)
    return df_layoff

### LayOff - Amount of companies on layoff by Sector and by Date
def historic_layoff_CompaniesAmount_bySector(): 
    data1 = pd.read_csv('original_files/historical_data_company.csv')
    data2 = pd.read_csv('original_files/Layoff – Estim. - CAE,Dim,Dist.csv')
    #Select the relevant information, deleting the first 8 rows
    df=data2.iloc[8:]
    #import today´s date
    today=date.today()
    #Select the columns that are relevant to work sectors
    df_work=df[df.columns[0:3]]
    df_work=df_work.iloc[2:23]
    #Rename columns for data cleaning
    df_work=df_work.rename(columns={'EEs QUE ENTREGARAM DOCUMENTO - COVID19 - Layoff Simplificado':'Index','Unnamed: 1':'Setor',
                       'Unnamed: 2':today,'Unnamed: 3':'Nº TRABALHADORES','Unnamed: 4':'Feminino','Unnamed: 5':'Masculino'})
    #Drop columns for data cleaning
    df_work=df_work.drop(['Index'],axis=1)
    data1=data1.drop(['Unnamed: 0'],axis=1)
    #Merge historical data with last report
    new_historical=pd.merge(left=data1, right=df_work, left_on='Setor', right_on='Setor')
    new_historical=new_historical.sort_values(by=[today],ascending=False)
    #Save new data as historical data
    new_historical.to_csv('original_files/historical_data_company.csv')
    return new_historical               


### Layoff - People amount by Sector and by Date
def historic_layoff_PeopleAmount_bySector():
    data3 = pd.read_csv('original_files/historical_data_person.csv')
    data4 = pd.read_csv('original_files/Layoff – Estim. - CAE,Dim,Dist.csv')
    #Select the relevant information, deleting the first 8 rows
    df=data4.iloc[8:]
    #import today´s date
    today=date.today()
    #Select the columns that are relevant to work sectors
    df_work=df[df.columns[0:4]]
    df_work=df_work.iloc[2:23]
    #Rename columns
    df_work=df_work.rename(columns={'EEs QUE ENTREGARAM DOCUMENTO - COVID19 - Layoff Simplificado':'Index','Unnamed: 1':'Setor',
                       'Unnamed: 2':'Nº NISS_EE','Unnamed: 3':today,'Unnamed: 4':'Feminino','Unnamed: 5':'Masculino'})
    #Drop columns for data cleaning
    df_work=df_work.drop(['Index','Nº NISS_EE'],axis=1)
    data3=data3.drop(['Unnamed: 0'],axis=1)
    #merge historical data with new data
    new_historical = pd.merge(left=data3, right=df_work, left_on='Setor', right_on='Setor')
    new_historical=new_historical.sort_values(by=[today],ascending=False)
    #Save new data as historical data
    new_historical.to_csv('original_files/historical_data_person.csv')
    return new_historical

### Layoff - by organization dimension and by date
def layoff_organization_dimension():
    data5 = pd.read_csv('original_files/historical_data_company_size.csv')
    data5=data5.drop(['Unnamed: 0'],axis=1)
    data6 = pd.read_csv('original_files/Layoff – Estim. - CAE,Dim,Dist.csv')
    #Create new dataset
    df=data6 
    # Search for row and column position of desired data
    i, c = np.where(df == 'até 10 trabalhadores')
    e, d=np.where(df=='>= 250 trabalhadores')
    #Create names for data range, for easier identification
    row_size=i+2
    col1=(c+1)
    col2=(d+1)
    #Splice the data with the selected rows found on the previous step
    df2=df.iloc[int(i):int(row_size),int(c):int(col2)]
    #perform some data cleaning
    df2=df2.reset_index()
    df2=df2.drop('index',1)
    df2.columns=df2.iloc[0]
    df2=df2.drop([0])
    #transpose the data to match the axis of the historical data
    df2=df2.transpose()
    df2=df2.reset_index()
    #import today´s date
    today=date.today()
    #Rearrange column names
    df2.columns=['TOTAL',today]
    new_historical = pd.merge(left=data5, right=df2, left_on='TOTAL', right_on='TOTAL')
    new_historical=new_historical.sort_values(by=[today],ascending=False)
    new_historical.to_csv('original_files/historical_data_company_size.csv')
    return new_historical


### Layoff - by District
def layoff_region_data():
    #Select new dataset
    data4 = pd.read_csv('original_files/Layoff – Estim. - CAE,Dim,Dist.csv')
    df=data4
    #Drop all set of row and columns that are filled with NaN
    df.dropna(axis=0, how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    #Delete the first rows that don't present any important information
    df=df.iloc[9:]
    #Search for the relevant information that presents the region information, and store the column number
    lower=df.columns.get_loc("EEs QUE ENTREGARAM DOCUMENTO - COVID19 - Layoff Simplificado.1")
    #Select the upper range of columns with relevant data
    upper=lower+3
    #filter the data with the selected parameters
    df_region=df.iloc[:,lower:upper]
    #rename columns and do some data cleaning
    df_region=df_region.rename(columns={'EEs QUE ENTREGARAM DOCUMENTO - COVID19 - Layoff Simplificado.1':'Region',
                                    'Unnamed: 8':'N° Empresas',
                       'Unnamed: 9':'Percentual(%)'})
    df_region['Region']=df_region['Region'].replace({'AVEIRO':'Aveiro','BEJA':'Beja','BRAGA':'Braga','BRAGANÇA':'Bragança',
                                                 'CASTELO BRANCO':'Castelo Branco','COIMBRA':'Coimbra','ÉVORA':'Évora',
                                                 'FARO':'Faro','GUARDA':'Guarda','LEIRIA':'Leiria','LISBOA':'Lisboa',
                                                 'PORTALEGRE':'Portalegre','PORTO':'Porto','SANTARÉM':'Santarém',
                                                 'SETÚBAL':'Setúbal','VIANA DO CASTELO':'Viana do Castelo',
                                                 'VILA REAL':'Vila Real','VISEU':'Viseu','R.A.AÇORES':'R.A.Açores',
                                                 'R.A.MADEIRA':'R.A.Madeira'})
    df_region['Percentual(%)']=df_region['Percentual(%)']*100
    df_region=df_region.reset_index()
    df_region=df_region.drop('index',1)
    df_region.dropna(axis=0, how='any', inplace=True)
    df_region.to_csv(r'dataframes/organization_region.csv', index = False)
    return df_region


#### Redução de atividade por Dia
def reducao_atividade_byday():
    
    reducao_atividade=pd.read_csv('original_files/Redução de Actividade TI e MOE.csv')
    # Drop rows with no info
    reducao_atividade.dropna(how='all',inplace=True)
    # Reset indexes
    reducao_atividade.reset_index(drop=True, inplace=True)
    # Get indexes that separate tables
    m = np.concatenate(( [True], reducao_atividade.iloc[:,1:13].isna().all(axis=1), [True] )) 
    indexes = np.flatnonzero(m[1:] != m[:-1])
    # Separate tables
    red_byday = reducao_atividade[indexes[0]+2:indexes[1]]
    
    # Clean byday table 
    red_byday=red_byday.dropna(axis=1,how='all')
    red_byday.columns = ['DATA', 'TI_ParagemTotal', 'TI_Reducao','TI_Total', 'PRO_TI_ParagemTotal', 'PRO_TI_Reducao','PRO_TI_Total', 'MOE_ParagemTotal', 'MOE_Reducao','MOE_Total', 'PRO_MOE_ParagemTotal', 'PRO_MOE_Reducao','PRO_MOE_Total']

    # Formatting the date - sometimes some values are already of data type
#     date_inds=pd.notnull(pd.to_datetime(red_byday['DATA'],errors='coerce'))
#     if date_inds.index[date_inds].size > 0:
#         red_byday['DATA'][date_inds]=red_byday['DATA'][date_inds].dt.strftime('%d/%b')
    red_byday['DATA'] = red_byday['DATA'].apply(dateparser.parse,date_formats=['%d/%b'])

    # Remove columns that dont have datetype in DATA, for example columns with the TOTAL
    red_byday.dropna(subset=['DATA'],inplace=True)
    # Reset indexes
    red_byday.reset_index(drop=True, inplace=True)

    # Save csv
    red_byday.to_csv(r'dataframes/reducao_atividade_porDia.csv', index = False)
  

#### Redução de atividade por Distrito
def reducao_atividade_bydistrict():
    
    reducao_atividade=pd.read_csv('original_files/Redução de Actividade TI e MOE.csv')
    # Drop rows with no info
    reducao_atividade.dropna(how='all',inplace=True)
    # Reset indexes
    reducao_atividade.reset_index(drop=True, inplace=True)
    # Get indexes that separate tables
    m = np.concatenate(( [True], reducao_atividade.iloc[:,1:13].isna().all(axis=1), [True] )) 
    indexes = np.flatnonzero(m[1:] != m[:-1])
    # Separate tables
    red_bydistrict = reducao_atividade[indexes[2]:indexes[3]]
    
    red_bydistrict_months=red_bydistrict
    # Clean bydistrict table 
    red_bydistrict_months.reset_index(drop=True, inplace=True)
    red_bydistrict_months=red_bydistrict_months.set_index(red_bydistrict_months.columns.values[0])
    red_bydistrict_months.index.name='Distritos'
    # Find columns corresponding to the total counts
    checknull_months=red_bydistrict_months.iloc[1].notnull() 
    checktotal_months=red_bydistrict_months.iloc[1].str.lower()!='total'
    checknull_title=red_bydistrict_months.iloc[0].notnull()
    # Generate multi level columns
    col_indexes=np.nonzero(checknull_title.array)
    col_indexes=col_indexes[0]
    columns=[]
    for j in range(4):
        if j<3: 
            max_range=col_indexes[j+1]
        else:
            max_range=red_bydistrict_months.shape[1]
        for i in range(col_indexes[j],max_range):
            columns.append((red_bydistrict_months.iloc[0,col_indexes[j]],red_bydistrict_months.iloc[1,i]))
    red_bydistrict_months.columns = pd.MultiIndex.from_tuples(columns,names=['Type', 'Month'])
    # Get columns concerning each month
    red_bydistrict_months=red_bydistrict_months.iloc[2:, checknull_months.array & checktotal_months.array]
    
    # Create dataframe with total counts for each district
    red_bydistrict_total=red_bydistrict_months.groupby(level=['Type'],axis=1).sum()
    red_bydistrict_total.columns=['PRO_MOE','PRO_TI','MOE','TI']

    # Save csvs (per month and total)
    red_bydistrict_months.to_csv(r'dataframes/reducao_atividade_porDistrito_porMes.csv')
    red_bydistrict_total.to_csv(r'dataframes/reducao_atividade_porDistrito_Total.csv')
    
    ## APPEND TO HISTORICAL DATA
    # Transform columns into indexes
    df_aux=red_bydistrict_total.stack().to_frame()
    # Change columns to the file's date
    df_aux.columns=[date.today()]

    # Import dataframe with historical data
    red_bydistrict_historical=pd.read_csv('dataframes/reducao_atividade_bydistrict_historicalData.csv',index_col=[0,1])
    # Append to dataframe with historical data for reducao de atividade por distrito
    red_bydistrict_historical=pd.concat([red_bydistrict_historical,df_aux],axis=1,join='outer')
    red_bydistrict_historical.to_csv('dataframes/reducao_atividade_bydistrict_historicalData.csv')


#### Redução de atividade por Sexo
def reducao_atividade_bysex():
    
    reducao_atividade=pd.read_csv('original_files/Redução de Actividade TI e MOE.csv')
    # Drop rows with no info
    reducao_atividade.dropna(how='all',inplace=True)
    # Reset indexes
    reducao_atividade.reset_index(drop=True, inplace=True)
    # Get indexes that separate tables
    m = np.concatenate(( [True], reducao_atividade.iloc[:,1:13].isna().all(axis=1), [True] )) 
    indexes = np.flatnonzero(m[1:] != m[:-1])
    # Separate tables
    red_bysex = reducao_atividade[indexes[4]+2:indexes[5]]
    
    # Clean bysex table 
    red_bysex=red_bysex.dropna(axis=1)
    red_bysex.columns=['TipoPedido','Total','Feminino','Masculino']
    if len(red_bysex.iloc[:,0])==3:
        red_bysex.iloc[:,0]=['Trabalhador Independente','Prorrogação Trabalhador Independente','Membro Orgão Estatutário']
    elif len(red_bysex.iloc[:,0])==4:
        red_bysex.iloc[:,0]=['Trabalhador Independente','Prorrogação Trabalhador Independente','Membro Orgão Estatutário','Prorrogação Membro Orgão Estatutário']
    red_bysex.reset_index(drop=True, inplace=True)

    # Save csv
    red_bysex.to_csv(r'dataframes/reducao_atividade_porSexo.csv', index = False)
    
    ## APPEND TO HISTORICAL DATA
    # Transform columns into indexes
    red_bysex_new=red_bysex.set_index('TipoPedido').stack().to_frame()
    # Change columns to the file's date
    red_bysex_new.columns=[date.today()]

    # Import dataframe with historical data
    red_bysex_historical=pd.read_csv('dataframes/reducao_atividade_bysex_historicalData.csv',index_col=[0,1])
    # # Append to dataframe with historical data for reducao de atividade por sexo
    red_bysex_historical=pd.concat([red_bysex_historical,red_bysex_new],axis=1,join='outer')
    red_bysex_historical.to_csv('dataframes/reducao_atividade_bysex_historicalData.csv')


### Despedimentos coletivos
def despedimentos_coletivos():
    despedimentos=pd.read_csv('original_files/Despedimentos coletivos.csv')
    # Drop first column which is empty
    despedimentos=despedimentos.drop(despedimentos.columns[0],axis=1)
    # Drop rows with nan
    despedimentos.dropna(inplace=True)
    despedimentos.reset_index(drop=True, inplace=True)
    # Rename columns
    despedimentos.columns = ['DATA', 'COLETIVOS_TOTAL', 'COLETIVOS_MICRO','TRABALHADORES_TOTAL', 'TRABALHADORES_MICRO']
    # Save csv
    despedimentos.to_csv(r'dataframes/despedimentos_coletivos.csv', index = False)


if __name__ == '__main__':
    
    df_baixas_all=baixas_all_data()
    df_baixas_distrito=baixas_distrito_data()
    df_layoff=layoff_data()
    historical_data_company=historic_layoff_CompaniesAmount_bySector()
    historical_data_person=historic_layoff_PeopleAmount_bySector()
    historical_data_company_size=layoff_organization_dimension()
    layoff_region=layoff_region_data()
    reducao_atividade_byday()
    reducao_atividade_bydistrict()
    reducao_atividade_bysex()
    despedimentos_coletivos()