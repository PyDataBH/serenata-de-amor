import shutil
import pandas as pd
import numpy as np
import os
import urllib
import zipfile
import glob



FILENAME_PREFIX='consulta_cand_'
TEMP_PATH = '../data/tse_temp'
TSE_CANDIDATES_URL='http://agencia.tse.jus.br/estatistica/sead/odsele/consulta_cand/'
OUTPUT_DATASET_PATH = '../data/2017-03-31-tse-candidates.xz'
os.makedirs(TEMP_PATH)

# setting year range from 2004 to 2016. this will be modified further to 'from 1994 to 2016'
year_list=[str(year) for year in (range(2004,2017,2))]

# Download files
for year in year_list:
    filename=FILENAME_PREFIX+year+'.zip'
    file_url=TSE_CANDIDATES_URL+filename
    output_file=os.path.join(TEMP_PATH,filename)
    urllib.request.urlretrieve(file_url,output_file)

# Unzip downloaded files
for year in year_list:
    filename=FILENAME_PREFIX+year+'.zip'
    filepath=os.path.join(TEMP_PATH,filename)
    zip_ref = zipfile.ZipFile(filepath, 'r')
    zip_ref.extractall(TEMP_PATH)
    zip_ref.close()


# ### Adding the headers
# The following headers were extracted from LEIAME.pdf in consulta_cand_2016.zip.
header_consulta_cand_till2010=[
    "DATA_GERACAO",#
    "HORA_GERACAO",#
    "ANO_ELEICAO",#
    "NUM_TURNO",# (*)
    "DESCRICAO_ELEICAO",# (*)
    "SIGLA_UF",#
    "SIGLA_UE",# (*)
    "DESCRICAO_UE",#
    "CODIGO_CARGO",# (*)
    "DESCRICAO_CARGO",#
    "NOME_CANDIDATO",#
    "SEQUENCIAL_CANDIDATO",# (*)
    "NUMERO_CANDIDATO",#
    "CPF_CANDIDATO",#
    "NOME_URNA_CANDIDATO",#
    "COD_SITUACAO_CANDIDATURA",#
    "DES_SITUACAO_CANDIDATURA",#
    "NUMERO_PARTIDO",#
    "SIGLA_PARTIDO",#
    "NOME_PARTIDO",#
    "CODIGO_LEGENDA",#
    "SIGLA_LEGENDA",#
    "COMPOSICAO_LEGENDA",#
    "NOME_LEGENDA",#
    "CODIGO_OCUPACAO",#
    "DESCRICAO_OCUPACAO",#
    "DATA_NASCIMENTO",#
    "NUM_TITULO_ELEITORAL_CANDIDATO",# 
    "IDADE_DATA_ELEICAO",#
    "CODIGO_SEXO",#
    "DESCRICAO_SEXO",#
    "COD_GRAU_INSTRUCAO",#
    "DESCRICAO_GRAU_INSTRUCAO",#
    "CODIGO_ESTADO_CIVIL",#
    "DESCRICAO_ESTADO_CIVIL",#
    "CODIGO_NACIONALIDADE",#
    "DESCRICAO_NACIONALIDADE",#
    "SIGLA_UF_NASCIMENTO",#
    "CODIGO_MUNICIPIO_NASCIMENTO",#
    "NOME_MUNICIPIO_NASCIMENTO",#
    "DESPESA_MAX_CAMPANHA",#
    "COD_SIT_TOT_TURNO",#
    "DESC_SIT_TOT_TURNO",#
]

header_consulta_cand_at2012=[
    "DATA_GERACAO",#
    "HORA_GERACAO",#
    "ANO_ELEICAO",#
    "NUM_TURNO",# (*)
    "DESCRICAO_ELEICAO",# (*)
    "SIGLA_UF",#
    "SIGLA_UE",# (*)
    "DESCRICAO_UE",#
    "CODIGO_CARGO",# (*)
    "DESCRICAO_CARGO",#
    "NOME_CANDIDATO",#
    "SEQUENCIAL_CANDIDATO",# (*)
    "NUMERO_CANDIDATO",#
    "CPF_CANDIDATO",#
    "NOME_URNA_CANDIDATO",#
    "COD_SITUACAO_CANDIDATURA",#
    "DES_SITUACAO_CANDIDATURA",#
    "NUMERO_PARTIDO",#
    "SIGLA_PARTIDO",#
    "NOME_PARTIDO",#
    "CODIGO_LEGENDA",#
    "SIGLA_LEGENDA",#
    "COMPOSICAO_LEGENDA",#
    "NOME_LEGENDA",#
    "CODIGO_OCUPACAO",#
    "DESCRICAO_OCUPACAO",#
    "DATA_NASCIMENTO",#
    "NUM_TITULO_ELEITORAL_CANDIDATO",#
    "IDADE_DATA_ELEICAO",#
    "CODIGO_SEXO",#
    "DESCRICAO_SEXO",#
    "COD_GRAU_INSTRUCAO",#
    "DESCRICAO_GRAU_INSTRUCAO",#
    "CODIGO_ESTADO_CIVIL",#
    "DESCRICAO_ESTADO_CIVIL",#
    "CODIGO_NACIONALIDADE",#
    "DESCRICAO_NACIONALIDADE",#
    "SIGLA_UF_NASCIMENTO",#
    "CODIGO_MUNICIPIO_NASCIMENTO",#
    "NOME_MUNICIPIO_NASCIMENTO",#
    "DESPESA_MAX_CAMPANHA",#
    "COD_SIT_TOT_TURNO",#
    "DESC_SIT_TOT_TURNO",#
    "NM_EMAIL",#
]

header_consulta_cand_from2014=[
    "DATA_GERACAO", 
    "HORA_GERACAO",
    "ANO_ELEICAO",
    "NUM_TURNO",# (*)
    "DESCRICAO_ELEICAO",# (*)
    "SIGLA_UF",
    "SIGLA_UE",# (*)
    "DESCRICAO_UE",
    "CODIGO_CARGO",# (*)
    "DESCRICAO_CARGO",
    "NOME_CANDIDATO",
    "SEQUENCIAL_CANDIDATO",# (*)
    "NUMERO_CANDIDATO",
    "CPF_CANDIDATO",
    "NOME_URNA_CANDIDATO",
    "COD_SITUACAO_CANDIDATURA",
    "DES_SITUACAO_CANDIDATURA",
    "NUMERO_PARTIDO",
    "SIGLA_PARTIDO",
    "NOME_PARTIDO",
    "CODIGO_LEGENDA",
    "SIGLA_LEGENDA",
    "COMPOSICAO_LEGENDA",
    "NOME_LEGENDA",
    "CODIGO_OCUPACAO",
    "DESCRICAO_OCUPACAO",
    "DATA_NASCIMENTO",
    "NUM_TITULO_ELEITORAL_CANDIDATO",
    "IDADE_DATA_ELEICAO",
    "CODIGO_SEXO",
    "DESCRICAO_SEXO",
    "COD_GRAU_INSTRUCAO",
    "DESCRICAO_GRAU_INSTRUCAO",
    "CODIGO_ESTADO_CIVIL",
    "DESCRICAO_ESTADO_CIVIL",
    "CODIGO_COR_RACA",
    "DESCRICAO_COR_RACA",
    "CODIGO_NACIONALIDADE",
    "DESCRICAO_NACIONALIDADE",
    "SIGLA_UF_NASCIMENTO",
    "CODIGO_MUNICIPIO_NASCIMENTO",
    "NOME_MUNICIPIO_NASCIMENTO",
    "DESPESA_MAX_CAMPANHA",
    "COD_SIT_TOT_TURNO",
    "DESC_SIT_TOT_TURNO",
    "NM_EMAIL",
]


sel_columns=[
# "DATA_GERACAO", 
# "HORA_GERACAO",
"ANO_ELEICAO",
"NUM_TURNO",# (*)
"DESCRICAO_ELEICAO",# (*)
"SIGLA_UF",
#"SIGLA_UE",# (*)
"DESCRICAO_UE",
# "CODIGO_CARGO",# (*)
"DESCRICAO_CARGO",
"NOME_CANDIDATO",
"SEQUENCIAL_CANDIDATO",# (*)
# "NUMERO_CANDIDATO",
"CPF_CANDIDATO",
# "NOME_URNA_CANDIDATO",
# "COD_SITUACAO_CANDIDATURA",
# "DES_SITUACAO_CANDIDATURA",
# "NUMERO_PARTIDO",
# "SIGLA_PARTIDO",
# "NOME_PARTIDO",
# "CODIGO_LEGENDA",
# "SIGLA_LEGENDA",
# "COMPOSICAO_LEGENDA",
# "NOME_LEGENDA",
# "CODIGO_OCUPACAO",
# "DESCRICAO_OCUPACAO",
# "DATA_NASCIMENTO",
"NUM_TITULO_ELEITORAL_CANDIDATO",
# "IDADE_DATA_ELEICAO",
# "CODIGO_SEXO",
# "DESCRICAO_SEXO",
# "COD_GRAU_INSTRUCAO",
# "DESCRICAO_GRAU_INSTRUCAO",
# "CODIGO_ESTADO_CIVIL",
# "DESCRICAO_ESTADO_CIVIL",
# "CODIGO_COR_RACA",
# "DESCRICAO_COR_RACA",
# "CODIGO_NACIONALIDADE",
# "DESCRICAO_NACIONALIDADE",
# "SIGLA_UF_NASCIMENTO",
# "CODIGO_MUNICIPIO_NASCIMENTO",
# "NOME_MUNICIPIO_NASCIMENTO",
# "DESPESA_MAX_CAMPANHA",
# "COD_SIT_TOT_TURNO",
"DESC_SIT_TOT_TURNO",
# "NM_EMAIL",
]


###Concatenate all files in one pandas dataframe
cand_df=pd.DataFrame()
for year in year_list:
    filesname=FILENAME_PREFIX+year+'*.txt'
    filespath=os.path.join(TEMP_PATH,filesname)
    files_of_the_year= sorted(glob.glob(filespath))
    for file_i in files_of_the_year:
        # the following cases do not take into account next elections. hopefully, TSE will add headers to the files
        if ('2014' in file_i) or ('2016' in file_i):
            cand_df_i=(pd.read_csv('./'+file_i,sep=';',header=None,dtype=str,names=header_consulta_cand_from2014,encoding='iso-8859-1'))
        elif ('2012' in file_i):
            cand_df_i=(pd.read_csv('./'+file_i,sep=';',header=None,dtype=str,names=header_consulta_cand_at2012,encoding='iso-8859-1'))
        else:
            cand_df_i=(pd.read_csv('./'+file_i,sep=';',header=None,dtype=str,names=header_consulta_cand_till2010,encoding='iso-8859-1'))
        cand_df=cand_df.append(cand_df_i[sel_columns])

cand_df.index=cand_df.reset_index().index # this index contains no useful information

# Exporting data
cand_df.to_csv(OUTPUT_DATASET_PATH,encoding='iso-8859-1',compression='xz',header=True,index=False)

# Removing temporary files
shutil.rmtree(TEMP_PATH)

