import pandas as pd

class Utils:
    def __init__(self):
        self.df = None

    def column_type_converter(self, df, column_name, type):
        self.df = df 
        self.df[column_name] = self.df[column_name].astype(type)

    def merge_dataframes(self, df_gini, df_mv):
        df_combined = pd.merge(df_gini[['UF', 'ano', 'Gini']], df_mv[['UF', 'ano', 'valor']], on=['UF', 'ano'])
        return df_combined