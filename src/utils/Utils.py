class Utils:
    def __init__(self, df):
        self.df = df

    def column_type_converter(self, column_name, type):
        self.df[column_name] = self.df[column_name].astype(type) 