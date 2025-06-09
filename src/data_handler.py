class Data_handler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_csv(self, sep=';', encoding='latin1', skiprows=0):
        import pandas as pd
        self.df = pd.read_csv(self.file_path, sep=sep, encoding=encoding, skiprows=skiprows) 
        return self.df
    
    def clean_data(self):
        self.df = self.df.dropna(how='all')
        self.df.columns = self.df.columns.str.strip()
        return self.df

    def get_dataframe(self):
        return self.df
    
    def gini_df_to_long(self, df):
        df_long = df.melt(
        id_vars=["Sigla", "CÃ³digo", "Estado"],
        value_vars=[str(ano) for ano in range(2012, 2023)],
        var_name="Ano",
        value_name="Gini"
        )
        return df_long
        
