import matplotlib.pyplot as plt

class PlotGenerator:
    def __init__(self, df):
        self.df = df

    def plot_gini_over_time_by_state(self, UF_list):
        plt.figure(figsize=(10, 5))

        for state in UF_list:
            df_state = self.df[self.df['UF'] == state]
            plt.plot(df_state["ano"], df_state["Gini"], marker='o', label=state)

        plt.title(f"Índice de Gini ao longo dos anos - {', '.join(UF_list)}")
        plt.xlabel("Ano")
        plt.ylabel("Índice de Gini")
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def plot_violence_over_time_by_state(self, UF_list):
        plt.figure(figsize=(12, 8))

        for state in UF_list:   
            df_state = self.df[self.df['UF'] == state]
            plt.plot(df_state['ano'], df_state['valor'], label=state, marker='o')
        
        plt.title(f"Mortes violência ao longo dos anos - {', '.join(UF_list)}")
        plt.xlabel("Ano")
        plt.ylabel("Valor")
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    