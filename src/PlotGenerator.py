import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

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

    def ratio_over_time_by_state(self, UF):
        df_state = self.df[self.df['UF'] == UF]
        
        fig, ax1 = plt.subplots(figsize=(12, 6))

        # Axis Y da left (Gini)
        color1 = 'blue'
        ax1.set_xlabel('Ano')
        ax1.set_ylabel('Índice de Gini')
        ax1.plot(df_state['ano'], df_state['Gini'], marker='o', color=color1, label='Gini')
        ax1.tick_params(axis='y', labelcolor=color1)

        ax1.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.2f}'))

        # Axis Y da Right (Valor)
        ax2 = ax1.twinx()
        color2 = 'red'
        ax2.set_ylabel('Valor de mortes violentas')
        ax2.plot(df_state['ano'], df_state['valor'], marker='s', color=color2, label='Valor')
        ax2.tick_params(axis='y', labelcolor=color2)

        ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:.0f} (mil)'))

        plt.title(f'Evolução do Gini e Valor de mortes violentas em {UF}')
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def plot_correlation_heatmap(self, states):
        
        if isinstance(states, str):
            states = [states]

        df_filtered = self.df[self.df["UF"].isin(states)]

        corr_data = []

        for uf in states:
            df_uf = df_filtered[df_filtered["UF"] == uf][["ano", "Gini", "valor"]].dropna()
            if len(df_uf) > 1:
                corr = df_uf.corr().loc["Gini", "valor"]
                corr_data.append({"UF": uf, "Correlação": corr})
            else:
                corr_data.append({"UF": uf, "Correlação": None})
        
        import pandas as pd
        corr_df = pd.DataFrame(corr_data).set_index("UF")

        plt.figure(figsize=(8, len(states) * 0.5 + 2))
        sns.heatmap(corr_df, annot=True, cmap="coolwarm", center=0, vmin=-1, vmax=1, fmt=".2f", linewidths=0.5)
        plt.title("Correlação entre Gini e Mortes Violentas por Estado")
        plt.tight_layout()
        plt.show()