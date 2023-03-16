import pandas as pd
import os

if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)

else:
    data_structure = {
        'Valor':[],
        'Efetuado':[],
        'Fixo':[],
        'Data':[],
        'Categoria':[],
        'Descrição':[]        
    }
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_receitas.to_csv("df_receitas.csv",sep=';')
    df_despesas.to_csv("df_despesas.csv",sep=';')


if ("df_cat_despesas.csv" in os.listdir()) and ("df_cat_receitas.csv" in os.listdir()):
    df_cat_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_cat_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
    cat_receita = df_cat_receitas.values.tolist()
    cat_despesa = df_cat_despesas.values.tolist()


else:
    cat_receita = {'Categoria':["Salário","Investimento","Comissão"]}
    cat_despesa = {'Categoria':["Alimentação","Aluguel","Gasolina","Saúde","Lazer","Viagem"]}
    df_cat_receitas = pd.DataFrame(cat_receita)
    df_cat_despesas = pd.DataFrame(cat_despesa)
    df_cat_receitas.to_csv("df_cat_receitas.csv",sep=';')
    df_cat_despesas.to_csv("df_cat_despesas.csv",sep=';')